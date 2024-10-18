# fmt: off
from dagster import Definitions
from .jobs import run_etl_job

defs = Definitions(
    jobs=[run_etl_job],
)