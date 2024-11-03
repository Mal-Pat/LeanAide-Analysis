import json
import numpy as np

keys=['a','b']
values=[[3,5],[7,6]]

with open("LeanAideAnalysis/Embeddings/ignore/test5.jsonl", 'a') as outfile:
    for i in range(len(keys)):
        json.dump({keys[i]:values[i]}, outfile)
        outfile.write('\n')