from qqe.capp import celery_app
from qqe.sample.models import get_proccess_info
from qqe.sample.models import get_settings_info


@celery_app.task
def celeryprint():
    print("This is a celery task:")
    print(f"\t{get_settings_info()}")
    print("")
    print("Proccess info:")
    print(f"\t{get_proccess_info()}")
