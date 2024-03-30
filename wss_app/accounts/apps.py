from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wss_app.accounts'

    def ready(self):
        import wss_app.accounts.signals
