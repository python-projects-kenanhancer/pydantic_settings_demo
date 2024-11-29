from pydantic import Field
from pydantic_settings import BaseSettings


class BackendDBSettings(BaseSettings):
    sql_alchemy_conn: str = Field(alias="AIRFLOW__DATABASE__SQL_ALCHEMY_CONN")
    load_default_connections: bool = Field(default=False, alias="AIRFLOW__DATABASE__LOAD_DEFAULT_CONNECTIONS")
