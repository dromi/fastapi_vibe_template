from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.routers import router as api_router
# from app.core.exceptions import register_exception_handlers  # Uncomment if you have custom handlers
# from app.middleware import some_middleware  # Import and add as needed

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# CORS middleware (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(api_router)

# Register custom exception handlers (uncomment if implemented)
# register_exception_handlers(app)

# Register custom middleware (add as needed)
# app.add_middleware(some_middleware)

# Startup event handler
@app.on_event("startup")
async def on_startup():
    # Place startup logic here (e.g., connect to services, initialize resources)
    pass

# Shutdown event handler
@app.on_event("shutdown")
async def on_shutdown():
    # Place shutdown logic here (e.g., cleanup resources)
    pass
