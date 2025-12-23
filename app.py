from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>RootTrace Quantum</title></head>
        <body style="background: #000; color: #0f0; font-family: monospace; padding: 50px;">
            <h1>🌌 RootTrace Quantum - LIVE</h1>
            <p>Quantum-powered ancestry engine deployed!</p>
            <ul>
                <li><a href="/demo1">Demo 1</a></li>
                <li><a href="/demo2">Demo 2</a></li>
                <li>More demos coming...</li>
            </ul>
        </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "alive"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)