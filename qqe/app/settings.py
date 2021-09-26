from decouple import config

from qq.plugins.types import Settings


def default() -> Settings:
    return {"samplesettings": samplesettings(), "process": None, "celery": celerysettings()}


def samplesettings() -> Settings:
    return "default settings value"


def celerysettings() -> Settings:
    host = config("QQE_BROKER_HOST", "localhost")
    user = config("QQE_BROKER_USER", "guest")
    password = config("QQE_BROKER_PASSWORD", "guest")
    vhost = config("QQE_BROKER_VHOST", "")
    port = config("QQE_BROKER_PORT", 5672, cast=int)

    return {
        "broker_url": f"amqp://{user}:{password}@{host}:{port}/{vhost}/",
    }


def command() -> Settings:
    settings = default()
    settings["process"] = "command"
    return settings


def fastapi() -> Settings:
    settings = default()
    settings["process"] = "fastapi"
    return settings


def celery() -> Settings:
    settings = default()
    settings["process"] = "celery"
    return settings
