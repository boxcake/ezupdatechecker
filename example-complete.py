import ezupdatechecker

# DNS entries are
# _fusscli_latest.fuss.rd.elliemae.io TXT "1.2.0"
# _fusscli_oldest.fuss.rd.elliemae.io TXT "1.0.0"

this_version = ezupdatechecker.EzUpdateStatus(
    dns_domain="fuss.rd.elliemae.io",
    service_name="nonexistantname",
    version='1.2.0'
)

print(str(this_version))

this_version = ezupdatechecker.EzUpdateStatus(
    dns_domain="fuss.rd.elliemae.io",
    service_name="fusscli",
    version='0.9.0'
)

print(str(this_version))

this_version = ezupdatechecker.EzUpdateStatus(
    dns_domain="fuss.rd.elliemae.io",
    service_name="fusscli",
    version='1.1.0'
)

print(str(this_version))


this_version = ezupdatechecker.EzUpdateStatus(
    dns_domain="fuss.rd.elliemae.io",
    service_name="fusscli",
    version='1.2.0'
)

print(str(this_version))

{'Version': '1.2', 'Deprecated': False, 'Latest': True, 'Successful': False}
{'Version': '0.9', 'Deprecated': True, 'Latest': False, 'Successful': True}
{'Version': '1.1', 'Deprecated': False, 'Latest': False, 'Successful': True}
{'Version': '1.2', 'Deprecated': False, 'Latest': True, 'Successful': True}
