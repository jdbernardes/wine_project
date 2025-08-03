from fastapi import FastAPI
from wine_project.routers import wines, root, dashboard

app = FastAPI()
app.include_router(wines.router)
app.include_router(dashboard.router)
app.include_router(root.router)
