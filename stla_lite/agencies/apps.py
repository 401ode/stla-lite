from django.apps import AppConfig


class AgenciesConfig(AppConfig):
    name = 'stla_lite.agencies'
    verbose_name = "Agencies"

    def ready(self):
        """
        Placeholder.
        """
        pass

