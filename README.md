# qa-ui-tests-playwright

![CI](https://github.com/narbkv07/qa-ui-tests-playwright/actions/workflows/tests.yml/badge.svg)

UI/E2E-автотесты для [SauceDemo](https://www.saucedemo.com) — стабильного демо-магазина.  
*Demonstrates UI automation with Playwright + Selenium, Page Object Model.*

---

## Что демонстрирует проект

| Навык | Детали |
|---|---|
| **Playwright** | pytest-playwright, локаторы `data-test`, headless-режим |
| **Selenium** | WebDriver, явные ожидания (WebDriverWait), headless Chrome |
| **Page Object Model** | LoginPage, InventoryPage, CartPage, CheckoutPage |
| **E2E-сценарии** | логин, каталог, корзина, оформление заказа |
| **CI/CD** | GitHub Actions, два job-а: Playwright + Selenium |

---

## Стек

- Python 3.13
- Playwright 1.50 / pytest-playwright 0.7
- Selenium 4.27 / webdriver-manager 4.0
- pytest-html 4.1

---

## Структура

```
qa-ui-tests-playwright/
├── pages/
│   ├── login_page.py       # POM: страница входа
│   ├── inventory_page.py   # POM: каталог товаров
│   ├── cart_page.py        # POM: корзина
│   └── checkout_page.py    # POM: оформление заказа
├── tests/                  # Playwright-тесты
│   ├── test_login.py       # 6 тестов: логин / ошибки
│   ├── test_inventory.py   # 5 тестов: сортировка, количество
│   ├── test_cart.py        # 6 тестов: корзина
│   └── test_checkout.py    # 5 тестов: happy path + валидация
├── tests_selenium/         # Selenium smoke-тесты
│   └── test_selenium_smoke.py  # 3 теста: логин + корзина
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .github/workflows/tests.yml
```

---

## Как запустить

```bash
git clone https://github.com/narbkv07/qa-ui-tests-playwright.git
cd qa-ui-tests-playwright

python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Установить Playwright браузеры (один раз)
playwright install chromium

# Запустить все Playwright-тесты (headless по умолчанию)
pytest tests/

# Запустить Selenium-тесты
pytest tests_selenium/

# Запустить с конкретным браузером
pytest tests/ --browser firefox
```

---

## Как смотреть отчёт

После запуска отчёт появляется в `reports/report.html`.

В GitHub Actions: вкладка **Artifacts** → `playwright-report` или `selenium-report`.

---

## Что покрыто

**Playwright (22 теста):**
- Логин: `standard_user` (успех), `locked_out_user`, неверный пароль, пустые поля
- Каталог: количество товаров, сортировка по имени (A→Z, Z→A) и цене (возр./убыв.)
- Корзина: добавление, удаление, счётчик бейджа, переход в корзину, удаление из корзины
- Оформление: happy path → "Thank you", сводка с итогом, валидация (имя/фамилия/индекс)

**Selenium (3 smoke-теста):**
- Успешный логин, ошибка при `locked_out_user`, бейдж корзины после добавления товара
