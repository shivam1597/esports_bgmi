# Scrapy settings for esports project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'esports'
LOG_LEVEL = 'INFO'
SPIDER_MODULES = ['esports.spiders']
NEWSPIDER_MODULE = 'esports.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'esports (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False
HTTPERROR_ALLOWED_CODES  =[404]

ITEM_PIPELINES = {
   'esports.pipelines.EsportsPipeline': 300,
}

FEED_EXPORTERS = {'csv': 'esports.exporter.Exporter'}
CSV_DELIMITER = '|'
FEED_EXPORT_FIELDS = ['esports']
FEED_STORAGE = 'esports.exporter.FeedStorage'
FEED_EXPORT_FIELDS = [
   'player_team_logo',
   'player_team_name',
   'player_name',
   'player_ig_name',
   'player_mobile',
   'player_game_id',
   'player_email',
   'player_id_proof',
   'player_dob',
   'player_photo',
   'player_city',
   'player_state'
   ]
# FEED_STORAGES = {"irftp": "esports.filestorage.FeedStorage"}
FILE_NAME = "/tmp/Esports.csv"
FEED_EXPORTERS = {"csv": "esports.exporter.Exporter"}