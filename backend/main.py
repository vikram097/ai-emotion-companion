from fastapi import FastAPI

app = FastAPI(title="AI Emotion Companion - Backend")


@app.get("/")
async def root():
    return {"status": "ok"}


# If there are routers under `app.api`, try to include them (no-op if missing)
try:
    from app.api import router as api_router
    app.include_router(api_router, prefix="/api")
except Exception:
    pass
