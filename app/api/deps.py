def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    return payload["sub"]


def require_permission(permission: str):
    def checker(user: User = Depends(get_current_user)):
        if permission not in user.permissions:
            raise HTTPException(status_code=403)
        return True
    return checker
