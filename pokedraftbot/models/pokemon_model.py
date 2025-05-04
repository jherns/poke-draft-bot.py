
class PokemonModel:
    def __init__(self, db):
        self.db = db
    
    def is_drafted(self, pokemon_name):
        pass

    def get_cost(self, pokemon_name):
        pass

    def get_similar_pokemon(self, pokemon_name):
        pass

    def get_user_pokemon(self, guild_id, user_id):
        pass

    def get_user_points(self, guild_id, user_id):
        pass

    def draft(self, guild_id, user_id, pokemon_name):
        pass

    def swap(self, guild_id, user_id, new_pokemon_name, old_pokemon_name):
        pass
    
    def __swap_pokemon(self, guild_id, user_id, new_pokemon_name, old_pokemon_name):
        pass
    
    def __draft_pokemon(self, guild_id, user_id, pokemon_name, price):
        pass