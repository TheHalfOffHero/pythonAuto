# Program: Who's that Pokemon
# date: August 25th, 2022
# Created By: Matthew Ruiz

from ast import Try
from unicodedata import name
from urllib import response
from webbrowser import get
import requests, random, json

#
#  Variables
#   
api_url_base = "https://pokeapi.co/api/v2/pokemon/"
pokemonRange = 151

#
# Class Definitions
#
class Pokemon:
  def __init__(self, name, type1, type2="none"):
    self.name = name
    self.type1 = type1
    self.type2 = type2

  def __str__(self) -> str:
    return 'Your Random Pokemon: {name}    Type: {type1}      Secondary Type: {type2}'.format(name=self.name,type1=self.type1,type2=self.type2 )

#

#
# Function Definitions
#

def getRandomPokemon():
    api_url = api_url_base + str(random.randint(1,pokemonRange))
    jsonString = requests.get(api_url)
    response = jsonString.json()

    pokemonName = (response['forms'])[0]['name']
    try:
        pokemonTypePrimary = response['types'][0]['type']['name']
        pokemonTypeSecondary = response['types'][1]['type']['name']
    except:
      pokemonTypePrimary = response['types'][0]['type']['name']
      pokemonTypeSecondary = "none"

    randomPokemon = Pokemon(pokemonName, pokemonTypePrimary, pokemonTypeSecondary)

    return randomPokemon


getRandomPokemon()
print(str(getRandomPokemon()))