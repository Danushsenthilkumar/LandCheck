from fastapi import FastAPI
from pymongo import TEXT, GEOSPHERE
from app.utils.db import db  # db is already connected on import

# Routers
from app.routes.reel_routes import router as reel_router
from app.routes.property_routes import router as property_router
from app.routes.agent_routes import router as agent_router
from app.routes.booking_routes import router as booking_router
from app.routes.user_routes import router as user_router
from app.routes.onboarding_routes import router as onboarding_router

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # ✅ Indexes on 'properties' collection
    properties_collection = db["properties"]

    properties_collection.create_index([("city", TEXT), ("address", TEXT)])

    try:
        properties_collection.drop_index("location_2dsphere")
    except Exception as e:
        print("Index didn't exist:", e)

    properties_collection.create_index([("location", GEOSPHERE)])
    print("✅ Indexes created successfully.")

# ✅ Register routers
app.include_router(reel_router)
app.include_router(property_router)
app.include_router(agent_router)
app.include_router(booking_router)
app.include_router(user_router)
app.include_router(onboarding_router)

# ✅ Run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
