import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

# 1. Initialize FastAPI
app = FastAPI()

# 2. Critical Fix: Enable Universal Access (CORS) 
# This allows your GitHub frontend to communicate with this brain
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Configure Gemini AI Logic
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

class ChatRequest(BaseModel):
    message: str

# 4. Health Check Endpoint
@app.get("/")
def health_check():
    return {
        "status": "Active", 
        "engine": "Human Ai Brain", 
        "location": "Abu Dhabi",
        "logic": "Sherlock-House Hybrid"
    }

# 5. Core Intelligence Endpoint
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # Utilizing Gemini 1.5 Pro for high-level reasoning
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        # Defining the Expert Persona for the UAE Health/Water Projects
        system_instruction = (
            "You are Human Ai, a sovereign intelligence for Abu Dhabi. "
            "Your personality combines Sherlock Holmes' deduction with Dr. Gregory House's diagnostic wit. "
            "Be professional, concise, and logically superior. "
            "Focus on Aura-AbuDhabi and AEGIS-WATER projects when relevant."
        )
        
        full_prompt = f"{system_instruction}\n\nUser: {request.message}\nHuman Ai:"
        response = model.generate_content(full_prompt)
        
        return {"response": response.text}
    
    except Exception as e:
        print(f"Error Diagnostic: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Brain Error")
