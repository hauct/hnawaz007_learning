{{config(materialized='table')}}

with source_data as (
    select * 
    from {{ source('src_postgres_address', 'address') }}
)

select *
from source_data