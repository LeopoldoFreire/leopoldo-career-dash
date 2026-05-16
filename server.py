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
        <head>
            <title>Leopoldo Career Dash</title>
            <style>
                body { font-family: sans-serif; background: #121212; color: white; padding: 20px; }
                .job-card { background: #1e1e1e; padding: 15px; margin: 10px 0; border-radius: 8px; }
            </style>
        </head>
        <body>
            <h1>🚀 Leopoldo Career Dash Online</h1>
            <div id="jobs">Carregando vagas...</div>
            <script>
                fetch('/api/vagas').then(r => r.json()).then(data => {
                    document.getElementById('jobs').innerHTML = data.map(v => 
                        `<div class='job-card'>${v.cargo} - <small>${v.fonte}</small></div>`
                    ).join('');
                });
            </script>
        </body>
    </html>
    """

@app.get("/api/vagas")
async def get_vagas():
    # Exemplo de chamada REST ao Supabase
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{SUPABASE_URL}/rest/v1/vagas?select=*",
            headers={"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}"}
        )
        return response.json()
