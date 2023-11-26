# devops-opneapi

1. Сначала необходимо запустить сервер. Инструкция по его запуску находится в конце файла `socks/README.md`.

2. Затем указать правильные пути в файлах `run.sh`, `./systemd/daemon.service`, `./systemd/logrotate/socks-logrotate.service`, `./systemd/logrotate/logrotate.sh`. В файле `./systemd/daemon.service` указать своего юзера. Также нужно сделать исполняемыми баш-скрипты.

3. Затем нужно перейти в директорию `socks-client` и скопировать systemd конфиги в директорию /etc/systemd/system/:

```
sudo cp ./systemd/daemon.service /etc/systemd/system/daemon.service
sudo cp ./systemd/logrotate/socks-logrotate.service /etc/systemd/system/socks-logrotate.service
sudo cp ./systemd/logrotate/socks-logrotate.timer /etc/systemd/system/socks-logrotate.timer
```

4. Нужно создать директорию `/var/log/socks-client/`

5. Далее можно запустить юниты
```
sudo systemctl daemon-reload
sudo systemctl start socks-logrotate.service
sudo systemctl start socks-logrotate.timer
sudo systemctl start daemon.service
```

Для проверки того, что сервис выдерживает 500е ошибки, можно остановить контейнер БД. Логи должны появляться в директории /var/log/socks-client/.