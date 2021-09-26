from qq import SimpleInjector
from qqe import IApp


@IApp
def get_settings_info(settings=SimpleInjector("settings")):
    return settings["samplesettings"]


@IApp
def get_proccess_info(settings=SimpleInjector("settings")):
    return settings["process"]
