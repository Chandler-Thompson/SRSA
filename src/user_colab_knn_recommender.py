# -*- coding: utf-8 -*-
"""User_Colab_KNN_Recommender.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iFsoaRBGPS7LAdx_g3L1BO2nhZ9o_BXV
"""

# from google.colab import drive
# drive.mount('/content/drive', force_remount=True)

# Commented out IPython magic to ensure Python compatibility.
# %cd '/content/drive/My Drive/Colab Notebooks/'
# %run Data_Parser.ipynb
import pandas as pd

def users_games_to_dict():
  users_games = get_parsed_data([False, True, False, False, False])
  users_games_dict = {}

  print('Converting User\'s Games to Dictionary...')

  for user in users_games[0]:
    users_games_dict[user['steam_id']] = user

  print(users_games_dict['76561197970982479'])# should output user with 277 'items_count'

  return users_games_dict

def create_playtime_matrix():
  game_df = get_user_game_sparse_matrix()
  users_dict = users_games_to_dict()

  print('Creating Playtime Matrix...')

  index = 0
  for userID, user in users_dict.items():
    print(str(index)+']Getting Playtimes from User '+str(user['user_id'])+'\'s '+str(len(user['items']))+' games.')
    index += 1
    for game in user['items']:
      game_df.at[userID, game['item_name']] = game['playtime_forever']

  return game_df

print(create_playtime_matrix().head())