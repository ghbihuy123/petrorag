from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chat_svc.routes import chat

# Initialize FastAPI app
app = FastAPI(
    title="ChatPetro API",
    description="Chatbot API for searching object type codes",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "ChatPetro API",
        "docs": "/docs",
        "health": "/api/chat/health"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}