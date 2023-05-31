from fastapi import APIRouter, Depends
from app.models.post_model import PostSchema
from app.auth.jwt_bearer import jwtBearer
from app.data_storage import posts

# router for post endpoints
router = APIRouter(prefix="/posts", tags=["post"])


# get posts
@router.get("/")
def get_posts():
    return {"all posts": posts}


# get post by id
@router.get("/{id}")
def get_post_by_id(id: int):
    post_lst = list(filter(lambda p: p["id"] == id, posts))
    if post_lst[0]:
        return {"post": post_lst[0]}
    else:
        raise {"message": "not found"}


# post add post
@router.post("/", dependencies=[Depends(jwtBearer())])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {"message": "post added"}
