from setuptools import find_packages, setup

setup(
    name="dagster",
    packages=find_packages(exclude=["etl_tests"]),
    install_requires=[
        "dagster==1.7.*",
        "dagster-cloud",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
