spin = input().strip()
charge = input().strip()

particles = [
    {
        "particle": 'Strange',
        "class": 'Quark',
        "spin": '1/2',
        "charge": '-1/3'
    },
    {
        "particle": 'Charm',
        "class": 'Quark',
        "spin": '1/2',
        "charge": '2/3'
    },
    {
        "particle": 'Electron',
        "class": 'Lepton',
        "spin": '1/2',
        "charge": '-1'
    },
    {
        "particle": 'Neutrino',
        "class": 'Lepton',
        "spin": '1/2',
        "charge": '0'
    },
    {
        "particle": 'Photon',
        "class": 'Boson',
        "spin": '1',
        "charge": '0'
    },
]

for particle in particles:
    if particle['spin'] == spin and particle['charge'] == charge:
        print(particle['particle'], particle['class'])
