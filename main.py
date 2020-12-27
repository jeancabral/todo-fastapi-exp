import uvicorn
from app.main import build_api

app = build_api()

if __name__ == '__main__':
    uvicorn.run(app, port=5000, log_level="info")
