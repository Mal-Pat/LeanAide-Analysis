import json

terms=[]

with open("LeanAideAnalysis/Embeddings/embeddings.jsonl", 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line)
        terms.append(data.keys())

print(terms)
