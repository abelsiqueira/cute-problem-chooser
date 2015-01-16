#!/usr/bin/env python

import json
import os

data = json.load(open("../sif.json"))

# Removing .SIF from the problem name.
for problem in data.keys():
    if ".SIF" in problem:
        data[problem[0:-4]] = data.pop(problem)

# Needs improvement
# Conditions

for problem in data.keys():
    # If there is an objective group, ignore
    if sum(data[problem]["objective"].values()) > 0:
        continue
    # If there are inequality constraints, ignore
    con = data[problem]["constraint"]
    if sum([con[s] for s in con.keys() if " ineq" in s]) > 0:
        continue
    # If there aren't equality constraint, ignore
    if sum([con[s] for s in con.keys() if " eq" in s]) == 0:
        continue
    # If the number of free variables isn't the total number
    # of variables, then there are not free variables.
    var = data[problem]["variable"]
    if var["free"] != sum(var.values()):
        continue
    print(problem)
