import requests
from Lib.BO_Checks import server_avalible, session_check
from Core.config import BO_Url
from Lib import BOm
from datetime import datetime


@server_avalible('write-offs-list')
@session_check
def getList(request):
    url = f'{BO_Url()}/api/write-offs'
    response = requests.get(url, headers=BOm.getHeader(request.user))
    return response.json()
    
    
def createDoc(request, docName):
    url = f'{BO_Url()}/api/local-inventories'
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d.%m.%Y %H:%M:%S")
    
    LIconf = {
        "creationDateTime":formatted_datetime,
        "name":docName
        
    }
    response = requests.post(url, headers=BOm.getHeader(request.user), json=LIconf)
    
    return response.json()


@server_avalible('write-offs-docinfo')
@session_check
def offsData(request, docId):
    url = f'{BO_Url()}/api/write-offs/{docId}'
    response = requests.get(url, headers=BOm.getHeader(request.user))
    return response.json()
    

@server_avalible('write-offs-positions')
@session_check
def positions(request, docId):
    url = f'{BO_Url()}/api/write-offs/{docId}/positions'
    response = requests.get(url, headers=BOm.getHeader(request.user))
    return response.json()