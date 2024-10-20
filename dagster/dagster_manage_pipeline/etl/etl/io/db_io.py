from pydantic import BaseModel
import pandas as pd
from sqlalchemy import create_engine
from dagster import ConfigurableIOManager, InputContext, OutputContext

class PostgresDataframeIOManager(ConfigurableIOManager, BaseModel):
    uid: str
    pwd: str
    server: str
    db: str
    port: str

    def handle_output(self, context: OutputContext, obj: pd.DataFrame):
        if obj is None:
            return

        table_name = context.asset_key.to_python_identifier()
        engine = create_engine(f'postgresql://{self.uid}:{self.pwd}@{self.server}:{self.port}/{self.db}')
        obj.to_sql(table_name, engine, if_exists='replace', index=False)

        context.add_output_metadata({"db": self.db, "table_name": table_name})
        
    def load_input(self, context: InputContext):
        table_name = context.upstream_output.asset_key.to_python_identifier()
        engine = create_engine(f'postgresql://{self.uid}:{self.pwd}@{self.server}:{self.port}/{self.db}')
        df = pd.read_sql(f"SELECT * FROM public.{table_name}", engine)
        return df