from fastapi import Header, HTTPException

async def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        # For now, allow guests in dev mode
        return "guest"

    # In production, check against DB or env
    if x_api_key == "striker-secret-key":
        return "admin"

    raise HTTPException(status_code=403, detail="Invalid API Key")
