from django.shortcuts import render
import requests
import pandas as pd
import numpy as np

def home(request):

    url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    response = requests.get(url)
    json = response.json()
    keys = json.keys()
    elements_df = pd.DataFrame(json['elements'])
    elements_types_df = pd.DataFrame(json['element_types'])
    teams_df = pd.DataFrame(json['teams'])

    elements_df.head()

    slim_elements_df = elements_df[['second_name','team','element_type','selected_by_percent','now_cost','minutes','transfers_in','value_season','total_points']]

    return render(request, 'home.html')


def leaders(request):

    # url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
    url = 'https://api.footystats.org/league-players?key=example&season_id=1625'

    response = requests.get(url)
    try:
        json = response.json()
    except ValueError as e:
        print(e)
    


        # name = element['first_name']+ " " + element['second_name']
        # data[name] = {
        # 'goals_scored': element['goals_scored'],
        # 'assists': element['assists'],
        # 'bonus': element['bonus'],
        # 'clean sheets' : element['clean_sheets'],
        # 'selected_by_percent' : element['selected_by_percent'],
        # 'own_goals': element['own_goals'],
        # 'points_per_game' : element['points_per_game'],
        # 'total_points' : element['total_points']
        # }


    return render(request, 'leaders.html')
