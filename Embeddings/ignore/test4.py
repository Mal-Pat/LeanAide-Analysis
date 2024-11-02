import json

with open("LeanAideAnalysis/Embeddings/unique_terms.json", 'r', encoding='utf-8') as file:
    data = json.load(file)
    print(data[0])
    print(data[1])