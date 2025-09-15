from django.apps import AppConfig


class MyappConfig(AppConfig):
    verbose_name = "Excellent App"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
