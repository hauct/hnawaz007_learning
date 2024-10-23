from setuptools import find_packages, setup

setup(
    name="etl",
    packages=find_packages(exclude=["etl_tests"]),
    install_requires=[
        "dagster==1.8.10",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)

# pip install dagster dagster-webserver dagster-cloud dagit

# pip uninstall -y dagster dagster-webserver dagster-cloud dagit