__author__ = 'dstrohl'
import os
import unittest
import django
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'AdvConfigMgr.tests.test_settings'
django.setup()

# from ..config_django.models import ConfigSections, ConfigOptions

DCM = getattr(settings, 'DJANGO_CONFIGURATION_MANAGER')

class TestDjangoConfig(unittest.TestCase):

    def SetUp(self):
        pass

    def test_base_load(self):
        self.assertEqual(DCM['django_config_manager']['show_in_admin'], True)


    def test_update_config(self):
        pass




'''
if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests"])
    sys.exit(bool(failures))
'''