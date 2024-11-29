from typing import Any

from pydantic_settings import BaseSettings


class FeatureFlagsSettings(BaseSettings):
    split_balances_enabled: bool
    circuit_breaker_enabled: bool
    circuit_breaker_checks_subset_config: dict[str, Any]
    circuit_breaker_duration: int
