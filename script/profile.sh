echo 'Добро пожаловать в систему установки WebGK (R3)'
echo ''
echo 'Устанавливаю зависимости...'
apt install screen python -y
echo 'Зависимости установлены'
cd WebGK_R3
echo 'Подтягиваю зависимости проекта...'
pip install -r requirements.txt
echo 'Зависимости проекта установлены'
echo 'Начинаю процедуру конфигурирования WGK'
python script/prof_gen.py
echo 'Конфигурирование завершено!'
echo 'Формирую файлы для запуска систем...'
cd 
cp ~/WebGK_R3/script/RSGK_run.sh ~/run.sh 