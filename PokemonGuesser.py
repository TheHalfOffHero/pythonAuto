# Program: Who's that Pokemon
# date: August 25th, 2022
# Created By: Matthew Ruiz

from ast import Try
from urllib import response
from webbrowser import get
import requests, random, json

#
#  Variables
#   
api_url_base = "https://pokeapi.co/api/v2/pokemon/"
pokemonRange = 151


def getRandomPokemon():
    api_url = api_url_base + str(random.randint(0,pokemonRange))
    jsonString = requests.get(api_url)
    response = jsonString.json()

    pokemonName = (response['forms'])[0]['name']
    try:
        pokemonTypePrimary = response['types'][0]['type']['name']
        pokemonTypeSecondary = response['types'][1]['type']
    except:
      pokemonTypePrimary = response['types'][0]['type']['name']

    return response


getRandomPokemon()
print(getRandomPokemon())