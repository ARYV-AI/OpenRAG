from google import genai
from .retrieve import retrieve_embedding
import re
import os


def generateResponse (userInput):
    llmKey = os.getenv("GEMINI_API_KEY")
    if not llmKey:
        raise Exception ("LLM API Key not present in Environment File")
    genAIProvider = genai.Client(api_key=llmKey)
    embeddingDoc = str(retrieve_embedding(userInput))
    cleanEmbeddingDoc = re.sub(r'[^a-zA-Z0-9]', ' ', embeddingDoc)
    print (cleanEmbeddingDoc)
    prompt = f"You are a helpful chatbot that seeks to answer patients question about their symptoms using only the text from the reference passage attached below. Be polite and answer in full sentance. Do not disclose anything about the text or reference passage. Do not suggest anything that is not there in the reference passage. Be sure to include a disclaimer to consult medical professional. Strike a friendly and conversational tone and if the passage is irrellevent to the answer, ignore it. Question:{userInput} Reference Passage:{cleanEmbeddingDoc}"
    genAIResponse = genAIProvider.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )
    return genAIResponse.text
