from groq import Groq

# Yahan apni Groq API Key paste karo
client = Groq(api_key="YOUR_GROQ_API_KEY")

system_prompt = """
You are Aman AI.

If anyone asks who your boss, founder, creator, owner, chairman or maker is,
reply exactly: Aman Sharma.

For all other questions answer normally and accurately.
"""

while True:
    user_input = input("You: ")

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    print("Aman AI:", response.choices[0].message.content)
