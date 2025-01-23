import requests
from celery import shared_task
from SyncModule.libs import ping_external_server, generate_changes_file
from Core.config import REMOTE_ADDRES_SERVER


@shared_task
def InitSyncProcedure():
    #Проверить доступность
    serverAvailable = ping_external_server()
    
    #Сгенерировать файл
    changeFileUrl = generate_changes_file('init')
    
    #Отправить файл
    if serverAvailable:
        remote_server_url = REMOTE_ADDRES_SERVER + '/dbw/file_acceptance/'

        # Открываем файл в бинарном режиме
        with open(changeFileUrl, 'rb') as file:
            # Отправляем файл на удаленный сервер
            response = requests.post(remote_server_url, files={'file': file})
            
            if response.status_code == 200:
                print('[DBS] Файл синхронизации отправлен')
            else:
                print('[DBS] Что то сломалось...')
    else:
        print('[DBS] Файл синхронизации не был отправлен')


@shared_task
def AcceptanceOfChanges(filename):
    #Проверить доступность
    serverAvailable = ping_external_server()
    pass