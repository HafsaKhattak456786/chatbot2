import google.generativeai as genai

# Replace with your API key
API_KEY = "AIzaSyDuNIfU4ITO_R0yZP96zdeibZvFkP9aExQ"

genai.configure(api_key=API_KEY)

print("Available Gemini models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"  - {model.name}")