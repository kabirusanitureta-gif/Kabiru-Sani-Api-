from fastapi import FastAPI

app = FastAPI(
    title="Kabiru Engineering API",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "name": "Kabiru Engineering API",
        "status": "running"
    }

@app.get("/ohms-law")
def ohms_law(voltage: float, resistance: float):
    current = voltage / resistance
    return {
        "voltage": voltage,
        "resistance": resistance,
        "current": current
    }

@app.get("/arduino")
def arduino_help():
    return {
        "message": "Arduino and ESP32 support endpoint"
}
