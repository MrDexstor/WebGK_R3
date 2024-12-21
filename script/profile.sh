echo 'Добро пожаловать в систему установки WebGK (R3)'
echo ''
echo 'Устанавливаю зависимости...'
apt update
apt upgrade
apt install screen python redis -y
echo 'Зависимости установлены'
cd WebGK_R3
echo 'Подтягиваю зависимости проекта...'
pip install django celery tzdata requests
echo 'Зависимости проекта установлены'
echo 'Начинаю процедуру конфигурирования WGK'
python script/prof_gen.py
echo 'Конфигурирование завершено!'
echo 'Формирую файлы для запуска систем...'
cd 
cp ~/WebGK_R3/script/rsgk.sh /data/data/com.termux/files/usr/bin/rsgk
cd 
cd WebGK_R3 
python manage.py makemigrations
python manage.py migrate
echo 'Регистрация IT Соотрудника'
python manage.py createsuperuser
rsgk run
