from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI(title="Hackathon API", description="API for certificate verification")

# Enable CORS for your React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://hackathon-verifier.vercel.app", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data - in real app, this would be your certificate-data.json
SAMPLE_CERTIFICATES = {
    "cert_001": {
        "name": "John Doe",
        "email": "john@student.edu",
        "project": "Blockchain Voting System",
        "award": "First Place",
        "date": "2024-03-15"
    },
    "cert_002": {
        "name": "Jane Smith", 
        "email": "jane@student.edu",
        "project": "DeFi Lending Platform",
        "award": "Best Innovation",
        "date": "2024-03-15"
    }
}

class VerificationRequest(BaseModel):
    certificate_id: str

@app.get("/")
async def root():
    return {"message": "Hackathon Certificate API is running!"}

@app.post("/verify")
async def verify_certificate(request: VerificationRequest):
    certificate_id = request.certificate_id
    
    if certificate_id in SAMPLE_CERTIFICATES:
        return {
            "verified": True,
            "certificate_data": SAMPLE_CERTIFICATES[certificate_id]
        }
    else:
        return {
            "verified": False,
            "message": "Certificate not found"
        }

@app.get("/certificates")
async def get_all_certificates():
    return SAMPLE_CERTIFICATES

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)