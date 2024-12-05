def getHeader(user, logined=False):
    if logined:
        header = {
           "No-Authentication" : 'True',
           "Authorization" : f'Basic {user.backoffice_login}'
        }
    else:
        header = {
                "Authorization": f"Bearer {user.bearer_token}"
            }
    
    return header