"""
Tests for custom Django management commands related to database readiness.
These tests ensure that the commands handle scenarios where the database is ready or unavailable.
"""

from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    '''test commands.'''


    def test_wait_for_db_ready(self, patched_check):
        '''test waiting for database if database ready'''
        
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])



    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """test waiting for database when getting OperationalError.

        Args:
            patched_check (_type_): _description_
        """

        patched_check.side_effect = [Psycopg2Error] * 2 + \
            [OperationalError] * 3 + [True]
        
        patched_sleep(2)
        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
