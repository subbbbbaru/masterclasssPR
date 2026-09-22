# Веб-сервис расчета скидок и налогов (CI/CD Workshop)

![CI Pipeline](https://github.com/subbbbbaru/cicd_workshop/actions/workflows/ci.yml/badge.svg)

Специализированный учебный модуль для отработки навыков автоматизации CI/CD и проведения Code Review.

## Функциональность
* Расчет итоговой стоимости товара с учетом скидки (`calculate_discount`)
* Расчет суммы налога от дохода (`calculate_tax`)
* Полное покрытие модульными тестами (Pytest)
* Автоматическая проверка стиля (Flake8) и безопасности (Bandit)

## Локальный запуск и тестирование
1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/ваш_логин/cicd_workshop.git
   ```
2. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запустить тесты:
   ```bash
   pytest -v
   ```