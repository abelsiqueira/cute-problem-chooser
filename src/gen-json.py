#!/usr/bin/env python

import subprocess
import os
def get_problem_data(problem):
    out = subprocess.check_output(["sifdecoder", problem])
    out = out.decode('utf-8')
    # The information below was taken from file
    # $SIFDECODE/src/decode/sifdecode.f90
    # so it should be able to handle all cases
    data = {"objective":
                {"linear": 0,
                "nonlinear": 0},
            "variable":
                {"free": 0,
                "only from below": 0,
                "only from above": 0,
                "below and above": 0,
                "fixed": 0,
                "slack": 0},
            "constraint":
                {"linear equality": 0,
                "linear inequality": 0,
                "nonlinear equality": 0,
                "nonlinear inequality": 0} }

    for line in out.split('\n'):
        list_of_num = [int(s) for s in line.split() if s.isdigit()]
        if len(list_of_num) > 0:
            number = list_of_num[0]
        for key in data.keys():
            if " {}".format(key) in line:
                for subkey in data[key].keys():
                    if " {}".format(subkey) in line:
                        data[key][subkey] += number
    return data

try:
    sifdir = os.environ["MASTSIF"]
except:
    print("ERROR: $MASTSIF not found. Have you installed CUTEst?")

data = {}
for file in [d for d in os.listdir(sifdir) if d.endswith(".SIF")]:
    data[file] = get_problem_data(file)

print(json.dumps(data, sort_keys=True, separators=(',', ': '), indent=2))
