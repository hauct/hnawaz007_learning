# fmt: off
from dagster import Definitions, load_assets_from_modules
from dagstermill import local_output_notebook_io_manager

from .assets import da_asset

all_assets = load_assets_from_modules([da_asset])

defs = Definitions(
    assets=[*all_assets],
    resources={
    "local_output_notebook_io_manager": local_output_notebook_io_manager,
    }
)