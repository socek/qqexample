from fastapi import FastAPI
from qqe.sample.models import get_proccess_info
from qqe.sample.models import get_settings_info

fastapp = FastAPI()


@fastapp.get("/")
async def root():
    return {
        "get_proccess_info": get_proccess_info(),
        "get_settings_info": get_settings_info(),
    }
