from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    name = 'transactions'

    def ready(self):

        from django.core import management 
        management.call_command('runapscheduler')


