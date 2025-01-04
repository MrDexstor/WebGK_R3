from WebGK.settings import BASE_DIR
# Настройки системы WebGK

# Режим локального тестового сервера
Develop_Server_Connect = False

# Ссылка на BackOffice
BO_Urls = 'http://bo-O003.x5.ru:8096'

# Дирректория для хранения файлов загрузок
FS_DIR = BASE_DIR / 'upload'

# Наименование рабочей сети WiFi
LAN_WIFI_SSID = 'Dmitr.Sorokovykh'

#ДАЛЕЕ НИЧЕГО НЕ МЕНЯЕМ!!!
# Обработчики настроек
def BO_Url():
    if Develop_Server_Connect:
        return 'http://127.0.0.1:8096'
    else:
        return BO_Urls
