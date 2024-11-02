import json

terms = []
with open("LeanAideAnalysis/Embeddings/test.json", 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line)
        try:
            terms = terms + json.loads(data['terms'])
        except:
            continue

print(terms)

def hashable(obj):
    try:
        hash(obj)
    except Exception:
        return False
    return True

not_hashable = []
for term in terms:
    if not hashable(term):
        not_hashable.append(term)

print(not_hashable)

for term in not_hashable:
    terms.remove(term)

print(terms)