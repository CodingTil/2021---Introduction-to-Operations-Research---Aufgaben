# -*- coding: utf-8 -*-

from gurobipy import *

# Erzeugt Liste von Speisen (als Strings) und die 
# Dictionaries kalorien, fett, kosten,
# die jeder Speise (als String) den entsprechenden
# Wert zuordnen.
speisen, kalorien, fett, kosten = multidict({
  "Apfel": [50, 0.4, 0.31],
  "Erdnussbutter": [627, 49.9, 0.82],
  "Milch": [42, 0.1, 0.06],
  "Brot": [188, 1.0, 0.49],
  "Birne": [55, 0.3, 0.25]
})

minKalorien = 2000
maxFett = 20
obst = ["Apfel", "Birne"]

# LP-Modelldatei einbinden.
import diet

# Dortige Loesungsfunktion aufrufen.
diet.solve(speisen, kalorien, fett, kosten, minKalorien, maxFett, obst)

