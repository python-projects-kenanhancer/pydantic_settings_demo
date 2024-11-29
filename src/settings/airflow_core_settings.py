from pydantic import Field
from pydantic_settings import BaseSettings


class AirflowCoreSettings(BaseSettings):
    fernet_key: str = Field(default="", alias="AIRFLOW__CORE__FERNET_KEY")
    dags_are_paused_at_creation: bool = Field(default=True, alias="AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION")
    load_examples: bool = Field(default=False, alias="AIRFLOW__CORE__LOAD_EXAMPLES")
    airflow_uid: int
