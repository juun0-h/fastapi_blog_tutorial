from fastapi import status, UploadFile
from fastapi.exceptions import HTTPException
from sqlalchemy import text, Connection
from sqlalchemy.exc import SQLAlchemyError
from schemas.blog_schema import BlogData
from utils import utils
from dotenv import load_dotenv
import os, time

load_dotenv()
UPLOAD_DIR = os.getenv("UPLOAD_DIR")


def get_all_blogs(conn: Connection) -> list[BlogData]:
    try:
        # 1. Python: image_loc가 None인 경우 default 이미지 경로로 설정
        # DB → Python으로 null 값 전송 → Python에서 조건 체크 → 값 변경
        # 추가적인 메모리 사용과 처리 시간 필요
        # query = """
        #     SELECT id, title, author, content, image_loc, modified_dt FROM blog;
        # """
        # result = conn.execute(text(query))
        # all_blogs = [BlogData(id=row.id,
        #       title=row.title,
        #       author=row.author,
        #       content=utils.truncate_text(row.content),
        #       image_loc=row.image_loc or '/static/default/blog_default.png',
        #       modified_dt=row.modified_dt) for row in result]

        # 2. SQL 최적화: COALESCE를 사용하여 image_loc가 NULL인 경우 default 이미지 경로로 설정
        # 메모리에서 바로 올바른 값으로 로드됨
        query = """
            SELECT id, title, author, content, 
                COALESCE(image_loc, '/static/default/blog_default.png') as image_loc, 
                modified_dt 
            FROM blog;
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
        if blog.image_loc is None:
            blog.image_loc = '/static/default/blog_default.png'

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

def upload_file(author: str, imagefile: UploadFile = None):
    try:
        user_dir = f"{UPLOAD_DIR}/{author}/"

        if not os.path.exists(user_dir):
            os.makedirs(user_dir)

        fname_only, ext = os.path.splitext(imagefile.filename)
        upload_fname = f"{fname_only}_{int(time.time())}{ext}"
        upload_file_loc = f"{user_dir}{upload_fname}"
        print(f"###########Upload file location: {upload_file_loc}###########")
        with open(upload_file_loc, "wb") as outfile:
            while content := imagefile.file.read(1024):
                outfile.write(content)

        # print(f"###########Upload complete: {upload_file_loc}###########")
        return upload_file_loc[1:]
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="An unexpected error occurred while uploading the file")


def create_blog(title: str, author: str, content: str, image_loc: str = None, conn: Connection = None) -> None:
    try:
        query = f"""
            INSERT INTO blog_db.blog (title, author, content, image_loc, modified_dt)
            VALUES ('{title}', '{author}', '{content}', {utils.none_to_null(image_loc, is_single_quote=True)}, now())
        """
        conn.execute(text(query))
        conn.commit()
    
    except SQLAlchemyError as e:
        print(e)
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Failed to create blog due to bad request")



def update_blog(id:int, title: str, author: str, content: str, image_loc: str | None, conn: Connection = None):
    try:
        query = f"""
            UPDATE blog_db.blog
            SET title = :title, author = :author, content = :content, image_loc = :image_loc, modified_dt = now()
            WHERE id = :id
        """
        bind_stmt = text(query).bindparams(id=id, title=title, author=author, content=content, image_loc=image_loc)
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


def delete_blog(id: int, image_loc: str | None, conn: Connection = None):
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

        if image_loc is not None and os.path.exists(f".{image_loc}"):
            print(f".{image_loc}")
            os.remove(f".{image_loc}")

    except SQLAlchemyError as e:
        print(e)
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail="Requested service is unavailable due to internal server error")
    
    except Exception as e:
        print(e)
        conn.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="An unexpected error occurred")