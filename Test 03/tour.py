from gurobipy import quicksum, Model, GRB
from gurobipy import *


def solve(days, routes, length, visitors, min_rest_days, min_length, hard_routes):

    model = Model('tour')

    model.modelSense = GRB.MAXIMIZE

    assignment = {}
    # Achtung: day nimmt alle Werte von 0 bis days-1 an.
    for day in range(days):
        for route in routes:
            assignment[day, route] = model.addVar(
                name=f"assignment_{day}_{route}", vtype=GRB.BINARY, obj=visitors[route])

    model.update()

    # 1. Nebenbedingung(en):
    # Bedeutung: Jeder Tag höchstens eine Tour
    for day in range(days):
        model.addConstr(quicksum(assignment[day, route]
                                 for route in routes) <= 1)

    # 2. Nebenbedingung(en):
    # Bedeutung: Jede Route nur höchstens einmal
    for route in routes:
        model.addConstr(quicksum(assignment[day, route]
                                 for day in range(days)) <= 1)

    # 3. Nebenbedingung(en):
    # Bedeutung: Kein Ruhetag am ersten Tag
    model.addConstr(quicksum(assignment[0, route]
                             for route in routes) == 1)

    # 4. Nebenbedingung(en):
    # Bedeutung: 'Les Champs' am letzten Tag
    model.addConstr(assignment[days - 1, 'Les Champs'] == 1)

    # 5. Nebenbedingung(en):
    # Bedeutung: Schwere Route <-/-> Schwere Route
    for day in range(days - 1):
        model.addConstr(quicksum(assignment[day, hard_route] + assignment[day + 1, hard_route]
                                 for hard_route in hard_routes) <= 1)

    # 6. Nebenbedingung(en):
    # Bedeutung: Min-length
    model.addConstr(quicksum(assignment[day, route] * length[route]
                             for day in range(days) for route in routes) >= min_length)

    # 7. Nebenbedingung(en):
    # Bedeutung: Anzahl Ruhetage: # Ruhetage = days - # Tage gefahren
    model.addConstr(days - quicksum(assignment[day, route] for day in range(
        days) for route in routes) >= min_rest_days)

    # ...

    model.optimize()

    if model.status == GRB.OPTIMAL:
        print(f"\nObjective value: {model.ObjVal}\n")
        for day in range(days):
            assign = None
            for route in routes:
                if (assignment[day, route].x > 0.1):
                    assign = route
            if assign == None:
                print(f'Day {day+1} will be a rest day')
            else:
                print(f'Day {day+1} will include the route: {assign}')
    else:
        print(f"No solution was found. Status {model.status}")

    return model
