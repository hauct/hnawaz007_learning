from dagster import file_relative_path, asset
from dagstermill import define_dagstermill_asset

# Asset backed by Jupyter notebook
analytics_notebook = define_dagstermill_asset(
    name='analytics_notebook',
    notebook_path=file_relative_path(__file__, '../../sql_da.ipynb'),
    group_name='Notebooks',
    io_manager_key='local_output_notebook_io_manager'
)

# @asset(group_name='asset')
# def analytics_notebook():
#     print('hello_world')
