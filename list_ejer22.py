from list_ import List

def order_by_name(item):
    return item.name

def order_by_species(item):
    return item.species

class Jedi:
    def __init__(self, name, masters, lightsaber_colors, species, padawans=None):
        self.name = name
        self.masters = masters  
        self.lightsaber_colors = lightsaber_colors 
        self.species = species
        self.padawans = padawans if padawans else [] 
    
    def __str__(self):
        masters_str = ", ".join(self.masters) if self.masters else "Ninguno"
        colors_str = ", ".join(self.lightsaber_colors)
        padawans_str = ", ".join(self.padawans) if self.padawans else "Ninguno"
        return f"{self.name} ({self.species}) - Maestros: {masters_str} - Sables: {colors_str} - Padawans: {padawans_str}"

jedis = List()
jedis.add_criterion('name', order_by_name)
jedis.add_criterion('species', order_by_species)

jedi_data = [
    {
        "name": "Luke Skywalker",
        "masters": ["Obi-Wan Kenobi", "Yoda"],
        "lightsaber_colors": ["azul", "verde"],
        "species": "humana",
        "padawans": ["Ben Solo", "Rey"]
    },
    {
        "name": "Yoda",
        "masters": [],
        "lightsaber_colors": ["verde"],
        "species": "desconocida",
        "padawans": ["Dooku", "Luke Skywalker", "Ki-Adi-Mundi"]
    },
    {
        "name": "Obi-Wan Kenobi",
        "masters": ["Qui-Gon Jinn"],
        "lightsaber_colors": ["azul"],
        "species": "humana",
        "padawans": ["Anakin Skywalker", "Luke Skywalker"]
    },
    {
        "name": "Anakin Skywalker",
        "masters": ["Obi-Wan Kenobi"],
        "lightsaber_colors": ["azul"],
        "species": "humana",
        "padawans": ["Ahsoka Tano"]
    },
    {
        "name": "Ahsoka Tano",
        "masters": ["Anakin Skywalker"],
        "lightsaber_colors": ["verde", "blanco"],
        "species": "togruta",
        "padawans": []
    },
    {
        "name": "Mace Windu",
        "masters": [],
        "lightsaber_colors": ["violeta"],
        "species": "humana",
        "padawans": ["Depa Billaba"]
    },
    {
        "name": "Qui-Gon Jinn",
        "masters": ["Dooku"],
        "lightsaber_colors": ["verde"],
        "species": "humana",
        "padawans": ["Obi-Wan Kenobi"]
    },
    {
        "name": "Kit Fisto",
        "masters": [],
        "lightsaber_colors": ["verde"],
        "species": "nautolano",
        "padawans": ["Nahdar Vebb"]
    },
    {
        "name": "Aayla Secura",
        "masters": ["Quinlan Vos"],
        "lightsaber_colors": ["azul"],
        "species": "twi'lek",
        "padawans": []
    },
    {
        "name": "Plo Koon",
        "masters": [],
        "lightsaber_colors": ["azul", "amarillo"],
        "species": "kel dor",
        "padawans": []
    },
    {
        "name": "Rey",
        "masters": ["Luke Skywalker", "Leia Organa"],
        "lightsaber_colors": ["amarillo"],
        "species": "humana",
        "padawans": []
    }
]

# Agregar Jedi a la lista
for jedi_info in jedi_data:
    jedi = Jedi(
        name=jedi_info["name"],
        masters=jedi_info["masters"],
        lightsaber_colors=jedi_info["lightsaber_colors"],
        species=jedi_info["species"],
        padawans=jedi_info["padawans"]
    )
    jedis.append(jedi)

# a. listado ordenado por nombre y por especie
print("a. Listado ordenado por nombre:")
jedis.sort_by_criterion('name')
for jedi in jedis:
    print(f"  - {jedi.name} ({jedi.species})")

print()
print("a. Listado ordenado por especie:")
jedis.sort_by_criterion('species')
for jedi in jedis:
    print(f"  - {jedi.species}: {jedi.name}")

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto
print("\nb. Información completa de Ahsoka Tano y Kit Fisto:")
for target_name in ["Ahsoka Tano", "Kit Fisto"]:
    index = jedis.search(target_name, 'name')
    if index is not None:
        jedi = jedis[index]
        print(f"  {jedi}")

# c. mostrar todos los padawan de Yoda y Luke Skywalker
print("\nc. Padawans de Yoda y Luke Skywalker:")
for master_name in ["Yoda", "Luke Skywalker"]:
    index = jedis.search(master_name, 'name')
    if index is not None:
        master = jedis[index]
        print(f"  {master_name}: {', '.join(master.padawans) if master.padawans else 'No tuvo padawans'}")

# d. mostrar los Jedi de especie humana y twi'lek
print("\nd. Jedi de especie humana y twi'lek:")
species_filtro = ["humana", "twi'lek"]
for jedi in jedis:
    if jedi.species in species_filtro:
        print(f"  - {jedi.name} ({jedi.species})")

# e. listar todos los Jedi que comienzan con A
print("\ne. Jedi que comienzan con A:") 
for jedi in jedis:
    if jedi.name.startswith('A'):
        print(f"  - {jedi.name}")

# f. mostrar los Jedi que usaron sable de luz de más de un color
print("\nf. Jedi con sables de más de un color:")
for jedi in jedis:
    if len(jedi.lightsaber_colors) > 1:
        colors_str = ", ".join(jedi.lightsaber_colors)
        print(f"  - {jedi.name}: {colors_str}")

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta
print("\ng. Jedi con sables amarillo o violeta:")
target_colors = ["amarillo", "violeta"]
for jedi in jedis:
    for color in jedi.lightsaber_colors:
        if color in target_colors:
            print(f"  - {jedi.name}: {color}")
            break

# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu
print("\nh. Padawans de Qui-Gon Jinn y Mace Windu:")
for master_name in ["Qui-Gon Jinn", "Mace Windu"]:
    index = jedis.search(master_name, 'name')
    if index is not None:
        master = jedis[index]
        padawans = master.padawans
        if padawans:
            print(f"  {master_name}: {', '.join(padawans)}")
        else:
            print(f"  {master_name}: No tuvo padawans")
           