from fastapi import FastAPI
from contextlib import asynccontextmanager
import redis_endpoints as rf

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = rf.redis_instance
    app.state.redis = client
    try:
        yield
    finally:
        # Disconnect the client and its pool
        await client.aclose()

app = FastAPI(lifespan=lifespan)

app.include_router(router=rf.router)

@app.get("/health-check")
def health_check():
    return "Great!"



