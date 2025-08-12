from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    """Simple health endpoint used in CI and later deploy/monitor sessions."""
    return {"status": "not ok", "version": "0.1.0"}
