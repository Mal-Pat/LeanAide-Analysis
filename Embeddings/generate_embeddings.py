from openai import OpenAI
import openai
import os
import json

# openai.api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI()

with open("LeanAideAnalysis/Embeddings/unique_terms.json", 'r', encoding='utf-8') as infile, open("LeanAideAnalysis/Embeddings/embeddings32001-34794.jsonl", 'a') as outfile:
    i=34300
    unique_terms = json.load(infile)[i:]
    for term in unique_terms:
        response = client.embeddings.create(
            input=term,
            model="text-embedding-3-small",
            dimensions=256
        )
    
        json.dump({term: response.data[0].embedding}, outfile)
        outfile.write('\n')
