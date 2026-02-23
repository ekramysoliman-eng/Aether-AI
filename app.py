import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

app = FastAPI()

# 1. THE CURE: Universal Access Control
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Configure Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def health_check():
    return {"status": "Active", "engine": "Human Ai Brain"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        # Persona: Sherlock-House Hybrid
        system_instruction = "You are Human Ai for Abu Dhabi projects. Be logical, witty, and concise."
        response = model.generate_content(f"{system_instruction}\nUser: {request.message}")
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
