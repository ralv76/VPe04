from fastapi import FastAPI
from datetime import datetime
import uvicorn

app = FastAPI(title="Time Server API ver2dev", description="Простой API для получения текущего времени сервера")

@app.get("/")
async def root():
    """Корневой endpoint"""
    return {
        "message": "Time Server API", 
        "endpoints": {
            "time": ["/time", "/time/iso"],
            "date": ["/date", "/date/iso", "/date/formatted"]
        }
    }

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

@app.get("/date")
async def get_date():
    """Возвращает текущую дату сервера в формате YYYY-MM-DD"""
    current_date = datetime.now().strftime("%Y-%m-%d")
    return {
        "server_date": current_date,
        "timestamp": datetime.now().timestamp()
    }

@app.get("/date/iso")
async def get_date_iso():
    """Возвращает текущую дату сервера в ISO формате"""
    current_date = datetime.now().date().isoformat()
    return {
        "server_date": current_date,
        "timestamp": datetime.now().timestamp()
    }

@app.get("/date/formatted")
async def get_date_formatted():
    """Возвращает текущую дату сервера в читаемом формате"""
    current_date = datetime.now().strftime("%d.%m.%Y")
    current_date_en = datetime.now().strftime("%B %d, %Y")
    return {
        "server_date": current_date,
        "server_date_en": current_date_en,
        "timestamp": datetime.now().timestamp()
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

