{{config(materialized='table')}}

with source_data as (
    select * 
    from {{ source('src_postgres', 'productcategory') }}
)

select *
from source_data