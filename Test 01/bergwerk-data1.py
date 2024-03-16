from gurobipy import *

import bergwerk

mines, work_hours = multidict({
	'Dunkle-Mine': [30],
	'Lava-Mine': [25],
	'Bergmine': [12],
})

ores, demand = multidict({
	'Eisen': [110],
	'Kohle': [220],
	'Redstone': [77],  # Easteregg gefunden!
})

available = {
	('Dunkle-Mine', 'Eisen'): 44,
	('Dunkle-Mine', 'Kohle'): 200,
	('Dunkle-Mine', 'Redstone'): 90,
	('Lava-Mine', 'Eisen'): 90,
	('Lava-Mine', 'Kohle'): 5,
	('Lava-Mine', 'Redstone'): 33,
	('Bergmine', 'Eisen'): 30,
	('Bergmine', 'Kohle'): 120,
	('Bergmine', 'Redstone'): 79,
}

unit_costs = {
	('Dunkle-Mine', 'Eisen'): 50,
	('Dunkle-Mine', 'Kohle'): 33,
	('Dunkle-Mine', 'Redstone'): 90,
	('Lava-Mine', 'Eisen'): 45,
	('Lava-Mine', 'Kohle'): 41,
	('Lava-Mine', 'Redstone'): 65,
	('Bergmine', 'Eisen'): 47,
	('Bergmine', 'Kohle'): 39,
	('Bergmine', 'Redstone'): 61,
}

unit_time_needed = {
	('Dunkle-Mine', 'Eisen'): 0.3,
	('Dunkle-Mine', 'Kohle'): 0.05,
	('Dunkle-Mine', 'Redstone'): 0.12,
	('Lava-Mine', 'Eisen'): 0.1,
	('Lava-Mine', 'Kohle'): 0.07,
	('Lava-Mine', 'Redstone'): 0.19,
	('Bergmine', 'Eisen'): 0.2,
	('Bergmine', 'Kohle'): 0.01,
	('Bergmine', 'Redstone'): 0.08,
}

subsidised_ores = ['Redstone']

bergwerk.solve(mines, ores, available, unit_costs, unit_time_needed, work_hours, subsidised_ores, demand)
