# QA-trainee-assignment-autumn-2025


## Задание 1

Детальные баг-репорты, содержащие:
- Описание багов
- Приоритет и пояснение к нему
- Ожидаемый и полученный результат
- Скриншоты отображения бага

Находятся в файле **[TASK-1-BUGS.md](https://github.com/ByZeWay/QA-trainee-assignment-autumn-2025/blob/main/TASK-1-BUGS.md)**

Файлы **image-2.png**...**image.24.png** - скриншоты, приведенные в баг-репорте к первому заданию


## Задание 2.1

### Описание файлов проекта

#### **[api_client.py](https://github.com/ByZeWay/QA-trainee-assignment-autumn-2025/blob/main/api_client.py)**
Базовый клиент для работы с HTTP API. Содержит методы для выполнения POST, GET, DELETE запросов с автоматической установкой заголовков Content-Type и Accept.

#### **[conftest.py](https://github.com/ByZeWay/QA-trainee-assignment-autumn-2025/blob/main/conftest.py)**
Конфигурационный файл pytest содержащий:
- Фикстуры для клиентов API (v1 и v2)
- Генерацию тестовых данных
- Фикстуру для создания тестовых объявлений
- Функции для извлечения ID из ответов API

#### **[test_api_v1.py](https://github.com/ByZeWay/QA-trainee-assignment-autumn-2025/blob/main/test_api_v1.py)**
Тесты для эндпоинтов API версии 1:
- Создание объявлений (позитивные и негативные сценарии)
- Получение объявлений по ID и продавцу
- Получение статистики
- Валидация входных данных
- Тесты граничных значений

#### **[test_api_v2.py](https://github.com/ByZeWay/QA-trainee-assignment-autumn-2025/blob/main/test_api_v2.py)**
Тесты для эндпоинтов API версии 2:
- Удаление объявлений
- Получение статистики
- Проверка консистентности версий API

#### **[test_lifecycle.py](https://github.com/ByZeWay/QA-trainee-assignment-autumn-2025/blob/main/test_lifecycle.py)**
Интеграционные тесты полного жизненного цикла объявления:
- Последовательное создание, получение, удаление
- Параллельные операции с одним объявлением

#### **[TESTCASES.md](https://github.com/ByZeWay/QA-trainee-assignment-autumn-2025/blob/main/TESTCASES.md)**
Полная документация тест-кейсов, содержащая:
- Предусловия и шаги выполнения
- Ожидаемые результаты
- Приоритеты тестов
- Ссылки на эндпоинты

#### **[BUGS.md](https://github.com/ByZeWay/QA-trainee-assignment-autumn-2025/blob/main/BUGS.md)**
Детальные баг-репорты, содержащие:
- Описание багов
- Шаги воспроизведения
- Ожидаемое и фактическое поведение
- Приоритеты и влияние на систему

---

### Установка и запуск

#### Предварительные требования
- Python 3.8 или выше
- pip (менеджер пакетов Python)

#### Шаг 1: Установка зависимостей
```bash
pip install -r requirements.txt
```

#### Шаг 2: Запуск тестов

**Запуск всех тестов:**
```bash
python -m pytest -v --html=report.html
```

**Запуск тестов для конкретной версии API:**
```bash
# Только API v1
python -m pytest test_api_v1.py -v

# Только API v2
python -m pytest test_api_v2.py -v

# Только интеграционные тесты
python -m pytest test_lifecycle.py -v
```

#### Шаг 3: Просмотр результатов

После завершения тестов в файле `report.html` в браузере можно просмотреть детальный отчет

---
