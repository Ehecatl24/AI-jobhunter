from fastapi import FastAPI

app = FastAPI(
    title="AI-jobhunter",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {
        "status": "running",
        "project": "AI-jobhunter",
        "version": "0.1.0"
    }