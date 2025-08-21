# 🚫 MAX Zamedlyator

**Описание:**  
MAX Zamedlyator — скрипт для блокировки всех запросов к серверам приложения **MAX** (`max.ru`), делая его полностью нерабочим на всех устройствах, подключённых к вашей сети. Можно использовать на ПК и мобильных устройствах через хотспот.  

**Примечание:** В будущем планируется добавить обход блокировка YouTube и Discord, чтобы они работали корректно через ваш хотспот.  

---

## 📥 Скачать

Вы можете скачать **готовый .exe файл** с релизов GitHub:  
[Releases](https://github.com/yourusername/max-blocker/releases)
https://github.com/kefiiiiir/max-zamedlyator/edit/main/README.md
Или использовать скрипт на Python:

```bash
git clone https://github.com/kefiiiiir/max-zamedlyator.git
cd max-blocker
python max_blocker.py
```
---

## ⚡ Требования

- Windows (для работы с firewall)
- Python 3.x
- Модули: `dnslib`, `dnspython`

## 🛠 Как использовать 
- Подключите компьютер к интернету.
- Запустите скрипт или .exe. Скрипт создаст локальный DNS-сервер и добавит firewall правила для блокировки MAX.
- Создайте Wi-Fi хотспот на ПК с SSID (например, Sch00lWiFi).
- Подключите устройства (телефоны, планшеты, ноутбуки) к вашему хотспоту. Скрипт начнёт блокировать MAX автоматически.
