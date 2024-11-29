from pydantic import Field
from pydantic_settings import BaseSettings


class CdtToNexumSettings(BaseSettings):
    airflow_home: str = Field(default="$PWD", alias="AIRFLOW_HOME", min_length=1)
    gcp_project: str = Field(default="", alias="GCP_PROJECT")
    google_application_credentials: str = Field(alias="GOOGLE_APPLICATION_CREDENTIALS")
    cdt_dataset: str = Field(default="cdt_ovo_to_nexum", alias="CDT_DATASET")
    google_cloud_project: str = Field(default="nexum-dev", alias="GOOGLE_CLOUD_PROJECT")
    no_proxy: str = Field(default="*", alias="no_proxy")
    dataset_output_env: str = Field(default="$(git rev-parse --abbrev-ref HEAD)", alias="DATASET_OUTPUT_ENV")
    inttest_dset: str = Field(default="integration_test", alias="INTTEST_DSET")
