import json
import numpy as np

keys=['a','b','c']
values=[[3,5],[7,6],[2,4]]

with open("LeanAideAnalysis/Embeddings/embeddings.jsonl", 'w') as outfile:
    for i in range(len(keys)):
        json.dump({keys[i]:values[i]}, outfile)
        outfile.write('\n')