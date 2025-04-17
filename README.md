# Тестовое задание YADRO - DevOps

Этот репозиторий содержит решения для тестового задания на позицию DevOps Engineer в компании YADRO.

## Структура репозитория

```
.
├── README.md              # Главный README файл репозитория
├── task_1_linux/          # Решения для Задания 1 (Linux команды)
│   └── commands.md        # Файл с командами и пояснениями
├── task_2_scripting/      # Решения для Задания 2 (Bash/Python скрипт)
│   ├── config.txt         # Пример файла с данными
│   ├── search_simple.sh   # Простой Bash скрипт
│   ├── search_complex.sh  # Сложный Bash скрипт (с параметрами)
│   ├── search_simple.py   # Простой Python скрипт
│   └── search_complex.py  # Сложный Python скрипт (с параметрами)
└── task_3_docker/         # Решения для Задания 3 (Docker)
    ├── Dockerfile         # Оптимизированный Dockerfile
    ├── Dockerfile.original # Оригинальный Dockerfile (для сравнения)
    ├── README.md          # README для Docker-задачи с пояснениями
    ├── config.txt         # Конфигурационный файл для скрипта внутри Docker
    └── search_complex.py  # Python скрипт, используемый в Docker
```

## Задание 1: Linux команды

Решение находится в файле `task_1_linux/commands.md`.

*   **Задача 1.1:** Создание файла `hello.txt` с текстом "Hello, DevOps!" и вывод его содержимого.
*   **Задача 1.2:** Поиск строк с заданным словом (например, "error") в лог-файле и вывод первых 5 совпадений с использованием конвейера.

## Задание 2: Bash/Python скрипт

Решения находятся в директории `task_2_scripting/`.

*   **Задача:** Найти строки, содержащие определенное слово, в заданном файле (`config.txt`).
*   **Реализация:**
    *   Представлены скрипты на Bash (`search_*.sh`) и Python (`search_*.py`).
    *   Реализованы как простой вариант (слово и файл "зашиты" в скрипт), так и сложный (слово и файл передаются как параметры командной строки).
    *   Python-скрипт `search_complex.py` использует `argparse` для удобной работы с аргументами и включает обработку ошибок.

*   **Пример использования (сложный Python вариант):**
    ```bash
    cd task_2_scripting
    python3 search_complex.py config.txt path
    # Или для поиска без учета регистра:
    python3 search_complex.py config.txt Path -i
    ```

## Задание 3: Docker

Решение находится в директории `task_3_docker/`.

*   **Задача:** Оптимизировать предоставленный `Dockerfile`.
*   **Реализация:**
    *   Оптимизированный `Dockerfile` использует легковесный базовый образ `python:3.9-slim-buster`.
    *   Применены лучшие практики: `WORKDIR`, непривилегированный пользователь (`USER`), `CMD` в формате exec, минимизация слоев (за счет выбора базового образа).
    *   Dockerfile копирует `search_complex.py` и `config.txt` и запускает скрипт для поиска слова "path" в `config.txt` по умолчанию.
    *   Подробные пояснения по оптимизации приведены в `task_3_docker/README.md`.

*   **Сборка и запуск Docker-образа:**
    ```bash
    cd task_3_docker
    # Сборка образа
    docker build -t yadro-test-app .
    # Запуск контейнера (выполнит поиск "path" в config.txt)
    docker run --rm yadro-test-app
    # Запуск контейнера с другими параметрами (например, поиск слова "port")
    docker run --rm yadro-test-app ./search_complex.py config.txt port
    ```
