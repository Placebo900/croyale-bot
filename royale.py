import requests
import json
import time

ACCESS_TOKEN = '' # write token

class CRoyale:
    
    def __init__(self, action=None, p_tag=None, c_tag=None, l_tag=None, tour_tag=None):
        self.action = action
        self.p_tag = p_tag
        self.c_tag = c_tag
        self.l_tag = l_tag
        self.tour_tag = tour_tag
        self.response = None
    
    def __str__(self):
        return self.response
        

    def get_clan_warlog(self):
        url = f'https://api.clashroyale.com/v1/clans/{self.c_tag}/warlog'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_clans(self):
        url = f'https://api.clashroyale.com/v1/clans'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_riverracelog_clan(self):
        url = f'https://api.clashroyale.com/v1/clans/{self.c_tag}/riverracelog'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp
    

    def get_clan_info(self):
        url = f'https://api.clashroyale.com/v1/clans/{self.c_tag}'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_members(self):
        url = f'https://api.clashroyale.com/v1/clans/{self.c_tag}/members'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_currentriverrace(self):
        url = f'https://api.clashroyale.com/v1/clans/{self.c_tag}/currentriverrace'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp



    def get_player_info(self):
        url = f'https://api.clashroyale.com/v1/players/{self.p_tag}'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_chests(self):
        url = f'https://api.clashroyale.com/v1/players/{self.p_tag}/upcomingchests'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_battlelog(self):
        url = f'https://api.clashroyale.com/v1/players/{self.p_tag}'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp



    def get_cards(self):
        url = f'https://api.clashroyale.com/v1/cards'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp



    def search_tournaments(self):
        url = f'https://api.clashroyale.com/v1/tournaments'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_tournament(self):
        url = f'https://api.clashroyale.com/v1/tournaments/{self.tour_tag}'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp



    def get_location_clan_rank(self):
        url = f'https://api.clashroyale.com/v1/locations/{self.l_tag}/rankings/clans'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_location_player_rank(self):
        url = f'https://api.clashroyale.com/v1/locations/{self.l_tag}/rankings/players'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_location_clanwars_rank(self):
        url = f'https://api.clashroyale.com/v1/locations/{self.l_tag}/rankings/clanwars'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_top_players_leauge_season(self):
        url = f'https://api.clashroyale.com/v1/locations/global/seasons/{self.l_tag}'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp
    
    def get_top_player_rank_season(self):
        url = f'https://api.clashroyale.com/v1/locations/global/seasons/{self.l_tag}/rankings/players'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_list_top_player_seasons(self):
        url = f'https://api.clashroyale.com/v1/locations/global/seasons'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_list_locations(self):
        url = f'https://api.clashroyale.com/v1/locations'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_location_info(self):
        url = f'https://api.clashroyale.com/v1/locations/{self.l_tag}'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp

    def get_global_tournament_rankings(self):
        url = f'https://api.clashroyale.com/v1/locations/global/rankings/tournamens/{self.l_tag}'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp



    def get_list_global_tournaments(self):
        url = f'https://api.clashroyale.com/v1/globaltournamens'
        resp = requests.get(url, params={
            'Authorization' : f'Bearer {ACCESS_TOKEN}'
        })
        self.response = resp
    

    def analyze_current_cw(self):
        self.get_currentriverrace()
        cw_info = json.loads(self.response.text)
        cw_self_clan = cw_info['clan']
        cw_self_clan['participants'].sort(key=lambda x: (-x['fame'], -x['repairPoints'], -x['boatAttacks'], -x['decksUsed'], -x['decksUsedToday']))
        with open('analyze_current_cw', 'w') as f:
            f.write('Итоги гонки на данный момент:\n')
            for i in range(len(cw_self_clan['participants'])):
                if cw_self_clan["participants"][i]['fame'] == cw_self_clan["participants"][i]["repairPoints"] == cw_self_clan["participants"][i]["boatAttacks"] \
                == cw_self_clan["participants"][i]["decksUsed"] == 0 :
                    break
                f.write(f'\t{i + 1}. {cw_self_clan["participants"][i]["name"]}: {cw_self_clan["participants"][i]["fame"]} медалей, ' \
                    f'{cw_self_clan["participants"][i]["repairPoints"]} очков с починки, {cw_self_clan["participants"][i]["boatAttacks"]} атак лодки, '\
                        f'{cw_self_clan["participants"][i]["decksUsed"]} использовано колод.\n')
        return cw_self_clan

    
    def analyze_cw(self, min_fames=0):
        self.get_riverracelog_clan()
        cw_info = json.loads(self.response.text)
        cw_info = cw_info['items'][0]['standings']
        for a in cw_info:
            if a['clan']['tag'] == '#' + self.tag[3:]:
                cw_info_self = a['clan']
                break
        cw_info_self['participants'].sort(key=lambda x: (-x['fame'], -x['repairPoints'], -x['boatAttacks'], -x['decksUsed'], -x['decksUsedToday']))
        with open('analyze_cw', 'w') as f:
            f.write('Итоги прошедшей гонки:\n')
            for i in range(len(cw_info_self['participants'])):
                if cw_info_self["participants"][i]['fame'] == cw_info_self["participants"][i]["repairPoints"] == cw_info_self["participants"][i]["boatAttacks"] \
                == cw_info_self["participants"][i]["decksUsed"] <= min_fames:
                    break
                f.write(f'\t{i + 1}. {cw_info_self["participants"][i]["name"]}: {cw_info_self["participants"][i]["fame"]} медалей, ' \
                    f'{cw_info_self["participants"][i]["repairPoints"]} очков с починки, {cw_info_self["participants"][i]["boatAttacks"]} атак лодки, '\
                        f'{cw_info_self["participants"][i]["decksUsed"]} использовано колод.\n')
        return cw_info_self

    def analyze_donates(self, min_donates=0):
        self.get_members()
        donates_info = json.loads(self.response.text)
        donates_self_info = donates_info['items']
        donates_self_info.sort(key=lambda x: (-x['donations']))
        with open('analyze_donates', 'w') as f:
            f.write('Донаты игроков:\n')
            for i in range(len(donates_self_info)):
                if donates_self_info[i]['donations'] <= min_donates:
                    break
                f.write(f'\t{i + 1}. {donates_self_info[i]["name"]}: {donates_self_info[i]["donations"]}\n')
        return donates_self_info

    def analyze_player(self):
        self.get_player_info()
        player_info = json.loads(self.response.text)
        coef_win = player_info["wins"] / player_info["battleCount"]
        coef_win_loss = player_info["wins"] / player_info["losses"]
        p_date = player_info["leagueStatistics"]["bestSeason"]["id"]
        p_trophies = player_info["leagueStatistics"]["bestSeason"]["trophies"]
        with open('analyze_player', 'w') as f:
            f.write('Информация об игроке:\n')
            f.write(f'\tИмя: {player_info["name"]}\n')
            f.write(f'\tВсего игр: {player_info["battleCount"]}, побед: {player_info["wins"]}, коэффициент победы/все игры: {coef_win:.2f}\n')
            f.write(f'\tКоэффициент победы/поражения: {coef_win_loss:.2f}\n')
            f.write(f'\tЛучший сезон: год - {p_date}, трофеи - {p_trophies}')
        return player_info


    def analyze_chests(self):
        self.get_chests()
        chests_info = json.loads(self.response.text)
        with open('analyze_chests', 'w') as f:
            f.write('Ближайшие сундуки:\n')
            for chest in chests_info['items']:
                f.write(f'\t{chest["index"] + 1}. {chest["name"]}\n')
        return chests_info

    
    funcs = {
        'get_clan_warlog' : get_clan_warlog, 'get_clans' : get_clans, 'get_riverracelog_clan' : get_riverracelog_clan,
        'get_clan_info' : get_clan_info, 'get_members' : get_members, 'get_currentriverrace' : get_currentriverrace, 'get_player_info' : get_player_info, 'get_chests' : get_chests,
        'get_battlelog' : get_battlelog, 'get_cards' : get_cards, 'search_tournaments' : search_tournaments, 'get_location_clan_rank' : get_location_clan_rank,
        'get_location_player_rank' : get_location_player_rank, 'get_location_clanwars_rank' : get_location_clanwars_rank, 'get_location_clanwars_rank' : get_location_clanwars_rank,
        'get_top_players_leauge_season' : get_top_players_leauge_season, 'get_top_player_rank_season' : get_top_player_rank_season, 'get_list_top_player_seasons' : get_list_top_player_seasons,
        'get_list_locations' : get_list_locations, 'get_location_info' : get_location_info, 'get_global_tournament_rankings' : get_global_tournament_rankings, 'get_list_global_tournaments' : get_list_global_tournaments,
        'analyze_current_cw' : analyze_current_cw, 'analyze_cw' : analyze_cw, 'analyze_donates' : analyze_donates, 'analyze_player' : analyze_player, 'analyze_chests' : analyze_chests
    }


    def call_func(self, *args, **kwargs):
        try:
            CRoyale.funcs[self.action](self, *args, **kwargs)
        except Exception as err:
            raise TimeoutError('!!!royale!!!', err)



cache = CRoyale()
