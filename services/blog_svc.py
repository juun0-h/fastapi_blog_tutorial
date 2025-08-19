from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy import text, Connection
from sqlalchemy.exc import SQLAlchemyError
from schemas.blog_schema import BlogData
from utils import utils


def get_all_blogs(conn: Connection) -> list[BlogData]:
    try:
        query = """
        SELECT id, title, author, content, image_loc, modified_dt FROM blog;
        """
        result = conn.execute(text(query))
        all_blogs = [BlogData(id=row.id,
              title=row.title,
              author=row.author,
              content=utils.truncate_text(row.content),
              image_loc=row.image_loc,
              modified_dt=row.modified_dt) for row in result]
        
        result.close()
        return all_blogs
    
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Requested service is unavailable due to internal server error")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="An unexpected error occurred")


def get_blog_by_id(id: int, conn: Connection = None) -> BlogData:
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
                        content=row.content, 
                        image_loc=row.image_loc, 
                        modified_dt=row.modified_dt)
        result.close()
        return blog
    
    except SQLAlchemyError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Requested service is unavailable due to internal server error")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="An unexpected error occurred")
    

def create_blog(title: str, author: str, content: str, conn: Connection = None) -> None:
    try:
        query = f"""
            INSERT INTO blog_db.blog (title, author, content, modified_dt)
            VALUES ('{title}', '{author}', '{content}', now())
        """
        conn.execute(text(query))
        conn.commit()
    
    except SQLAlchemyError as e:
        print(e)
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Failed to create blog due to bad request")



def update_blog(id:int, title: str, author: str, content: str, conn: Connection = None):
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

    except SQLAlchemyError as e:
        print(e)
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Failed to update blog due to bad request")


def delete_blog(id: int, conn: Connection = None):
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

    except SQLAlchemyError as e:
        print(e)
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Requested service is unavailable due to internal server error")