"""
This plugin searches for Azure Storage Account access keys.
"""
import re

from detect_secrets.plugins.base import RegexBasedDetector


class AzureStorageKeyDetector(RegexBasedDetector):
    """Scans for Azure Storage Account access keys."""
    secret_type = 'Azure Storage Account access key'

    denylist = [
        # Account Key (AccountKey=xxxxxxxxx)
        re.compile(r'AccountKey=[a-zA-Z0-9+\/=]{88}'),
    ]
