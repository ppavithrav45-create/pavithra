from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from .routes import router

app = FastAPI(title="FitBuddy AI")

app.include_router(router)


@app.get("/", response_class=HTMLResponse)
def home():
    html_path = Path(__file__).parent.parent / "templates" / "index.html"
    return html_path.read_text(encoding="utf-8")