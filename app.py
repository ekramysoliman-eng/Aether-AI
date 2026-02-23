import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai

app = FastAPI()

# تفعيل بروتوكول الأمان للسماح لـ GitHub بالوصول
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # هذا السطر هو مفتاح الحل
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        # تعليمات الشخصية المدمجة (هولمز وهاوس)
        system_instruction = "You are Human Ai, with the logic of Sherlock Holmes and the wit of Dr. House. Be professional and brief."
        response = model.generate_content(f"{system_instruction}\nUser: {request.message}")
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
