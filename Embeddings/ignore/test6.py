import os
import json

with open("LeanAideAnalysis/Embeddings/unique_terms.json", 'r', encoding='utf-8') as infile:
    i=34300
    unique_terms = json.load(infile)[i:]
    print(unique_terms[0])
    print(unique_terms[1])
    print(unique_terms[2])