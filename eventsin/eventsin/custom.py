from social_auth.models import UserSocialAuth

def create_user(backend, details, response, uid, username, user=None, *args,
                **kwargs):
    """Create user. Depends on get_username pipeline."""
    if user:
        return {'user': user}
    if not username:
        return None

    # Customization 
    email = details.get('email')
    new_user = UserSocialAuth.create_user(username=email, email=email)
    new_user.is_staff = True

    try:
        from settings import SOCIAL_AUTH_CREATE_USERS_AS_SUPER_ADMIN
        if SOCIAL_AUTH_CREATE_USERS_AS_SUPER_ADMIN:
            new_user.is_superuser = True        
    except:
        pass    
    
    return {
        'user': new_user,         
        'is_new': True
    }


