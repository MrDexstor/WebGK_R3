#!/bin/bash

# Проверяем, передан ли аргумент
if [ "$#" -ne 1 ]; then
  echo "Использование: $0 {run|stop}"
  exit 1
fi

# Определяем действие на основе аргумента
case "$1" in
  run)
    cd ~/WebGK_R3
    echo 'Загрузка ядра сервера'
    screen -wipe
    echo 'Удалены устаревшие сессии'
    screen -dmS rsgk
    echo 'Создан рабочий стол сервера'
    screen -S rsgk -X screen scripts/web.sh
    screen -S rsgk -X screen scripts/redis.sh
    screen -S rsgk -X screen scripts/celery.sh
    echo 'Отданы все команды запуска'
    ;;
  stop)
    cd ~/WebGK_R3
    echo 'Остановка сервера'
    screen -S rsgk -X quit
    echo 'Удаление сессии screen'
    screen -wipe
    echo 'Сервер остановлен и сессия удалена'
    ;;
  *)
    echo "Неверный аргумент: $1"
    echo "Использование: $0 {run|stop}"
    exit 1
    ;;
esac