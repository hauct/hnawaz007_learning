from setuptools import find_packages, setup

setup(
    name="etl",
    packages=find_packages(exclude=["etl_test"]),
    install_requires=[
        "dagster==1.7.*",
        "dagster-cloud",
        "dagster-duckdb",
        "geopandas",
        "kaleido",
        "pandas",
        "plotly",
        "shapely",
        "logging",
        "pyodbc"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
