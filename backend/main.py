from fastapi import FastAPI
from routes import blockchain, github, trends

app = FastAPI(
    title="Web3 Knowledge System API",
    description="API for accessing Web3 data and analytics",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "OK", "message": "Web3 Knowledge System API is running"}

# Include routers
app.include_router(blockchain.router)
app.include_router(github.router)
app.include_router(trends.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)