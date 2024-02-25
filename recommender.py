from openai import OpenAI 
import os 
os.environ["OPENAI_API_KEY"] = "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" 
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def recommend_similar_songs(input_text):
    prompt = f"Given the input: \"{input_text}\", recommend 5 songs that are similar."

    response = client.chat.completions.create(
        messages=[ 
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}"} 
        ], 
        temperature=0, 
        model="gpt-3.5-turbo"
    )
        
    recommended_songs = response.choices[0].message.content.split("\n")[1:]
    return recommended_songs

input_text = input("Enter your input text: ")
recommended_songs = recommend_similar_songs(input_text)
print("5 similar songs are:", recommended_songs)
