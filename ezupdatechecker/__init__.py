# -*- coding: utf-8 -*-
#
#  ezupdatenotifer, A tiny module to assist in notifying users of software updates through DNS
#  https://github.com/boxcake/ezupdatechecker

from distutils.version import StrictVersion as semver
import dns.resolver
import logging

__version_info__ = (0, 9, 0)
__version__ = '.'.join(str(v) for v in __version_info__)


class EzUpdateStatus(object):

    __check_names = ['latest', 'oldest']

    def __init__(self, **kwargs):
        self.log = logging.getLogger(__name__)

        log_level = logging.DEBUG if kwargs.get('debug',False) else logging.ERROR
        self.log.setLevel(log_level)

        self.auto_check = kwargs.get('autocheck', True)

        self.service_name = kwargs['service_name']
        self.base_dns_domain = kwargs['dns_domain']

        self.nx_errors = 0

        self.version_data = {
            'current': semver(kwargs.get('version'))}

        if self.auto_check:
            self.check()

    def check(self):
        self.nx_errors = self.query_dns_records()

    def query_dns_records(self):
        resolver = dns.resolver.Resolver()
        nx_errors = 0

        for version_name in EzUpdateStatus.__check_names:
            query_host = f"_{self.service_name}_{version_name}.{self.base_dns_domain}"
            try:
                result = resolver.query(
                    query_host,
                    "TXT"
                )
            except dns.resolver.NXDOMAIN:
                self.log.warning(f"NX for {query_host}")
                nx_errors += 1
                result = [self.version_data['current']]
            finally:
                version_number = self.rr_to_semantic_version(result)
                self.log.debug(f"{version_name} = {version_number}")
                self.version_data[version_name] = version_number

        return nx_errors

    def __str__(self):
        return str({
            'CurrentVersion': str(self.version_data['current']),
            'LatestVersion': str(self.version_data['latest']),
            'Deprecated': self.is_deprecated,
            'Latest': self.is_latest,
            'Successful': self.success
        })

    @staticmethod
    def rr_to_semantic_version(rdata):
        first_result = rdata[0]
        return semver(str(first_result).replace('"',''))

    @property
    def is_deprecated(self):
        return True if self.version_data['current'] < self.version_data['oldest'] else False

    @property
    def is_latest(self):
        return True if self.version_data['current'] >= self.version_data['latest'] else False

    @property
    def latest(self):
        return str(self.version_data['latest'])

    @property
    def success(self):
        return True if not self.nx_errors else False

