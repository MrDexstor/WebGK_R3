import requests
from Lib.BO_Checks import check_network, sessionCheck
from Core.config import BO_Url
from Lib import BOm
from datetime import datetime


@check_network('li-create')
@sessionCheck
def createDoc(request, name, positions =[]):
    url = f'{BO_Url()}/api/local-inventories'
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d.%m.%Y %H:%M:%S")

    LIconf = {
        "creationDateTime":formatted_datetime,
        "name":name,
        "positionsCreationParameters": positions

    }
    response = requests.post(url, headers=BOm.getHeader(request.user), json=LIconf)

    return response.json()
