# Dies ist eine Instanzdatei mit konkreten Daten, Sie muessen diese Datei nicht aendern!

from gurobipy import *

# places: Liste der Staedte (als str)
places = ['Seehafen', 'Lokschuppen', 'Palast', 'Post', 'Supermarkt', 'Verlies']

# costs: Dictionary der Transportcosts einer Charge pro Stunde: z.B.: costs["Printen"] = 2
goods, costs = multidict({
    'Printen': 2,
    'Lennet Bier': 0.5,
    'RWTH Tassen': 0.2
})

# travel_distance: Dictionary der Distanz (in Kilometern) zwischen Paaren von Ortenz.B.: travel_distance['Seehafen', 'Palast'] = 28
# capacities: Dictionary der Kapazitaeten (in Anzahl an Chargen) zwischen Paaren von Orten z.B.: capacities['Seehafen', 'Juelich'] = 70
travel_distance = {(i, j): 0 for i in places for j in places}
capacities = {(i, j): 0 for i in places for j in places}

# availabilities: Dictionary der Verfuegbarkeiten (in Anzahl an Chargen) von Guetern in Orten z.B.: availabilities[('Seehafen','RWTH Tassen')] = 45
# demands: Dictionary der Bedarfe (in Anzahl an Chargen) von Guetern in Orten z.B.: demands[('Seehafen','Printen')] = 20
availabilities = {(i, k): 0 for i in places for k in goods}
demands = {(i, k): 0 for i in places for k in goods}

travel_distance[('Seehafen', 'Lokschuppen')] = 28
travel_distance[('Seehafen', 'Palast')] = 31
travel_distance[('Seehafen', 'Post')] = 32
travel_distance[('Seehafen', 'Supermarkt')] = 16
travel_distance[('Seehafen', 'Verlies')] = 22
travel_distance[('Lokschuppen', 'Seehafen')] = 28
travel_distance[('Lokschuppen', 'Palast')] = 25
travel_distance[('Lokschuppen', 'Post')] = 18
travel_distance[('Lokschuppen', 'Supermarkt')] = 19
travel_distance[('Lokschuppen', 'Verlies')] = 42
travel_distance[('Palast', 'Seehafen')] = 31
travel_distance[('Palast', 'Lokschuppen')] = 25
travel_distance[('Palast', 'Post')] = 41
travel_distance[('Palast', 'Supermarkt')] = 30
travel_distance[('Palast', 'Verlies')] = 15
travel_distance[('Post', 'Seehafen')] = 32
travel_distance[('Post', 'Lokschuppen')] = 18
travel_distance[('Post', 'Palast')] = 41
travel_distance[('Post', 'Supermarkt')] = 19
travel_distance[('Post', 'Verlies')] = 48
travel_distance[('Supermarkt', 'Seehafen')] = 16
travel_distance[('Supermarkt', 'Lokschuppen')] = 19
travel_distance[('Supermarkt', 'Palast')] = 30
travel_distance[('Supermarkt', 'Post')] = 19
travel_distance[('Supermarkt', 'Verlies')] = 32
travel_distance[('Verlies', 'Seehafen')] = 22
travel_distance[('Verlies', 'Lokschuppen')] = 42
travel_distance[('Verlies', 'Palast')] = 15
travel_distance[('Verlies', 'Post')] = 48
travel_distance[('Verlies', 'Supermarkt')] = 32
capacities[('Seehafen', 'Lokschuppen')] = 70
capacities[('Seehafen', 'Palast')] = 70
capacities[('Seehafen', 'Post')] = 60
capacities[('Seehafen', 'Supermarkt')] = 60
capacities[('Seehafen', 'Verlies')] = 50
capacities[('Lokschuppen', 'Seehafen')] = 70
capacities[('Lokschuppen', 'Palast')] = 60
capacities[('Lokschuppen', 'Post')] = 60
capacities[('Lokschuppen', 'Supermarkt')] = 60
capacities[('Lokschuppen', 'Verlies')] = 50
capacities[('Palast', 'Seehafen')] = 70
capacities[('Palast', 'Lokschuppen')] = 60
capacities[('Palast', 'Post')] = 60
capacities[('Palast', 'Supermarkt')] = 60
capacities[('Palast', 'Verlies')] = 50
capacities[('Post', 'Seehafen')] = 60
capacities[('Post', 'Lokschuppen')] = 60
capacities[('Post', 'Palast')] = 60
capacities[('Post', 'Supermarkt')] = 60
capacities[('Post', 'Verlies')] = 50
capacities[('Supermarkt', 'Seehafen')] = 60
capacities[('Supermarkt', 'Lokschuppen')] = 60
capacities[('Supermarkt', 'Palast')] = 60
capacities[('Supermarkt', 'Post')] = 60
capacities[('Supermarkt', 'Verlies')] = 50
capacities[('Verlies', 'Seehafen')] = 50
capacities[('Verlies', 'Lokschuppen')] = 50
capacities[('Verlies', 'Palast')] = 50
capacities[('Verlies', 'Post')] = 50
capacities[('Verlies', 'Supermarkt')] = 50

availabilities[('Seehafen', 'RWTH Tassen')] = 45
availabilities[('Lokschuppen', 'Printen')] = 30
availabilities[('Palast', 'Lennet Bier')] = 35
availabilities[('Post', 'RWTH Tassen')] = 25
availabilities[('Supermarkt', 'Lennet Bier')] = 35
availabilities[('Verlies', 'Printen')] = 20

demands[('Seehafen', 'Printen')] = 20
demands[('Seehafen', 'Lennet Bier')] = 20
demands[('Lokschuppen', 'Lennet Bier')] = 20
demands[('Lokschuppen', 'RWTH Tassen')] = 20
demands[('Palast', 'Printen')] = 10
demands[('Palast', 'RWTH Tassen')] = 10
demands[('Post', 'Printen')] = 10
demands[('Post', 'Lennet Bier')] = 20
demands[('Supermarkt', 'Printen')] = 10
demands[('Supermarkt', 'RWTH Tassen')] = 20
demands[('Verlies', 'Lennet Bier')] = 10
demands[('Verlies', 'RWTH Tassen')] = 20

max_travel = 4000

import lummerland

model = lummerland.solve(places, goods, travel_distance, costs, capacities, availabilities, demands, max_travel)

if not isinstance(model, Model):
    print("solve-Funktion gibt kein Gurobi-Modell zurueck!")
