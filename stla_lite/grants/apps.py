from django.apps import AppConfig


class GrantsConfig(AppConfig):
    name = 'stla_lite.grants'
    verbose_name = "Grants"

    def ready(self):
        """
        Placeholder.
        """
        pass
