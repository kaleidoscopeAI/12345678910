from fastapi import FastAPI
from .routes import router
import logging
import uvicorn
from typing import Any

logger = logging.getLogger(__name__)

def create_app(core=None) -> FastAPI:
    """Create FastAPI application"""
    app = FastAPI(
        title="Kaleidoscope AI API",
        description="Quantum-Classical Hybrid AI System",
        version="0.1.0"
    )
    
    app.state.core = core
    app.include_router(router)
    
    return app

def start_api_server(config: dict, core: Any):
    """Start API server"""
    try:
        app = create_app(core)
        logger.info(f"Starting API server on {config['host']}:{config['port']}")
        uvicorn.run(
            app,
            host=config["host"],
            port=config["port"],
            log_level="info",
            access_log=True,
            workers=config.get("workers", 1)
        )
    except Exception as e:
        logger.error(f"Failed to start API server: {e}")
        raise
