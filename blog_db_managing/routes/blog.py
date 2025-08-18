from fastapi import APIRouter, Request, Depends, Form, status
from db.database import direct_get_conn, context_get_conn
from fastapi.exceptions import HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy import text, Connection
from sqlalchemy.exc import SQLAlchemyError
from schemas.blog_schema import Blog, BlogData
from utils import utils

# Router 생성
router = APIRouter(prefix="/blogs", tags=["blogs"])

# Jinja2 Template engine 생성
templates = Jinja2Templates(directory="templates")

# router.get("/blogs") -> X: prefix로 이미 /blogs를 선언함
@router.get("/")
async def get_all_blogs(request: Request):
    conn = None
    try:
        conn = direct_get_conn()
        query = """
                SELECT id, title, author, content, image_loc, modified_dt FROM blog_db.blog
                """
        result = conn.execute(text(query))
        # rows = result.fetchall()
        rows = [BlogData(id=row.id,
                     title=row.title,
                     author=row.author,
                     content=utils.truncate_text(row.content),
                     image_loc=row.image_loc,
                     modified_dt=row.modified_dt) for row in result]
        result.close()
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={"all_blogs": rows}
        )
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Requested service is unavailable due to internal server error")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="An unexpected error occurred")
    finally:
        if conn:
            conn.close()


@router.get("/show/{id}")
def get_blog_by_id(request: Request,
                         id: int,
                         conn: Connection = Depends(context_get_conn)):
    try:
        query = f"""
            SELECT id, title, author, content, image_loc, modified_dt FROM blog_db.blog
            WHERE id = :id
        """
        stmt = text(query)
        bind_stmt = stmt.bindparams(id = id)
        result = conn.execute(bind_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with id {id} not found")
        
        row = result.fetchone()

        blog = BlogData(id=row.id, 
                        title=row.title, 
                        author=row.author, 
                        content=utils.newline_to_br(row.content), 
                        image_loc=row.image_loc, 
                        modified_dt=row.modified_dt)
        result.close()
        return templates.TemplateResponse(
            request=request,
            name="show_blog.html",
            context={"blog": blog}
        )
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Requested service is unavailable due to internal server error")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="An unexpected error occurred")
    

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
    try:
        query = f"""
            INSERT INTO blog_db.blog (title, author, content, modified_dt)
            VALUES ('{title}', '{author}', '{content}', now())
        """
        conn.execute(text(query))
        conn.commit()
        return RedirectResponse(url="/blogs", status_code=status.HTTP_303_SEE_OTHER)
    except SQLAlchemyError as e:
        print(e)
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Failed to create blog due to bad request")


@router.get("/modify/{id}")
def update_blog_ui(request: Request, id: int, conn: Connection = Depends(context_get_conn)):
    try:
        query = f"""
        select id, title, author, content from blog where id = :id
        """
        stmt = text(query)
        bind_stmt = stmt.bindparams(id=id)
        result = conn.execute(bind_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with id {id} not found")
        row = result.fetchone()
       
        return templates.TemplateResponse(
            request=request,
            name="modify_blog.html",
            context={"id": row.id, "title": row.title, "author": row.author, "content": row.content}
        )
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Failed to update blog due to bad request")
    
@router.post("/modify/{id}")
def update_blog(request: Request, id:int,
                title: str = Form(min_length=2, max_length=200),
                author: str = Form(max_length=100),
                content: str = Form(min_length=2, max_length=4000),
                conn: Connection = Depends(context_get_conn)):
    try:
        query = f"""
            UPDATE blog_db.blog
            SET title = :title, author = :author, content = :content, modified_dt = now()
            WHERE id = :id
        """
        bind_stmt = text(query).bindparams(id=id, title=title, author=author, content=content)
        result = conn.execute(bind_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with id {id} not found")
        conn.commit()
        return RedirectResponse(url=f"/blogs/show/{id}", status_code=status.HTTP_303_SEE_OTHER)
    except SQLAlchemyError as e:
        print(e)
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Failed to update blog due to bad request")


@router.post("/delete/{id}")
def delete_blog(id: int, conn: Connection = Depends(context_get_conn)):
    try:
        query = f"""
            DELETE FROM blog_db.blog
            WHERE id = :id
        """
        bind_stmt = text(query).bindparams(id=id)
        result = conn.execute(bind_stmt)
        if result.rowcount == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with id {id} not found")
        conn.commit()
        return RedirectResponse(url="/blogs", status_code=status.HTTP_303_SEE_OTHER)
    except SQLAlchemyError as e:
        print(e)
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Requested service is unavailable due to internal server error")