from dagster import asset
from etl.resources.db_conn import get_postgres_creds
from sqlalchemy import text

import pandas as pd
import logging

# Extract data from postgresdb
@asset(group_name='ProductCatergory', compute_kind='pandas', io_manager_key='file_io')
def extract_dim_product_category(context) -> pd.DataFrame:
    "Extract data from PostgresDB"
    table_schema = 'production'
    table_name = 'productcategory'
    engine = get_postgres_creds()
    conn = engine.connect()
    df = pd.read_sql_query(f'select * FROM {table_schema}.{table_name}', conn)
    return df

# Load data
@asset(group_name='ProductCatergory', compute_kind='pandas', io_manager_key='db_io')
def rename_dim_product_category(context, extract_dim_product_category: pd.DataFrame) -> pd.DataFrame:
    "Transform and Stage data in PostgresDB"
    try:
        context.log.info(extract_dim_product_category.head())
        df = extract_dim_product_category[['productcategoryid', 'name']]
        df = df.rename(columns={'productcategoryid': 'productcategory_id'})
        return df
    except Exception as e:
        context.log.info(str(e))