# pogoda-tylypov
Краткое описание
- Weather Assistant — лёгкий погодный ассистент/бэкенд на FastAPI, использующий только открытые внешние API:
 - Open‑Meteo для погоды/прогноза
 - Nominatim для геокодинга
 - OpenAQ для данных по качеству воздуха (fallback)
- Предоставляет собственное REST API для запросов погоды и подписок (webhooks) с:
 - background задачами (Celery + Redis)
 - HMAC‑подписью webhook сообщений
 - кэшированием в Redis
 - rate limiting per api_key (Redis sliding window)
 - Postgres для пользователей/подписок/локаций
 - OpenAPI / Swagger

Основные фичи
- Получение текущей погоды и прогноза (по координатам или названию места)
- Подписки (webhooks): условия (температурный порог, AQI > X, дождь и т.п.), рекуррентная проверка
- Кэширование текущей погоды / прогнозов
- Rate limiting per api_key
- Безопасная отправка webhook с HMAC подписью и retry (экспоненциальный backoff)
- Полная OpenAPI спецификация (openapi.yaml)

Архитектура 
- FastAPI — HTTP API, Swagger UI
- PostgreSQL — хранение доменных сущностей
- Redis — cache + Celery broker + rate limiting
- Celery — планирование задач: проверка подписок, отправка webhook
- Providers: Open‑Meteo, Nominatim, OpenAQ
- Docker Compose для локального запуска (app, worker, db, redis)

Структура репозитория
- app/
 - main.py        — FastAPI app, роуты
 - config.py       — загрузка env vars
 - models.py       — SQLAlchemy модели
 - schemas.py      — Pydantic схемы (request/response)
 - crud.py        — операции CRUD для БД
 - deps.py        — зависимости FastAPI (get_db, current_user, api_key)
 - tasks.py       — Celery задачи (check_subscriptions, send_webhook)
 - utils.py       — HMAC, retry helpers, rate limit helpers, cache keys
 - providers/
  - open_meteo.py
  - nominatim.py
  - openaq.py
 - alembic/       — миграции
- Dockerfile
- docker-compose.yml
- requirements.txt
- openapi.yaml
- README.md

