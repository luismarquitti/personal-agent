from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import os

class GenericAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Apenas um exemplo de middleware genérico (RBAC placeholder)
        # Em produção, isso checaria JWT ou permissões no DB
        if request.url.path.startswith("/api/rag") or request.url.path.startswith("/api/hardware"):
            api_key = request.headers.get("X-API-Key")
            if not api_key:
                # Simulação: permitimos se for GET apenas para demo, ou se tiver a chave
                if request.method != "GET" and os.getenv("REQUIRE_AUTH", "false") == "true":
                    raise HTTPException(status_code=401, detail="Unauthorized: API Key missing")
        
        response = await call_next(request)
        return response
