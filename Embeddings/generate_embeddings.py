from openai import OpenAI
import openai
import os
import json

openai.api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI()

with open("LeanAideAnalysis/Embeddings/unique_terms.json", 'r', encoding='utf-8') as infile, open("LeanAideAnalysis/Embeddings/embeddings.jsonl", 'w') as outfile:
    unique_terms = json.load(infile)
    i=1
    for term in unique_terms:
        print(i,term)
        i+=1
        response = client.embeddings.create(
            input=term,
            model="text-embedding-3-small",
            dimensions=256
        )
    
        json.dump({term: response.data[0].embedding}, outfile)
        outfile.write('\n')
