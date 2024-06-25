# from fastapi.testclient import TestClient
# from app.main import app
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from app.database import get_db
# from app.config import settings
# from app.database import Base
# import pytest
# from app import models
# from app.oauth2 import create_access_token
# # SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>:<@ip address/hostname>/<database_name'
# # SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:root@localhost/fastapi'

# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:root@localhost:5432/fastapi_test'
# # SQLALCHEMY_DATABASE_URL = f'''postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'''

# engine =create_engine(SQLALCHEMY_DATABASE_URL)

# TestingSessionLocal = sessionmaker(autocommit = False, autoflush = False, bind=engine)




# # client = TestClient(app)

# @pytest.fixture()
# def session():
#     Base.metadata.drop_all(bind=engine)
#     Base.metadata.create_all(bind=engine)

#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @pytest.fixture()
# def client(session):
#     def override_get_db():
#         try:
#             yield session
#         finally:
#             session.close()

   
#     app.dependency_overrides[get_db]=override_get_db
#     yield TestClient(app)



# @pytest.fixture
# def test_user(client):
#     user_data = {
#         "email":"khizrmohd@gmail.com",
#         "password":"password1234"
#     }
#     res = client.post("/users/", json=user_data)

#     assert res.status_code==201
#     print(res.json())
#     new_user = res.json()
#     new_user['password'] = user_data['password']
#     return new_user


# @pytest.fixture
# def token(test_user):
#     return create_access_token({"user_id":test_user['id']})


# @pytest.fixture
# def authorized_client(client,token):
#     client.headers = {
#         **client.headers,
#         "Authorization":f"Bearer {token}"
#     }

#     return client


# @pytest.fixture
# def test_posts(test_user, session):
#     posts_data = [{
#         "title": "first title",
#         "content": "first content",
#         "owner_id": test_user['id']
#     },{
#         "title": "2nd title",
#         "content": "2nd content",
#         "owner_id": test_user['id']
#     },{
#         "title": "3rd title",
#         "content": "3rd content",
#         "owner_id": test_user['id']
#     }]

#     def create_post_model(post):
#        return models.Post(**post)
    
#     post_map = map(create_post_model, posts_data)

#     posts = list(post_map)
#     session.add_all(posts)
#     session.commit()

#     posts = session.query(models.Post).all()
#     print('************')
#     # print(posts[0].id)
#     post_dict_list = []
#     for post in posts:
#         print(post.id)
#         out={
#             'id':post.id,
#             'title':post.title,
#             'content':post.content,
#             'published':post.published,
#             'created_at':post.created_at,
#             'owner_id':post.owner_id,
            
#         }
#         post_dict_list.append(out)
#         print(out)
#     print(post_dict_list)
#     return post_dict_list


from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app

from app.config import settings
from app.database import get_db
from app.database import Base
from app.oauth2 import create_access_token
from app import models
from alembic import command


# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password123@localhost:5432/fastapi_test'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    print("my session fixture ran")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():

        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user2(client):
    user_data = {"email": "sanjeev123@gmail.com",
                 "password": "password123"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def test_user(client):
    user_data = {"email": "sanjeev@gmail.com",
                 "password": "password123"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user['id']})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }
    print(client.get('/posts'))
    return client


@pytest.fixture
def test_posts(test_user, session, test_user2):
    posts_data = [{
        "title": "first title",
        "content": "first content",
        "owner_id": test_user['id']
    }, {
        "title": "2nd title",
        "content": "2nd content",
        "owner_id": test_user['id']
    },
        {
        "title": "3rd title",
        "content": "3rd content",
        "owner_id": test_user['id']
    }, {
        "title": "3rd title",
        "content": "3rd content",
        "owner_id": test_user2['id']
    }]

    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model, posts_data)
    posts = list(post_map)

    session.add_all(posts)
    # session.add_all([models.Post(title="first title", content="first content", owner_id=test_user['id']),
    #                 models.Post(title="2nd title", content="2nd content", owner_id=test_user['id']), models.Post(title="3rd title", content="3rd content", owner_id=test_user['id'])])
    session.commit()

    posts = session.query(models.Post).all()
    return posts