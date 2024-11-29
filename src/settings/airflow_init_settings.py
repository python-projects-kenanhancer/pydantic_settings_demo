from pydantic import Field
from pydantic_settings import BaseSettings


class AirflowInitSettings(BaseSettings):
    db_upgrade: bool = Field(default=True, alias="_AIRFLOW_DB_UPGRADE")
    www_user_create: bool = Field(default=True, alias="_AIRFLOW_WWW_USER_CREATE")
    www_user_username: str = Field(alias="_AIRFLOW_WWW_USER_USERNAME")
    www_user_password: str = Field(alias="_AIRFLOW_WWW_USER_PASSWORD")
