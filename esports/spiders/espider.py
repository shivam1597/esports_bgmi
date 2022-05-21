import json
import scrapy
from esports.items import EsportsItem
# import requests as Request
from scrapy import Request
class ESpider(scrapy.Spider):

    name = "spider"
    star_urls = ["https://api.tmp.tesseractesports.com/rounds/stats/628340b04ff9fb0cdc082df2"]

    def start_requests(self):

        url = "https://api.tmp.tesseractesports.com/rounds/stats/628340b04ff9fb0cdc082df2"
        yield Request(url=url)

        # yield Request(url=url)

    def parse(self, response, **kwargs):
        
        player_data = EsportsItem()
        self.logger.info(type(response.body.decode('utf-8')))
        json_data = json.loads(response.body.decode('utf-8'))
        teams_data_list = json_data.get('teams')

        for team_data in teams_data_list:
            all_players = team_data['players']
            for player in all_players:
                # print('city' in player)
                # print(player.get("IngameName"))
                player_data['player_team_logo'] = team_data.get("Logo").get("formats").get("thumbnail").get("url")
                player_data['player_team_name'] = team_data.get("Name")
                player_data['player_name'] = player.get("Name")# + ' ' + player.get("lastname")
                player_data['player_ig_name'] = player.get("IngameName")
                player_data["player_mobile"] = player.get("Mobile")
                player_data["player_game_id"] = player.get("username")
                player_data["player_email"] = player.get("email")
                player_data["player_id_proof"] = player.get("dob_proof")
                player_data["player_dob"] = player.get("dob")
                player_data["player_photo"] = player.get("Photo").get("formats").get("thumbnail").get("url")
                player_data["player_city"] = player.get("city")
                player_data["player_state"] = player.get("state")

                yield player_data
        
# login = WebLogin()
# login.automate()