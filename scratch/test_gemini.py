import os 
from google import genai

client = genai.Client()
MODEL = os.environ.get("LLM_MODEL", "gemini-3.5-flash-lite")

response = client.models.generate_content(
    model = MODEL,
    contents = "10000 + 100000000 = ?"
)

print(response.text)