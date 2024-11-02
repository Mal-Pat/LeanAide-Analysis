from openai import OpenAI
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI()

response = client.embeddings.create(
    input="unital homomorphisms",
    model="text-embedding-3-small"
)

print(response)
print(response.data[0].embedding)

with open("LeanAideAnalysis/Embeddings/embeddings.json", "w") as outfile:
    outfile.write(json.dumps(response, indent=4))
