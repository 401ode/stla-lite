from django.apps import AppConfig


class TimesheetsConfig(AppConfig):
    name = 'stla_lite.timesheets'
    verbose_name = "Timesheets"

    def ready(self):
        """
        Placeholder.
        """
        pass
