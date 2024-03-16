from gurobipy import *

import bergwerk

mines, work_hours = multidict({
	'Dunkle-Mine': [300],
	'Lava-Mine': [250],
	'Bergmine': [410],
	'Ural-Mine': [500],
	'Altai-Mine': [700],
	'Ruhrmine': [1050],
})

ores, demand = multidict({
	'Eisen': [361],
	'Kohle': [590],
	'Redstone': [111],  # Easteregg gefunden!
	'Gold': [52],
	'Diamant': [29],
	'Wolfram': [128],
})

available = {
	('Dunkle-Mine', 'Eisen'): 278,
	('Dunkle-Mine', 'Kohle'): 340,
	('Dunkle-Mine', 'Redstone'): 56,
	('Dunkle-Mine', 'Gold'): 12,
	('Dunkle-Mine', 'Diamant'): 2,
	('Dunkle-Mine', 'Wolfram'): 68,

	('Lava-Mine', 'Eisen'): 284,
	('Lava-Mine', 'Kohle'): 53,
	('Lava-Mine', 'Redstone'): 34,
	('Lava-Mine', 'Gold'): 20,
	('Lava-Mine', 'Diamant'): 14.5,
	('Lava-Mine', 'Wolfram'): 32,

	('Bergmine', 'Eisen'): 30,
	('Bergmine', 'Kohle'): 120,
	('Bergmine', 'Redstone'): 79,
	('Bergmine', 'Gold'): 30,
	('Bergmine', 'Diamant'): 120,
	('Bergmine', 'Wolfram'): 79,

	('Ural-Mine', 'Eisen'): 300,
	('Ural-Mine', 'Kohle'): 170,
	('Ural-Mine', 'Redstone'): 36,
	('Ural-Mine', 'Gold'): 18,
	('Ural-Mine', 'Diamant'): 5,
	('Ural-Mine', 'Wolfram'): 22,

	('Altai-Mine', 'Eisen'): 67,
	('Altai-Mine', 'Kohle'): 23,
	('Altai-Mine', 'Redstone'): 55,
	('Altai-Mine', 'Gold'): 67,
	('Altai-Mine', 'Diamant'): 43,
	('Altai-Mine', 'Wolfram'): 19,

	('Ruhrmine', 'Eisen'): 99,
	('Ruhrmine', 'Kohle'): 199,
	('Ruhrmine', 'Redstone'): 39.5,
	('Ruhrmine', 'Gold'): 2.5,
	('Ruhrmine', 'Diamant'): 24,
	('Ruhrmine', 'Wolfram'): 26,
}

unit_costs = {
	('Dunkle-Mine', 'Eisen'): 40,
	('Dunkle-Mine', 'Kohle'): 32,
	('Dunkle-Mine', 'Redstone'): 33,
	('Dunkle-Mine', 'Gold'): 55,
	('Dunkle-Mine', 'Diamant'): 12,
	('Dunkle-Mine', 'Wolfram'): 89,

	('Lava-Mine', 'Eisen'): 34,
	('Lava-Mine', 'Kohle'): 67,
	('Lava-Mine', 'Redstone'): 31,
	('Lava-Mine', 'Gold'): 52.5,
	('Lava-Mine', 'Diamant'): 34,
	('Lava-Mine', 'Wolfram'): 77,

	('Bergmine', 'Eisen'): 45.6,
	('Bergmine', 'Kohle'): 33,
	('Bergmine', 'Redstone'): 67,
	('Bergmine', 'Gold'): 48,
	('Bergmine', 'Diamant'): 32,
	('Bergmine', 'Wolfram'): 72,

	('Ural-Mine', 'Eisen'): 47,
	('Ural-Mine', 'Kohle'): 44,
	('Ural-Mine', 'Redstone'): 12,
	('Ural-Mine', 'Gold'): 66,
	('Ural-Mine', 'Diamant'): 21.1,
	('Ural-Mine', 'Wolfram'): 56.9,

	('Altai-Mine', 'Eisen'): 47,
	('Altai-Mine', 'Kohle'): 42.42,
	('Altai-Mine', 'Redstone'): 22,
	('Altai-Mine', 'Gold'): 52,
	('Altai-Mine', 'Diamant'): 78,
	('Altai-Mine', 'Wolfram'): 39,

	('Ruhrmine', 'Eisen'): 56.65,
	('Ruhrmine', 'Kohle'): 39,
	('Ruhrmine', 'Redstone'): 23.4,
	('Ruhrmine', 'Gold'): 55,
	('Ruhrmine', 'Diamant'): 18,
	('Ruhrmine', 'Wolfram'): 66,
}

unit_time_needed = {
	('Dunkle-Mine', 'Eisen'): 0.64,
	('Dunkle-Mine', 'Kohle'): 1.3,
	('Dunkle-Mine', 'Redstone'): 0.2,
	('Dunkle-Mine', 'Gold'): 4,
	('Dunkle-Mine', 'Diamant'): 1.2,
	('Dunkle-Mine', 'Wolfram'): 2,

	('Lava-Mine', 'Eisen'): 0.47,
	('Lava-Mine', 'Kohle'): 1.5,
	('Lava-Mine', 'Redstone'): 1.34,
	('Lava-Mine', 'Gold'): 3.99,
	('Lava-Mine', 'Diamant'): 0.8,
	('Lava-Mine', 'Wolfram'): 1.11,

	('Bergmine', 'Eisen'): 1.2,
	('Bergmine', 'Kohle'): 2,
	('Bergmine', 'Redstone'): 0.9,
	('Bergmine', 'Gold'): 3.5,
	('Bergmine', 'Diamant'): 0.556,
	('Bergmine', 'Wolfram'): 1.28,

	('Ural-Mine', 'Eisen'): 2.2,
	('Ural-Mine', 'Kohle'): 1,
	('Ural-Mine', 'Redstone'): 2.4,
	('Ural-Mine', 'Gold'): 4.7,
	('Ural-Mine', 'Diamant'): 0.9,
	('Ural-Mine', 'Wolfram'): 0.99,

	('Altai-Mine', 'Eisen'): 1.7,
	('Altai-Mine', 'Kohle'): 1.56,
	('Altai-Mine', 'Redstone'): 0.95,
	('Altai-Mine', 'Gold'): 4.2,
	('Altai-Mine', 'Diamant'): 1.3,
	('Altai-Mine', 'Wolfram'): 1.45,

	('Ruhrmine', 'Eisen'): 0.51,
	('Ruhrmine', 'Kohle'): 3.1,
	('Ruhrmine', 'Redstone'): 0.899,
	('Ruhrmine', 'Gold'): 3.56,
	('Ruhrmine', 'Diamant'): 0.8,
	('Ruhrmine', 'Wolfram'): 1.86,
}

subsidised_ores = ['Redstone', 'Wolfram']

bergwerk.solve(mines, ores, available, unit_costs, unit_time_needed, work_hours, subsidised_ores, demand)
