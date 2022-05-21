# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EsportsItem(scrapy.Item):
    # define the fields for your item here like:
    player_team_logo = scrapy.Field()
    player_team_name = scrapy.Field()
    player_name = scrapy.Field()
    player_ig_name = scrapy.Field()
    player_mobile = scrapy.Field()
    player_game_id = scrapy.Field()
    player_email = scrapy.Field()
    player_id_proof = scrapy.Field()
    player_dob = scrapy.Field()
    player_photo = scrapy.Field()
    player_city = scrapy.Field()
    player_state = scrapy.Field()