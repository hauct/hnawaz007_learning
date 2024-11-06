{{config(materialized='table')}}

with source_data as (
    select * 
    from {{ source('src_postgres_production', 'productcategory') }}
)

select *
from source_data