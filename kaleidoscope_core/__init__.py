"""
Kaleidoscope AI Core Package
===========================
Core functionality for the Kaleidoscope AI system.
"""

from .core import KaleidoscopeCore
from .quantum import QuantumSimulator
from .types import FileType

import atexit
import signal
import logging

logger = logging.getLogger(__name__)

def shutdown_handler():
    """Cleanup on shutdown"""
    logger.info("Shutting down Kaleidoscope AI...")
    # Add cleanup code here

# Register shutdown handler
atexit.register(shutdown_handler)
signal.signal(signal.SIGTERM, lambda signo, frame: shutdown_handler())

__version__ = '0.1.0'
__all__ = ['KaleidoscopeCore', 'QuantumSimulator', 'FileType']
from .core import KaleidoscopeCore
from .types import FileType
