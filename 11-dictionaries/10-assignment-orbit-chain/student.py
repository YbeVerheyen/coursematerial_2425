orbits = {
    'Moon': 'Earth',
    'Mars': 'Sun',
    'Earth': 'Sun',
    'Jupiter': 'Sun',
    'Saturn': 'Sun',
    'Sun': 'Sagittarius A*',
    'Phobos': 'Mars',
    'Ganymede': 'Jupiter',
    'Callisto': 'Jupiter',
    'Europa': 'Jupiter',
}

def orbit_chain(orbits, start):
    chain = [start]
    new_orbit = start
    while new_orbit in orbits:
        new_orbit = orbits[new_orbit]
        chain.append(new_orbit)
    return chain
        