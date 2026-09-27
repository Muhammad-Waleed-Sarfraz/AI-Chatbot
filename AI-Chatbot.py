from google import genai
client = genai.Client(api_key = "Add Your API Here")
while True:
    user_text = input("You : ")
    response = client.models.generate_content(model = 'gemini-3.8-flash', contents=user_text)
    if (user_text.lower() == "quit"):
        print("-----Good Bye-----")
        break
print(response.text)
    
