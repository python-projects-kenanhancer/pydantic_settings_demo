import os

from dotenv import load_dotenv


def load_environment_file(env_suffix: str = None):
    if env_suffix:
        env_suffix = env_suffix.lower()
        env_file = f".env.{env_suffix}"
    else:
        env_file = ".env"

    # Construct the absolute path to the .env file in the project's root directory
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    env_path = os.path.join(project_root, env_file)

    if not os.path.exists(env_path):
        raise FileNotFoundError(f"Environment file '{env_file}' not found at '{env_path}'.")

    # Load the new .env file
    load_dotenv(dotenv_path=env_path, override=True)
    return env_path
