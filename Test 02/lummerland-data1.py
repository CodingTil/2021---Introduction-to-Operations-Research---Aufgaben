# Dies ist eine Instanzdatei mit konkreten Daten, Sie muessen diese Datei nicht aendern!

from gurobipy import *

# places: Liste der Staedte (als str)
places = ['Seehafen', 'Baecker', 'Koenig_Alfons', 'Frau_Waas', 'Palast', 'Post']

# costs: Dictionary der Transportkosten einer Charge pro Stunde: z.B.: coasts["Brote"]=2
goods, costs = multidict({
    'Brote': 2,
    'Briefe': 0.5,
    'Schokolade': 0.2,
    'Nadeln': 0.35
})

# travel_distance: Dictionary der Distanz (in Kilometern) zwischen Paaren von Orten z.B.: travel_distance['Seehafen', 'Baecker'] = 28
# capacities: Dictionary der Kapazitaeten (in Anzahl an Chargen) zwischen Paaren von Orten z.B.: capacities['Seehafen', 'Baecker'] = 70
travel_distance = {(i, j): 0 for i in places for j in places}
capacities = {(i, j): 0 for i in places for j in places}

# availabilities: Dictionary der Verfuegbarkeiten (in Anzahl an Chargen) von Guetern in Orten z.B.: availabilities[('Seehafen','Schokolade')] = 45
# demands: Dictionary der Bedarfe (in Anzahl an Chargen) von Guetern in Orten z.B.: demands[('Seehafen','Brote')] = 20
availabilities = {(i, k): 0 for i in places for k in goods}
demands = {(i, k): 0 for i in places for k in goods}

travel_distance[('Seehafen', 'Baecker')] = 28
travel_distance[('Seehafen', 'Koenig_Alfons')] = 31
travel_distance[('Seehafen', 'Frau_Waas')] = 32
travel_distance[('Seehafen', 'Palast')] = 16
travel_distance[('Seehafen', 'Post')] = 22
travel_distance[('Baecker', 'Seehafen')] = 28
travel_distance[('Baecker', 'Koenig_Alfons')] = 25
travel_distance[('Baecker', 'Frau_Waas')] = 18
travel_distance[('Baecker', 'Palast')] = 19
travel_distance[('Baecker', 'Post')] = 42
travel_distance[('Koenig_Alfons', 'Seehafen')] = 31
travel_distance[('Koenig_Alfons', 'Baecker')] = 25
travel_distance[('Koenig_Alfons', 'Frau_Waas')] = 41
travel_distance[('Koenig_Alfons', 'Palast')] = 30
travel_distance[('Koenig_Alfons', 'Post')] = 15
travel_distance[('Frau_Waas', 'Seehafen')] = 32
travel_distance[('Frau_Waas', 'Baecker')] = 18
travel_distance[('Frau_Waas', 'Koenig_Alfons')] = 41
travel_distance[('Frau_Waas', 'Palast')] = 19
travel_distance[('Frau_Waas', 'Post')] = 48
travel_distance[('Palast', 'Seehafen')] = 16
travel_distance[('Palast', 'Baecker')] = 19
travel_distance[('Palast', 'Koenig_Alfons')] = 30
travel_distance[('Palast', 'Frau_Waas')] = 19
travel_distance[('Palast', 'Post')] = 32
travel_distance[('Post', 'Seehafen')] = 22
travel_distance[('Post', 'Baecker')] = 42
travel_distance[('Post', 'Koenig_Alfons')] = 15
travel_distance[('Post', 'Frau_Waas')] = 48
travel_distance[('Post', 'Palast')] = 32
capacities[('Seehafen', 'Baecker')] = 70
capacities[('Seehafen', 'Koenig_Alfons')] = 70
capacities[('Seehafen', 'Frau_Waas')] = 60
capacities[('Seehafen', 'Palast')] = 60
capacities[('Seehafen', 'Post')] = 50
capacities[('Baecker', 'Seehafen')] = 70
capacities[('Baecker', 'Koenig_Alfons')] = 60
capacities[('Baecker', 'Frau_Waas')] = 60
capacities[('Baecker', 'Palast')] = 60
capacities[('Baecker', 'Post')] = 50
capacities[('Koenig_Alfons', 'Seehafen')] = 70
capacities[('Koenig_Alfons', 'Baecker')] = 60
capacities[('Koenig_Alfons', 'Frau_Waas')] = 60
capacities[('Koenig_Alfons', 'Palast')] = 60
capacities[('Koenig_Alfons', 'Post')] = 50
capacities[('Frau_Waas', 'Seehafen')] = 60
capacities[('Frau_Waas', 'Baecker')] = 60
capacities[('Frau_Waas', 'Koenig_Alfons')] = 60
capacities[('Frau_Waas', 'Palast')] = 60
capacities[('Frau_Waas', 'Post')] = 50
capacities[('Palast', 'Seehafen')] = 60
capacities[('Palast', 'Baecker')] = 60
capacities[('Palast', 'Koenig_Alfons')] = 60
capacities[('Palast', 'Frau_Waas')] = 60
capacities[('Palast', 'Post')] = 50
capacities[('Post', 'Seehafen')] = 50
capacities[('Post', 'Baecker')] = 50
capacities[('Post', 'Koenig_Alfons')] = 50
capacities[('Post', 'Frau_Waas')] = 50
capacities[('Post', 'Palast')] = 50

availabilities[('Seehafen', 'Schokolade')] = 45
availabilities[('Seehafen', 'Nadeln')] = 40
availabilities[('Baecker', 'Brote')] = 30
availabilities[('Baecker', 'Nadeln')] = 10
availabilities[('Koenig_Alfons', 'Briefe')] = 35
availabilities[('Frau_Waas', 'Schokolade')] = 25
availabilities[('Frau_Waas', 'Nadeln')] = 10
availabilities[('Palast', 'Briefe')] = 35
availabilities[('Post', 'Brote')] = 20

demands[('Seehafen', 'Brote')] = 20
demands[('Seehafen', 'Briefe')] = 20
demands[('Baecker', 'Briefe')] = 20
demands[('Baecker', 'Schokolade')] = 20
demands[('Koenig_Alfons', 'Brote')] = 10
demands[('Koenig_Alfons', 'Schokolade')] = 10
demands[('Koenig_Alfons', 'Nadeln')] = 20
demands[('Frau_Waas', 'Brote')] = 10
demands[('Frau_Waas', 'Briefe')] = 20
demands[('Palast', 'Brote')] = 10
demands[('Palast', 'Schokolade')] = 20
demands[('Palast', 'Nadeln')] = 20
demands[('Post', 'Briefe')] = 10
demands[('Post', 'Schokolade')] = 20
demands[('Post', 'Nadeln')] = 20

max_travel = 6000

import lummerland

model = lummerland.solve(places, goods, travel_distance, costs, capacities, availabilities, demands, max_travel)

if not isinstance(model, Model):
    print("solve-Funktion gibt kein Gurobi-Modell zurueck!")
