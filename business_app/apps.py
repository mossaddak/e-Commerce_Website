from django.apps import AppConfig


class BusinessAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'business_app'

    '''def ready(self):
        import business_app.signals'''
