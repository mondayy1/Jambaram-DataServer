from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.combination import router as combination_router
from routes.champion import router as champion_router
app = FastAPI(docs_url='/api/model/docs', openapi_url='/api/model/openapi.json')

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the router from the predict module
app.include_router(champion_router)
app.include_router(combination_router)
