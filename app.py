from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import time

app = FastAPI(title="Mantle Sentinel AI Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/telemetry")
def get_telemetry():
    return {
        "status": "online",
        "current_block": random.randint(12450000, 12450050),
        "sequencer_latency_ms": round(random.uniform(200.0, 450.0), 2),
        "gas_price_gwei": round(random.uniform(0.05, 0.15), 4),
        "network_load_percent": random.randint(15, 45),
        "timestamp": int(time.time())
    }

@app.get("/api/alerts")
def get_alerts():
    return [
        {
            "id": 1,
            "timestamp": int(time.time()) - 300,
            "type": "Gas Spike Spammer",
            "severity": "MEDIUM",
            "status": "BLOCKED",
            "details": "Abnormal Gwei deviation detected from contract 0x3a...4f"
        },
        {
            "id": 2,
            "timestamp": int(time.time()) - 50,
            "type": "Flash Loan Outflow",
            "severity": "CRITICAL",
            "status": "MITIGATED",
            "details": "Large liquidity drain attempt isolated on Mantle Bridge wrapper"
        }
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
