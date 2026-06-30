from app.schemas.users import UserCreate
from app.service.users.users_service import UserService

def test_create_user(db_session):
    service = UserService(db_session)
    data = UserCreate(username="Jenavarro", 
                      password="Eliasnavarro16*", 
                      role="viewer")
    result = service.create_user(data)
    assert result.username
    assert result.role == "viewer"
    assert result.status is True
    assert result.user_id is not None
