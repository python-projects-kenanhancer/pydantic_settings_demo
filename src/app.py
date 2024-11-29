from settings import Settings, load_environment_file


def main():
    load_environment_file("dev")

    settings = Settings()

    print(f"project_env: {settings.project_env.value}")

    print(f"meta_database: {settings.meta_database.model_dump_json()}")

    print(f"airflow_core: {settings.airflow_core.model_dump_json()}")

    print(f"airflow_init: {settings.airflow_init.model_dump_json()}")

    print(f"backend_db: {settings.backend_db.model_dump_json()}")

    print(f"settings: {settings.model_dump_json()}")


if __name__ == "__main__":
    main()
