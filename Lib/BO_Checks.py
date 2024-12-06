import json, requests
from WebGK.settings import BASE_DIR
from Core.config import BO_Url
from Lib import BOm

def server_avalible(funct_name):
    def server_avalible_checker(function):
        def wrapper(*args, **kwargs):
            try:
                 requests.get(f'{BO_Url()}/ping')
            except Exception:
                result = json.load(open(BASE_DIR/f'dev/respone_templates/{funct_name}.json'))
            else:
                result = function(*args, **kwargs)
            return result
        return wrapper
    return server_avalible_checker
    

def loginBO(request):
    account = User.objects.get(id=request.user.id)
    account.bearer_token = sessions.login(request)['accessToken']['value']
    account.save()
    
    
def session_check(funct):
    def wrapper(request, *args, **kwargs):
        loginBO(request)
        result = funct(request, *args, **kwargs)
        return result
    return wrapper