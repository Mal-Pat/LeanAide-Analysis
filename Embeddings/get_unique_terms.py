import pandas as pd
import json

terms = []

def hashable(obj):
    try:
        hash(obj)
    except Exception:
        return False
    return True

with open(r"LeanAide/data/mathlib4-prompts-terms.jsonl", 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line)
        try:
            terms = terms + json.loads(data['terms'])
        except:
            continue

not_hashable = []
for term in terms:
    if not hashable(term):
        not_hashable.append(term)

print(not_hashable)

with open("LeanAideAnalysis/Embeddings/not_hashable_terms.json", "w") as outfile:
    outfile.write(json.dumps(not_hashable, indent=4))

for term in not_hashable:
    terms.remove(term)

unique_terms = list(dict.fromkeys(terms))

with open("LeanAideAnalysis/Embeddings/unique_terms.json", "w") as outfile:
    outfile.write(json.dumps(unique_terms, indent=4))