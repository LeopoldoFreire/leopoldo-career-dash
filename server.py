from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import httpx
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

@app.get("/", response_class=HTMLResponse)
async def read_root():
return """
<html>
<body>
<h1>Leopoldo Career Dash está online!</h1>
</body>
</html>
"""

@app.get("/api/vagas")
async def get_vagas():
async with httpx.AsyncClient() as client:
esponse = await client.get(
f"{SUPABASE_URL}/rest/v1/vagas?select=*",
headers={"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}
)
return response.json()
