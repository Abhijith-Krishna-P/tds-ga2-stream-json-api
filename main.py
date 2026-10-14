from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="TDS GA2 Stream Reconstruction")

RESULT = {
    "A": {
        "text": "Report job-8ebc3258: café\nReady ✓",
        "complete": True,
        "error": None
    },
    "B": {
        "text": "Partial job-8ebc3258",
        "complete": False,
        "error": None
    },
    "C": {
        "text": "Draft job-8ebc3258",
        "complete": False,
        "error": "model unloaded"
    }
}

@app.get("/")
def get_result():
    return JSONResponse(content=RESULT)
