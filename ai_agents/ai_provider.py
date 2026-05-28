
import os

# =========================
# GEMINI SUPPORT
# =========================
def ask_gemini(prompt):

    import google.generativeai as genai

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return None

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)

    return response.text


# =========================
# GROQ SUPPORT
# =========================
def ask_groq(prompt):

    from groq import Groq

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        return None

    client = Groq(api_key=api_key)

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama3-8b-8192"
    )

    return completion.choices[0].message.content


# =========================
# AI ROUTER
# =========================
def ask_ai(prompt):

    gemini_key = os.getenv("GEMINI_API_KEY")

    if gemini_key:
        print("🤖 Using Gemini AI")
        return ask_gemini(prompt)

    groq_key = os.getenv("GROQ_API_KEY")

    if groq_key:
        print("⚡ Using Groq AI")
        return ask_groq(prompt)

    raise Exception(
        "❌ No GEMINI_API_KEY or GROQ_API_KEY found."
    )

