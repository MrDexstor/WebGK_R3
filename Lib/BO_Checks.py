import json, requests, termux
from WebGK.settings import BASE_DIR
from Core.config import BO_Url
from Lib import BOm
from Core.models import User 
from ServerAPI import sessions

def check_network(funct_name):
    def network_check(function):
        def wrapper(*args, **kwargs):
            wifi = termux.API.generic(['termux-wifi-scaninfo'])[1]
            if wifi == {'API_ERROR': 'Location needs to be enabled on the device'}:
                result = json.load(open(BASE_DIR/f'dev/respone_templates/{funct_name}.json')) 
            else: 
                lan_detected = False
                for point in wifi:
                    if point['ssid'] == 'Dmitr.Sorokovykh':
                        lan_detected = True
                        break
                
                if lan_detected:
                    result = function(*args, **kwargs)
                else:
                    result = json.load(open(BASE_DIR/f'dev/respone_templates/{funct_name}.json')) 
            return result
        return wrapper
    return network_check
    



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