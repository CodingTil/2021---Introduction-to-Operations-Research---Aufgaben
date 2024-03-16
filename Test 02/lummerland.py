# coding=utf-8

from gurobipy import *

# Maximalkostenflussproblem?


def solve(places, goods, travel_distance, costs, capacities, availabilities, demands, max_travel):
    model = Model("lummerland")

    # Ziel (Minimieren oder Maximieren?)
    model.modelSense = GRB.MINIMIZE

    # Variablen erzeugen.
    x = {}
    for g in goods:
        for p in places:
            for q in places:
                x[g, p, q] = model.addVar(
                    name="x_" + g + "_" + p + "_" + q, obj=(costs[g] * travel_distance[p, q]), lb=0)

    # Variablen dem Modell bekannt machen.
    model.update()

    # Erste Nebenbedingung:
    # Bedeutung: Maximale Fahrstrecke
    # Ungleichung: ...
    model.addConstr(quicksum(x[g, p, q] * travel_distance[p, q]
                    for g in goods for p in places for q in places) <= max_travel)

    # Zweite Nebenbedingung (falls noetig):
    # Bedeutung: Kapazität
    # Ungleichung: ...
    for p in places:
        for q in places:
            model.addConstr(quicksum(x[g, p, q]
                            for g in goods) <= capacities[p, q])

    # Dritte Nebenbedingung (falls noetig):
    # Bedeutung: Availabilities
    # Ungleichung: ...
    for g in goods:
        for p in places:
            model.addConstr(quicksum(x[g, p, q]
                            for q in places) <= availabilities[p, g])

    # Vierte Nebenbedingung (falls noetig):
    # Bedeutung: Demands
    # Ungleichung: ...
    for g in goods:
        for q in places:
            model.addConstr(quicksum(x[g, p, q]
                            for p in places) >= demands[q, g])

    # Fuenfte Nebenbedingung (falls noetig):
    # Bedeutung: ...
    # Ungleichung: ...

    # Nebenbedingungen hinzugefuegt? LP loesen lassen!
    model.optimize()

    # Transportmengen ausgeben.
    if model.status == GRB.OPTIMAL:
        print('\nOptimalloesung hat Kosten von %g.\n' % (model.ObjVal))
        for k in goods:
            for s1 in places:
                for s2 in places:
                    if x[k, s1, s2].x > 0.0001:
                        print('Von %s nach %s werden %g Chargen von %s transportiert.' % (
                            s1, s2, x[k, s1, s2].x, k))
    else:
        print('Keine Optimalloesung gefunden. Status: %i' % (model.status))

    return model
