from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from routers import peptide_prices

app = FastAPI()

app.include_router(peptide_prices.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return HTMLResponse(content="<h1>Welcome to the Peptide Prices API</h1>")