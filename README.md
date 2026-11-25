# Python CI/CD Calculator Application

![Python CI Application](https://github.com/dmytrooliinyk-aks26m-oss/stps-lab1-cicd/actions/workflows/python-app.yml/badge.svg)

Навчальний проєкт для демонстрації налаштування конвеєра безперервної інтеграції (CI) за допомогою **GitHub Actions**, перевірки якості коду лінтером **flake8**, захисту конфіденційних даних через **GitHub Secrets** та управління вимогами за допомогою **GitHub Issues & Projects**.

## Основний функціонал
- Модуль арифметичних операцій (`calculator.py`) із функціями додавання та віднімання.
- Автоматизовані модульні тести (`test_calculator.py`) на базі стандартної бібліотеки `unittest`.
- Перевірка відповідності коду стандарту оформлення **PEP 8** за допомогою статичного аналізатора `flake8`.
- Автоматичний запуск перевірок при кожному `push` та `pull_request` у гілку `main`.
