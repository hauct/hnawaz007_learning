from dagster import Out, Output, job, op
import logging
from dagster_getting_started.etl.etl.db_conn import get_postgres_creds

#import needed libraries
from sqlalchemy import text
import pyodbc
import pandas as pd
import os

# extract data from postgresdb
@op(out={"df":Out(is_required=True), "tbl": Out(is_required=True)})
def extract_dim_product_category(context):
    try:
        lgr = logging.getLogger('console_logger')
        table_schema = 'production'
        table_name = 'productcategory'
        engine = get_postgres_creds()
        conn = engine.connect()
        query = text(
            f"""SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = '{table_schema}'
            AND table_name = '{table_name}'"""
        )
        result = conn.execute(query)
        src_tables = result.fetchall()
        for tbl in src_tables:
            #query and load save data to dataframe
            df = pd.read_sql_query(f'select * FROM {table_schema}.{tbl[0]}', conn)
            #logging table name
            context.log.info("table name " + str(tbl[0]))
            context.log.info(df.head())
            lgr.error("table name " + str(tbl[0]) )
            lgr.error(df)

            yield Output(df, "df")
            yield Output(tbl[0], "tbl")
    except Exception as e:
        print("Data extract error: " + str(e))

# load data from postgresdb
@op
def load_dim_product_category(context, df, tbl):
    try:
        lgr = logging.getLogger('console_logger')
        rows_imported = 0
        # print info and errors
        lgr.error("table received name " + str(tbl))
        context.log.info(df.head())
        lgr.error(df.head())
        lgr.error(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
        engine = get_postgres_creds()
        df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False, schema="public")
        rows_imported += len(df)
        # print success message
        context.log.info("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))
        lgr.error(str(e))



