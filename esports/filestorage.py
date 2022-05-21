"""
Feed Exports extension

See documentation in docs/topics/feed-exports.rst
"""

import os
import logging
import posixpath
import gzip
import shutil
from ftplib import FTP
from scrapy.utils.ftp import ftp_makedirs_cwd
from scrapy.extensions.feedexport import BlockingFeedStorage
from scrapy.utils.project import get_project_settings
import cloudinary

logger = logging.getLogger(__name__)


class FeedStorage(BlockingFeedStorage):
    def __init__(self, uri):
        self.settings = get_project_settings()
        self.settings = get_project_settings()
        cloudinary.config(
            cloud_name="shivam1519",
            api_key="854775435856326",
            api_secret="HvYInSsrqgYDlL0t8ILlS2H-mqk"
        )

    def _store_in_thread(self, file):
        filename = self.settings.get("FILE_NAME")
        if os.path.exists(filename):
            os.remove(filename)
        with open('esports.csv', mode='r+', encoding='utf-8', errors='ignore') as f:
            cloudinary.uploader.upload(f.name, resource_type='raw', use_filename=True,
                                       unique_filename=False)
            print('yessssssssssssssssssssssssssss')
            f.close()
        if os.path.exists('esports.csv'):
            os.remove('esports.csv')
