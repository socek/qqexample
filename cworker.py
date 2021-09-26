from qq.plugins.celery.finder import TaskFinder

from qqe import application
from qqe.capp import celery_app

application.start("celery")
TaskFinder(["qqe"], celery_app=celery_app).find()
print("Starting celery")
