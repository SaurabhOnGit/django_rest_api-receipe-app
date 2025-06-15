"""
Django command to wait for DB to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """command to wait for db
    """
    help = 'Description of your command'

    # def add_arguments(self, parser):
    #     parser.add_argument('name', type=str, help='The name to greet')

    def handle(self, *args, **options):
        """entrypoint for command."""
        self.stdout.write('waiting for database to up...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('database unavailable. waiting 2 seconds...')
                time.sleep(2)

        self.stdout.write(self.style.SUCCESS("Database available!"))

        # name = options['name']
        # self.stdout.write("This is my custom command!")

    # def check(self, *args, **options):
    #     pass
