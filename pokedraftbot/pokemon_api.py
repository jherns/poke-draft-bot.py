import requests

class PokemonApi:
    def __init__(self):
        self.host_name = "https://pokeapi.co/api/v2/"
    
    def getPokemon(self, pokemon):
        try:
            url = f"{self.host_name}/pokemon/{pokemon}"
            return requests.get(url)
        except:
            print(f"An error occured fetching data for {pokemon}")
