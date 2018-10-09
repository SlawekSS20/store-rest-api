from werkzeug.security import safe_str_cmp  # funkcja do bezpiecznego porównania stringów
from models.user import UserModel


# funkcja sprawdza user i pass, jak ok zwraca obiekt user jak nie -> None
def authenticate(username, password):
    user = UserModel.find_by_user_name(username)
    if user and safe_str_cmp(user.password, password):
        return user


# w payload jest json (? sprawdzić), z którego wyciągamy id i szukamy usera - potrzebne do JWT
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


