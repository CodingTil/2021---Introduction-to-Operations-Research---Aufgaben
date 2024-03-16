from gurobipy import multidict
import tour

days = 6
routes, length, visitors = multidict({
    'Les Champs':[111,20000],
    'Nimes':[203, 50000],
    'Pau':[28, 44000],
    'Col du Tourmalet':[167, 39000],
    'Bergerac':[166, 5000],
    'Col de la Loze':[109, 23000],
    'Nice':[275, 51000],
    'Meribel':[18, 28000],
    'Planche des Belles Filles':[144, 27000],
    'Chauvigny':[175, 23000],
})

min_rest_days = 1

min_length = 930

hard_routes = ['Col du Tourmalet', 'Chauvigny']

tour.solve(days, routes, length, visitors, min_rest_days, min_length, hard_routes)
