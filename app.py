import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

app = FastAPI()

# تفعيل الوصول الكامل لربط GitHub بالسيرفر
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(f"You are Human Ai, a Sherlock-style expert. Answer: {request.message}")
        return {"response": response.text}
    except Exception as e:
        return {"response": f"Brain Error: {str(e)}"}
