import pytest
from fastapi import HTTPException
from app.schemas.users import UserCreate, UserUpdate
from app.service.users.users_service import UserService


class TestCreateUser:
    def test_create_user_success(self, db_session):
        service = UserService(db_session)
        data = UserCreate(username="Jenavarro", password="Eliasnavarro16*", role="viewer")
        result = service.create_user(data)

        assert result.username == "Jenavarro"
        assert result.role == "viewer"
        assert result.status is True
        assert result.user_id is not None

    def test_create_user_invalid_role(self, db_session):
        service = UserService(db_session)
        data = UserCreate(username="invalido", password="Pass1234*", role="superadmin")
        with pytest.raises(HTTPException) as exc:
            service.create_user(data)
        assert exc.value.status_code == 400
        assert "Rol no valido" in exc.value.detail

    def test_create_username_duplicate(self, db_session):
        service = UserService(db_session)
        data = UserCreate(username="Jenavarro", password="Eliasnavarro16*", role="viewer")
        service.create_user(data)

        with pytest.raises(HTTPException) as exc:
            service.create_user(data)
        assert exc.value.status_code == 400
        assert "username ya esta en uso" in exc.value.detail


class TestGetAllUsers:
    def test_get_all_users_empty(self, db_session):
        service = UserService(db_session)
        users = service.get_all_users()
        assert users == []

    def test_get_all_users_with_data(self, db_session):
        service = UserService(db_session)
        data1 = UserCreate(username="user1", password="Pass1234*", role="viewer")
        data2 = UserCreate(username="user2", password="Pass1234*", role="editor")
        service.create_user(data1)
        service.create_user(data2)

        users = service.get_all_users()
        assert len(users) == 2
        assert users[0].username == "user1"
        assert users[1].username == "user2"


class TestGetUserById:
    def test_get_user_by_id_success(self, db_session):
        service = UserService(db_session)
        data = UserCreate(username="buscado", password="Pass1234*", role="admin")
        created = service.create_user(data)

        result = service.get_user_by_id(created.user_id)
        assert result.user_id == created.user_id
        assert result.username == "buscado"

    def test_get_user_by_id_not_found(self, db_session):
        service = UserService(db_session)
        with pytest.raises(HTTPException) as exc:
            service.get_user_by_id("non-existent-id")
        assert exc.value.status_code == 404
        assert "no encontrado" in exc.value.detail


class TestUpdatePassword:
    def test_update_password_success(self, db_session):
        service = UserService(db_session)
        data = UserCreate(username="passuser", password="Oldpass1*", role="viewer")
        created = service.create_user(data)
        old_hash = created.password

        update_data = UserUpdate(password="Newpass1*")
        result = service.update_password_user(created.user_id, update_data)
        assert result["message"] == "Contraseña actualizada correctamente"

        updated = service.get_user_by_id(created.user_id)
        assert updated.password != old_hash

    def test_update_password_user_not_found(self, db_session):
        service = UserService(db_session)
        update_data = UserUpdate(password="Newpass1*")
        with pytest.raises(HTTPException) as exc:
            service.update_password_user("non-existent-id", update_data)
        assert exc.value.status_code == 404


class TestUpdateRole:
    def test_update_role_success(self, db_session):
        service = UserService(db_session)
        data = UserCreate(username="roleuser", password="Pass1234*", role="viewer")
        created = service.create_user(data)

        update_data = UserUpdate(role="editor")
        result = service.update_role_user(created.user_id, update_data)
        assert result["message"] == "El rol de usuario fue actualizado correctamente"

        updated = service.get_user_by_id(created.user_id)
        assert updated.role == "editor"

    def test_update_role_invalid(self, db_session):
        service = UserService(db_session)
        data = UserCreate(username="roleuser2", password="Pass1234*", role="viewer")
        created = service.create_user(data)

        update_data = UserUpdate(role="invalid_role")
        with pytest.raises(HTTPException) as exc:
            service.update_role_user(created.user_id, update_data)
        assert exc.value.status_code == 400
        assert "Rol no valido" in exc.value.detail

    def test_update_role_user_not_found(self, db_session):
        service = UserService(db_session)
        update_data = UserUpdate(role="admin")
        with pytest.raises(HTTPException) as exc:
            service.update_role_user("non-existent-id", update_data)
        assert exc.value.status_code == 404


class TestDisableUser:
    def test_disable_user(self, db_session):
        service = UserService(db_session)
        data = UserCreate(username="disableuser", password="Pass1234*", role="viewer")
        created = service.create_user(data)

        update_data = UserUpdate(status=False)
        result = service.disable_user(created.user_id, update_data)
        assert "deshabilitado" in result["message"]

        updated = service.get_user_by_id(created.user_id)
        assert updated.status is False

    def test_enable_user(self, db_session):
        service = UserService(db_session)
        data = UserCreate(username="enableuser", password="Pass1234*", role="viewer")
        created = service.create_user(data)

        service.disable_user(created.user_id, UserUpdate(status=False))

        update_data = UserUpdate(status=True)
        result = service.disable_user(created.user_id, update_data)
        assert "habilitado" in result["message"]

        updated = service.get_user_by_id(created.user_id)
        assert updated.status is True

    def test_disable_user_not_found(self, db_session):
        service = UserService(db_session)
        update_data = UserUpdate(status=False)
        with pytest.raises(HTTPException) as exc:
            service.disable_user("non-existent-id", update_data)
        assert exc.value.status_code == 404
