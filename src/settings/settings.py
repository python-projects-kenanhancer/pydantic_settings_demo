from pydantic_settings import BaseSettings

from settings import (
    AirflowCoreSettings,
    AirflowInitSettings,
    BackendDBSettings,
    CdtToNexumSettings,
    Environment,
    FeatureFlagsSettings,
    MetaDatabaseSettings,
)


class Settings(BaseSettings):
    project_env: Environment

    feature_flags: FeatureFlagsSettings
    meta_database: MetaDatabaseSettings
    backend_db: BackendDBSettings
    airflow_init: AirflowInitSettings
    airflow_core: AirflowCoreSettings
    cdt_to_nexum: CdtToNexumSettings

    def __init__(self):
        super().__init__(
            feature_flags=FeatureFlagsSettings(),
            meta_database=MetaDatabaseSettings(),
            backend_db=BackendDBSettings(),
            airflow_init=AirflowInitSettings(),
            airflow_core=AirflowCoreSettings(),
            cdt_to_nexum=CdtToNexumSettings(),
        )
