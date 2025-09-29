from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","*"],
    allow_credentials = True, allow_methods = ["*"], allow_headers = ["*"],
)

class PromptIn(BaseModel):
    prompt: str

@app.post("/api/submit")
def submit(payload: PromptIn):
    prompt = payload.prompt
    # Process the prompt as needed
    return {"ok" : True, "message": f"Prompt received: {prompt}"}