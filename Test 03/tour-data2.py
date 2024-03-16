from gurobipy import multidict
import tour

days = 12
routes, length, visitors = multidict({
    'Les Champs':[111,20000],
    'Nimes':[283, 50000],
    'Pau':[28, 100000],
    'Col du Tourmalet':[167, 39000],
    'Bergerac':[166, 5000],
    'Col de la Loze':[109, 23000],
    'Nice':[275, 51000],
    'Meribel':[18, 28000],
    'Planche des Belles Filles':[144, 27000],
    'Chauvigny':[175, 23000],
    'Lyon':[67,95000],
    'Bordeaux':[234,33000],
    'Grenoble':[123,42345],
    'Bielefeld':[45,77001], # und ich dachte, die Stadt gibt's gar nicht ...
})

min_rest_days = 2

min_length = 1600

hard_routes = ['Col du Tourmalet', 'Les Champs', 'Planche des Belles Filles', 'Nimes', 'Pau']

tour.solve(days, routes, length, visitors, min_rest_days, min_length, hard_routes)