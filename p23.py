import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print("name : Krishna | Roll No. : 1323215")
if not api_key:
    raise ValueError("GEMINI_API_KEY is missing in the .env file.")
genai.configure(api_key=api_key)
PERSONAL_SUMMARY_PROMPT = """
You are a personalized text-summarizer.
Summarize the given text with the following rules:
1. Output must be factual and concise.
2. Remove repetitive, irrelevant, or emotional filler.
3. Preserve important technical details, data, and definitions.
4. Maintain a professional tone.
5. Format the output using short paragraphs or bullet points.
6. Do not add assumptions or opinions.
Text to summarize:
{input_text}
Generate the best possible summary.
"""
model = genai.GenerativeModel("gemini-2.5-flash")
def summarize_text(text):
    prompt = PERSONAL_SUMMARY_PROMPT.format(input_text=text)
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred during summarization: {e}"
input_text = """
Artificial Intelligence is transforming industries by automating tasks,
enhancing decision-making, and increasing operational efficiency.
However, concerns such as job displacement, ethical risks, and privacy
issues are rising as AI adoption grows.
"""
print(summarize_text(input_text))
