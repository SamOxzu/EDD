f_pokemon = set()
v_pokemon = set()
c_pokemon = set()

while True:
    cmd = input()
    if cmd == '#':
        break
    owner, pokemon_id = cmd.split()
    pokemon_id = int(pokemon_id)
    
    if owner == 'F':
        f_pokemon.add(pokemon_id)
    elif owner == 'V':
        v_pokemon.add(pokemon_id)
    
    c_pokemon.add(pokemon_id)

print(len(f_pokemon), len(v_pokemon), len(c_pokemon))