from .. import models, schemas
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session 
from ..database import  get_db
from typing import  List

router=APIRouter(
    prefix="/posts",
    tags=['posts']
)


@router.get("/posts",response_model=List[schemas.Post])
async def get_posts(db : Session = Depends(get_db)):
    # cursor.execute("""select * from posts """)
    # posts= cursor.fetchall()
    posts= db.query(models.Post).all()
    print(posts)
    return posts



@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db : Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (Title,Content,Published) VALUES (%s,%s,%s) RETURNING
    # *""",
    # (post.title,post.content,post.published))
    # new_post=cursor.fetchone
    # conn.commit()

    new_post=models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

#Title str, content str

@router.get("/{id}",response_model=schemas.Post)
def get_post(id: int, response: Response, db : Session = Depends(get_db)):
    post= db.query(models.Post).filter(models.Post.id==id).first()
    print(post)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
        # response.status_code= status.HTTP_404_NOT_FOUND
        # return {'Message': f"post with id: {id} was not found"}
    return post

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db : Session = Depends(get_db)):

    post= db.query(models.Post).filter(models.Post.id==id)
    # cursor.execute(""" DELETE FROM posts WHERE id=  RETURNING *""")
    # #deleting post
    # #find index in array that has required id
    # index=find_index_post(id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")
    # my_posts.pop(index) 
    # return Response(status_code=status.HTTP_204_NO_CONTENT)

    post.delete(synchronize_session=False)
    db.commit() 