import os


class Config:
    SOURCES_API_BASE_URL = (
        "https://newsapi.org/v2/top-headlines/sources?language=en&apiKey=1844de703b4f4a8fa0bd8a16bf08a6e7"
    )
    SOURCES_API_KEY = os.environ.get("SOURCES_API_KEY")

    ARTICLES_API_BASE_URL = (
        "https://newsapi.org/v2/top-headlines?sources={}&apiKey=1844de703b4f4a8fa0bd8a16bf08a6e7"
    )


class ProdConfig(Config):
    """
    Production configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    """

    pass


class DevConfig(Config):
    """
    Development configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    """

    DEBUG = True


config_options = {"development": DevConfig, "production": ProdConfig}
