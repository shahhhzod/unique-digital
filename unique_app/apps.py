from django.apps import AppConfig


class UniqueAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'unique_app'
