import unittest
from unittest.mock import patch
from distutils.version import StrictVersion as semver
from ezupdatechecker import EzUpdateStatus

# ToDo: Tests for DNS lookups, string representation etc.


class TestEzUpdateChecker(unittest.TestCase):

    def setUp(self):
        self.ez = EzUpdateStatus(
            dns_domain="boxcakesoftware.com",
            service_name="zapper",
            version='1.0.0',
            autocheck=False
        )

    def tearDown(self):
        pass

    def test_rr_to_semantic_version(self):
        self.assertEqual('1.0.1', str(self.ez.rr_to_semantic_version(['1.0.1'])))
        self.assertEqual('1.0.1', str(self.ez.rr_to_semantic_version(['1.0.1','1.1.1'])))

    def test_is_deprecated(self):
        # Lower
        self.ez.version_data['oldest'] = semver('0.0.0')
        self.assertEqual(False, self.ez.is_deprecated)

        # Equal
        self.ez.version_data['oldest'] = semver('1.0.0')
        self.assertEqual(False, self.ez.is_deprecated)

        # Higher
        self.ez.version_data['oldest'] = semver('1.4.0')
        self.assertEqual(True, self.ez.is_deprecated)

    def test_is_latest(self):
        # Lower
        self.ez.version_data['latest'] = semver('0.0.0')
        self.assertEqual(True, self.ez.is_latest)

        # Equal
        self.ez.version_data['latest'] = semver('1.0.0')
        self.assertEqual(True, self.ez.is_latest)

        # Higher
        self.ez.version_data['latest'] = semver('1.4.0')
        self.assertEqual(False, self.ez.is_latest)

    def test_latest(self):
        self.ez.version_data['latest'] = semver('1.2.3')
        self.assertEqual('1.2.3', self.ez.latest)

    def test_success(self):
        self.ez.nx_errors = 0
        self.assertEqual(True, self.ez.success)

        self.ez.nx_errors = 1
        self.assertEqual(False, self.ez.success)

        self.ez.nx_errors = 2
        self.assertEqual(False, self.ez.success)
