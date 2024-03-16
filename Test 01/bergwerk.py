#!/usr/bin/python

from gurobipy import *


def solve(mines, ores, available, unit_costs, unit_time_needed, work_hours, subsidised_ores, demand):

	model = Model('bergwerk')

	x = {}
	for m in mines:
		for o in ores:
			x[m, o] = model.addVar(obj=unit_costs[m, o], name=f'x_{m}_{o}')

	model.modelSense = GRB.MINIMIZE

	model.update()

	# 1. Nebenbedingung:
	# Bedeutung: Demand treffen
	# Ungleichung:
	for o in ores:
		model.addConstr(quicksum(x[m, o] for m in mines) >= demand[o])

	# 2. Nebenbedingung:
	# Bedeutung: Nicht mehr als available
	# Ungleichung:
	for m in mines:
		for o in ores:
			model.addConstr(x[m, o] <= available[m, o])

	# 3. Nebenbedingung:
	# Bedeutung: 2/3 Arbeitszeit
	# Ungleichung:
	for m in mines:
		model.addConstr(quicksum(x[m, o] * unit_time_needed[m, o] for o in ores) <= 2.0 / 3.0 * work_hours[m])

	# 4. Nebenbedingung:
	# Bedeutung: Subventionen
	# Ungleichung:
	for m in mines:
		model.addConstr(quicksum(x[m, o] for o in ores) / 4.0 <= quicksum(x[m, so] for so in subsidised_ores))

	# optimize
	model.optimize()

	# Ausgabe der Loesung.
	if model.status == GRB.OPTIMAL:
		print('\nOptimaler Zielfunktionswert: %g\n' % model.ObjVal)
		for m in mines:
			for o in ores:
				print(f"Mine {m} baut {str(x[m,o].x)} Einheiten {o} ab")
			print("")
	else:
		print('Keine Optimalloesung gefunden. Status: %i' % (model.status))
	return model
