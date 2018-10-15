import sys
import ezupdatechecker

# DNS entries are
# _fusscli_latest.fuss.rd.elliemae.io TXT "1.2.0"
# _fusscli_oldest.fuss.rd.elliemae.io TXT "1.0.0"

ez = ezupdatechecker.EzUpdateStatus(
    dns_domain="fuss.rd.elliemae.io",
    service_name="fusscli",
    version='0.1.0'
)

if ez.is_deprecated:
    print(
        f"This version of the client software is deprecated.\n"
        f"Please visit the service page to download version {ez.latest}"
    )
    sys.exit(1)

if not ez.is_latest:
    print(
        f"An update is available {ez.latest}"
    )

if not ez.success:
    print(
        "DNS lookups failed. We fail safe and let the user continue to use the tool"
    )

# This version of the client software is deprecated.
# Please visit the service page to download version 1.2
#
# Process finished with exit code 1
