from fastapi import FastAPI
app = FastAPI(
    title = "AI Reflection & Guidance Platform" , 
    description="Backend API for the AI Reflection & Guidance Platform",
    version = "1.0.0"
)

@app.get("/")
def root():
    return {
        "message" : "Welcome to the AI Reflection & guidance Platform API!"
    }