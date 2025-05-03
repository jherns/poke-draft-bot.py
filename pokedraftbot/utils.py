
def  get_pokemon_info(name, info):
    abilities = info["abilities"]
    stats = info["stats"]
    types = info["types"]

    replies = []
    replies.append(f"Pokemon: {name}")

    abilities_list = []
    for ability in abilities:
       abilities_list.append(ability["ability"]["name"])
    replies.append(f"Abilities: {", ".join(abilities_list)}")

    type_list = []
    for type in types:
       type_list.append(type["type"]["name"])
    replies.append(f"Types: {", ".join(type_list)}")

    for stat in stats:
       replies.append(f"{stat["stat"]["name"].upper()}: {stat["base_stat"]}")
    return "\n".join(replies)