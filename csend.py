from qqe import application
from qqe.capp.tasks import celeryprint

if __name__ == "__main__":
    application.start("command")
    celeryprint.delay()
    print("Send task to queue...")
