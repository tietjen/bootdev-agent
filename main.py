import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# response = client.models.generate_content(
#     model='gemini-2.0-flash-001', contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
# )
# print(response.text)
# print("Prompt tokens:", response.usage_metadata.prompt_token_count)
# print("Response tokens:", response.usage_metadata.candidates_token_count)

if len(sys.argv) > 1:
    prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages,
        )
    print(response.text)
    
    if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
        
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
else:
    print("No prompt provided")
    sys.exit(1)