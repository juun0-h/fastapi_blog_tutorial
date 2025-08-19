from fastapi import APIRouter, Request, Depends, Form, status
from db.database import direct_get_conn, context_get_conn
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy import text, Connection
from sqlalchemy.exc import SQLAlchemyError
from schemas.blog_schema import Blog, BlogData
from services import blog_svc
from utils import utils

# Router 생성
router = APIRouter(prefix="/blogs", tags=["blogs"])

# Jinja2 Template engine 생성
templates = Jinja2Templates(directory="templates")

# router.get("/blogs") -> X: prefix로 이미 /blogs를 선언함
@router.get("/")
async def get_all_blogs(request: Request, 
                        conn: Connection = Depends(context_get_conn)):
        all_blogs = blog_svc.get_all_blogs(conn)

        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"all_blogs": all_blogs}
        )

@router.get("/show/{id}")
def get_blog_by_id(request: Request, id: int,
                   conn: Connection = Depends(context_get_conn)):

        blog = blog_svc.get_blog_by_id(id, conn)
        blog.content = utils.newline_to_br(blog.content)

        return templates.TemplateResponse(
            request=request,
            name="show_blog.html",
            context={"blog": blog}
        )
    

@router.get("/new")
def create_blog_ui(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="new_blog.html",
        context={}
    )


@router.post("/new")
def create_blog(request: Request,
                title: str = Form(min_length=2, max_length=200),
                author: str = Form(max_length=100),
                content: str = Form(min_length=2, max_length=4000),
                conn: Connection = Depends(context_get_conn)):
     
     blog_svc.create_blog(title=title, author=author, content=content, conn=conn)

     return RedirectResponse(url="/blogs", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/modify/{id}")
def update_blog_ui(request: Request, id: int, conn: Connection = Depends(context_get_conn)):

    blog = blog_svc.get_blog_by_id(id, conn)

    return templates.TemplateResponse(
        request=request,
        name="modify_blog.html",
        context={"blog": blog}
    )


@router.post("/modify/{id}")
def update_blog(request: Request, id:int,
                title: str = Form(min_length=2, max_length=200),
                author: str = Form(max_length=100),
                content: str = Form(min_length=2, max_length=4000),
                conn: Connection = Depends(context_get_conn)):
    
    blog_svc.update_blog(id=id, title=title, author=author, content=content, conn=conn)

    return RedirectResponse(url=f"/blogs/show/{id}", status_code=status.HTTP_303_SEE_OTHER)


@router.post("/delete/{id}")
def delete_blog(id: int, conn: Connection = Depends(context_get_conn)):
    
    blog_svc.delete_blog(id=id, conn=conn)
    
    return RedirectResponse(url="/blogs", status_code=status.HTTP_303_SEE_OTHER)