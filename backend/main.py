""" Server Ignition"""
import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run(app.app, host="localhost", port=8000, log_level="info")
