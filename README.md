# 🏥 Health Academy | Академия Здоровья
<img width="1920" height="903" alt="image" src="https://github.com/user-attachments/assets/00aabb1d-8512-4fc7-b4f6-4c8c7d41e2d3" />
<img width="1790" height="862" alt="image" src="https://github.com/user-attachments/assets/0d544110-f8d0-4522-a529-ef593a9aae80" />
<img width="1920" height="730" alt="image" src="https://github.com/user-attachments/assets/236d0446-7e74-431c-b46d-4b9ee816b145" />
<img width="1829" height="893" alt="image" src="https://github.com/user-attachments/assets/cdbd36b3-d5b1-4d51-9096-da873db14246" />
<img width="1919" height="869" alt="image" src="https://github.com/user-attachments/assets/bcc417f1-9353-45d3-b995-08c6af60b878" />

<div align="center">

![Django](https://img.shields.io/badge/Django-5.1.4-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Stripe](https://img.shields.io/badge/Stripe-Payment-008CDD?style=for-the-badge&logo=stripe&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

**Современная медицинская платформа для управления приемами и платежами**

[Особенности](#-особенности) • [Установка](#-установка) • [Использование](#-использование) • [Документация](#-документация) • [Контакты](#-контакты)

---

</div>

## 📋 Оглавление

- [О проекте](#-о-проекте)
- [Особенности](#-особенности)
- [Технологии](#-технологии)
- [Системные требования](#-системные-требования)
- [Установка](#-установка)
- [Конфигурация](#-конфигурация)
- [Использование](#-использование)
- [Структура проекта](#-структура-проекта)
- [API Endpoints](#-api-endpoints)
- [Скриншоты](#-скриншоты)
- [Roadmap](#-roadmap)
- [Вклад в проект](#-вклад-в-проект)
- [Лицензия](#-лицензия)
- [Контакты](#-контакты)

---

## 🎯 О проекте

**Health Academy** — это полнофункциональная веб-платформа для управления медицинскими услугами, разработанная на Django. Система предоставляет удобный интерфейс для взаимодействия врачей и пациентов, онлайн-запись на прием, интеграцию с платежной системой Stripe и многое другое.

### 🌟 Зачем этот проект?

- ✅ Упрощает процесс записи на прием к врачу
- ✅ Автоматизирует управление расписанием врачей
- ✅ Обеспечивает безопасные онлайн-платежи
- ✅ Предоставляет детальную статистику и отчеты
- ✅ Улучшает коммуникацию между врачами и пациентами

---

## ✨ Особенности

### 👥 Управление пользователями

- **Две роли пользователей**: Врачи (Doctor) и Пациенты (Patient)
- Регистрация и аутентификация
- Персонализированные профили
- Система уведомлений

### 🩺 Для врачей

- 📊 Личная панель управления с статистикой
- 📅 Управление расписанием и доступностью
- 👨‍⚕️ Просмотр и управление записями пациентов
- 💰 Отслеживание платежей и доходов
- 🔔 Уведомления о новых записях

### 🧑‍🦱 Для пациентов

- 🔍 Поиск врачей по специальности
- 📝 Онлайн-запись на прием
- 💳 Безопасная оплата через Stripe
- 📜 История посещений и платежей
- ⭐ Оценка и отзывы о врачах

### 💻 Технические особенности

- 🎨 Современный responsive дизайн (Bootstrap 5)
- 🔒 Система безопасности и авторизации
- 💾 SQLite база данных
- 📧 Email-уведомления
- 🌐 Мультиязычность (Русский/English)
- 📱 Адаптивный интерфейс для мобильных устройств

---

## 🛠 Технологии

### Backend
- **Django 5.1.4** - Web framework
- **Python 3.12** - Programming language
- **SQLite** - Database
- **Django Crispy Forms** - Form rendering
- **Jazzmin** - Admin panel

### Frontend
- **Bootstrap 5.3.3** - CSS Framework
- **Font Awesome 6.0** - Icons
- **Google Fonts (Roboto)** - Typography
- **Vanilla JavaScript** - Interactivity

### Интеграции
- **Stripe API** - Payment processing
- **SMTP** - Email notifications

---

## 💻 Системные требования

- **Python**: 3.12 или выше
- **pip**: Последняя версия
- **Git**: Для клонирования репозитория
- **Виртуальное окружение**: venv (рекомендуется)

### Минимальные требования

- **ОС**: Windows 10+, macOS 10.14+, Linux (Ubuntu 20.04+)
- **RAM**: 2 GB
- **Disk Space**: 500 MB

---

## 🚀 Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/yourusername/django_healthacademy.git
cd django_healthacademy
```

### 2. Создание виртуального окружения

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения

Создайте файл `.env` в корневой директории:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Stripe API Keys
STRIPE_PUBLIC_KEY=pk_test_your_public_key
STRIPE_SECRET_KEY=sk_test_your_secret_key

# Email Configuration (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True
```

### 5. Применение миграций

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Создание суперпользователя

```bash
python manage.py createsuperuser
```

Следуйте инструкциям для создания админ-аккаунта.

### 7. Сбор статических файлов

```bash
python manage.py collectstatic --noinput
```

### 8. Запуск сервера разработки

```bash
python manage.py runserver
```

Откройте браузер и перейдите по адресу: `http://127.0.0.1:8000`

---

## ⚙️ Конфигурация

### Настройка Stripe

1. Зарегистрируйтесь на [Stripe](https://stripe.com)
2. Получите API ключи в Dashboard → Developers → API keys
3. Добавьте ключи в файл `.env`
4. Настройте webhook endpoints (опционально)

### Настройка Email

Для Gmail:
1. Включите 2-факторную аутентификацию
2. Сгенерируйте App Password
3. Добавьте учетные данные в `.env`

### Настройка базы данных

По умолчанию используется SQLite. Для PostgreSQL:

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'healthacademy_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## 📖 Использование

### Для администратора

1. Войдите в админ-панель: `http://127.0.0.1:8000/admin`
2. Управляйте пользователями, врачами, записями
3. Просматривайте статистику и отчеты

### Для врача

1. Зарегистрируйтесь с типом пользователя "Doctor"
2. Заполните профиль (специальность, график работы)
3. Управляйте записями через личный кабинет
4. Отслеживайте платежи

### Для пациента

1. Зарегистрируйтесь с типом пользователя "Patient"
2. Найдите врача по специальности
3. Запишитесь на прием
4. Оплатите визит через Stripe
5. Получите подтверждение

---

## 📁 Структура проекта

```
django_healthacademy/
├── 📁 base/                    # Основное приложение
│   ├── models.py              # Модели БД
│   ├── views.py               # Представления
│   ├── urls.py                # URL маршруты
│   └── templates/             # Шаблоны
│
├── 📁 userauths/              # Аутентификация
│   ├── models.py              # Пользовательская модель
│   ├── forms.py               # Формы регистрации/входа
│   └── views.py               # Логика авторизации
│
├── 📁 patient/                # Приложение пациента
│   ├── views.py               # Dashboard, записи
│   ├── models.py              # Модели пациента
│   └── templates/             # Шаблоны пациента
│
├── 📁 physician/              # Приложение врача
│   ├── views.py               # Dashboard, управление
│   ├── models.py              # Модели врача
│   └── templates/             # Шаблоны врача
│
├── 📁 static/                 # Статические файлы
│   ├── assets/css/           # CSS стили
│   ├── assets/js/            # JavaScript
│   └── assets/images/        # Изображения
│
├── 📁 templates/              # Общие шаблоны
│   └── base/
│       └── base.html         # Базовый шаблон
│
├── 📁 media/                  # Загружаемые файлы
├── manage.py                  # Django CLI
├── requirements.txt           # Зависимости
├── .env                       # Переменные окружения
└── README.md                  # Документация
```

---

## 🔌 API Endpoints

### Главные маршруты

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/` | Главная страница |
| GET | `/about/` | О нас |
| GET | `/contact/` | Контакты |

### Аутентификация

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET/POST | `/register/` | Регистрация |
| GET/POST | `/login/` | Вход |
| GET | `/logout/` | Выход |

### Пациент

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/patient/dashboard/` | Панель управления |
| GET | `/patient/appointments/` | Мои записи |
| GET | `/patient/payments/` | История платежей |
| GET | `/patient/notifications/` | Уведомления |
| GET/POST | `/patient/profile/` | Профиль |

### Врач

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/physician/dashboard/` | Панель управления |
| GET | `/physician/appointments/` | Записи пациентов |
| GET | `/physician/payments/` | Платежи |
| GET | `/physician/notifications/` | Уведомления |
| GET/POST | `/physician/profile/` | Профиль |

---

## Источник
https://www.youtube.com/watch?v=3aRyCwP6ibY&list=LL&index=2&t=141s
### Главная страница
![Home Page](screenshots/home.png)

### Dashboard врача
![Doctor Dashboard](screenshots/doctor-dashboard.png)

### Dashboard пациента
![Patient Dashboard](screenshots/patient-dashboard.png)

### Страница оплаты
![Payment Page](screenshots/payment.png)

<div align="center">

**Сделано с ❤️ для улучшения медицинского обслуживания**

⭐ Не забудьте поставить звезду, если проект вам понравился!

[⬆ Вернуться к началу](#-health-academy--академия-здоровья)

</div>
