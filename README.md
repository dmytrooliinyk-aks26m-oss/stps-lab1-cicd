# STPS Lab 1 — CI/CD Pipeline та документування коду

![Python CI Application](https://github.com/dmytrooliinyk-aks26m-oss/stps-lab1-cicd/actions/workflows/python-app.yml/badge.svg)

Навчальний проєкт з дисципліни **«Сучасні технології створення програмних систем»**.

## Структура репозиторію
- `calculator.py` — модуль бізнес-логіки з типізацією та Google-style docstrings;
- `test_calculator.py` — модульні тести (`unittest`);
- `.github/workflows/python-app.yml` — конвеєр GitHub Actions (перевірка стилю `flake8` та запуск тестів).

## Локальний запуск та перевірка
```bash
flake8 .
python -m unittest discover -v
```
