from fastapi import FastAPI
from datetime import datetime
import uvicorn

app = FastAPI(title="Time Server API", description="Простой API для получения текущего времени сервера")

@app.get("/")
async def root():
    """Корневой endpoint"""
    return {"message": "Time Server API", "endpoints": ["/time", "/time/iso"]}

@app.get("/time")
async def get_time():
    """Возвращает текущее время сервера в формате YYYY-MM-DD HH:MM:SS"""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "server_time": current_time,
        "timestamp": datetime.now().timestamp()
    }

@app.get("/time/iso")
async def get_time_iso():
    """Возвращает текущее время сервера в ISO формате"""
    current_time = datetime.now().isoformat()
    return {
        "server_time": current_time,
        "timestamp": datetime.now().timestamp()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

