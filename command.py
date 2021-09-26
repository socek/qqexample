from qqe import application
from qqe.sample.models import get_proccess_info
from qqe.sample.models import get_settings_info


def command_start():
    application.start("command")

    print("This is a command:")
    print(f"\t{get_settings_info()}")
    print("")
    print("Proccess info:")
    print(f"\t{get_proccess_info()}")


if __name__ == "__main__":
    command_start()
