"""Config.

This module contains the configuration settings for the application.
These values can be overridden by environment variables.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings."""

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
    )

    service_url: str = 'https://api.hunter.io/v2'
    api_key: str = ''


settings = Settings()
