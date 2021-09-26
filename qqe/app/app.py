from qq import Application
from qq.plugins import SettingsPlugin
from qq.plugins.celery.plugin import CeleryPlugin

from qqe.capp import celery_app


class QqeApplication(Application):
    def create_plugins(self):
        self.plugins[SettingsPlugin.DEFAULT_KEY] = SettingsPlugin("qqe.app.settings")
        self.plugins[CeleryPlugin.DEFAULT_KEY] = CeleryPlugin(celery_app)


application = QqeApplication()
