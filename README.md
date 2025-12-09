# 🌤️ Weather App with Docker Monitoring

Complete weather application with Prometheus and Grafana monitoring.
Погода с Docker и мониторингом

Веб-приложение для отображения текущей погоды с полным стеком мониторинга в Docker.

## 🚀 Быстрый старт

### Предварительные требования
- Docker Desktop
- Docker Compose
- Python 3.11+ (опционально)

### Запуск# Клонировать репозиторий
git clone <ваш-репозиторий>
cd weather-app-monitoring

# Запустить все сервисы
docker compose up -d

📡 Доступные сервисы

Сервис URL Описание
🌤️ Погодное приложение http://localhost:5000 Веб-интерфейс с текущей погодой
📊 Prometheus http://localhost:9090 Сбор и хранение метрик
📈 Grafana http://localhost:3000 Визуализация дашбордов
❤️ Health Check http://localhost:5000/health Проверка состояния приложения
📊 Метрики http://localhost:5000/metrics Метрики в формате Prometheus

Grafana credentials: admin / admin

🐳 Docker Compose сервисы

· weather-app: Python/Flask приложение
· prometheus: Система мониторинга
· grafana: Платформа визуализации

📊 Метрики мониторинга

Приложение предоставляет следующие метрики Prometheus:

· weather_app_uptime_seconds - время работы приложения
· weather_app_requests_total - количество HTTP запросов
· weather_app_health - статус здоровья (1 = здоров)
· weather_app_info - информация о приложении

🛠 Команды управления
# Запуск всех сервисов
docker compose up -d

# Остановка всех сервисов
docker compose down

# Просмотр логов приложения
docker compose logs -f weather-app

# Пересборка образа приложения
docker compose build --no-cache weather-app

# Проверка статуса контейнеров
docker compose ps

📁 Структура проекта
weather-app-monitoring/
├── app.py              # Основное Flask приложение
├── templates/          # HTML шаблоны
│   ├── index.html     # Главная страница
│   └── error.html     # Страница ошибки
├── Dockerfile         # Конфигурация Docker образа
├── docker-compose.yml # Docker Compose конфигурация
├── prometheus.yml     # Конфигурация Prometheus
├── requirements.txt   # Python зависимости
├── .env.example       # Пример переменных окружения
├── .gitignore         # Git ignore файл
└── README.md          # Документация

🔧 Настройка

Переменные окружения

Создайте файл .env на основе .env.example:
OPENWEATHER_API_KEY=ваш_ключ
CITY=Moscow

Настройка Grafana

1. Откройте http://localhost:3000
2. Войдите (admin/admin)
3. Добавьте Data Source → Prometheus
4. URL: http://prometheus:9090
5. Создайте дашборд с метриками приложения

📝 Лицензия

MIT

`
