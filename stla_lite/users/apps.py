from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'stla_lite.users'
    verbose_name = "Users"

    def ready(self):
        """
        TODO: Check to see if Employee ID number in database.
        Check to see if supervisor email in database.
        """
        pass
