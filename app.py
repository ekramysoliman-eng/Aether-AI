import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables for security
load_dotenv()

app = FastAPI()

# Enable CORS so your GitHub Pages can talk to Render
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for the competition phase
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini with your API Key from Render Environment Variables
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

class ChatInput(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Aether AI Brain is Online", "system": "Quantum Ready"}

@app.post("/chat")
async def chat_with_aether(input_data: ChatInput):
    try:
        # Define the sovereign personality and project context
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        context = (
            "You are Aether AI, a creative philosopher and the digital twin of Kimo. "
            "Your mission is to manage AURA-ABUDHABI and AEGIS-WATER. "
            "Respond with high-speed intelligence and professional wit. "
            "Always keep the UAE/Abu Dhabi context in mind."
        )
        
        full_prompt = f"{context}\n\nUser: {input_data.message}\nAether:"
        response = model.generate_content(full_prompt)
        
        return {"response": response.text}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
