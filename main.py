from fastapi import FastAPI
from routes.students import router as student_router
from routes.analytics import router as analytics_router

app = FastAPI()

app.include_router(student_router)
app.include_router(analytics_router)

@app.get("/")
def home():
    return {"message": "Welcome to this Student Analytics API project"}
