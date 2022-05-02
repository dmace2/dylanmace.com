from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html = True), name="static")


@app.get("/")
async def read_root():
    # return RedirectResponse(url="/static/index.html")
    return FileResponse("static/index.html")

@app.get("/projects")
async def read_projects():
    # return RedirectResponse(url="/static/projects.html")
    return FileResponse("static/projects.html")

@app.get("/projects/distalradius")
async def read_dr():
    return FileResponse("static/DistalRadiusDesign.pdf")

@app.get("/resume")
async def read_resume():
    return FileResponse("static/resume.pdf")

# @app.get("/assets/css/main.css")
# async def get_style():
#     return FileResponse("static/assets/css/main.css")


# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
