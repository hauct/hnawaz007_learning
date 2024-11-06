# fmt: off
from dagster import Definitions, load_assets_from_modules
from .assets import product_category
from .io.file_io import LocalFileSystemIOManager
from .io.db_io import PostgresDataframeIOManager
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Get Postgres credentials from environment variables
postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_host = os.getenv('POSTGRES_HOST')
postgres_port = os.getenv('POSTGRES_PORT')
postgres_db = os.getenv('POSTGRES_DB')

product_category_assets = load_assets_from_modules([product_category])

defs = Definitions(
    assets=[*product_category_assets],
    resources={
        "file_io": LocalFileSystemIOManager(),
        "db_io": PostgresDataframeIOManager(
            uid=postgres_user,
            pwd=postgres_password,
            server=postgres_host,
            port=postgres_port,
            db=postgres_db
        )
    }
)


