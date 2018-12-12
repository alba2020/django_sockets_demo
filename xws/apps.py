from django.apps import AppConfig


class XwsConfig(AppConfig):
    name = 'xws'
    
    def ready(self):
            import xws.signals
