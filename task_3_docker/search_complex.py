#!/usr/bin/env python3
import sys
import argparse # Используем argparse для лучшей обработки аргументов

# Скрипт для поиска заданного слова в заданном файле
# Файл и слово передаются как аргументы командной строки

# Настройка парсера аргументов
parser = argparse.ArgumentParser(
    description="Ищет строки, содержащие заданное слово, в указанном файле.",
    epilog="Пример: python3 search_complex.py config.txt path"
)
parser.add_argument("filename", help="Путь к файлу для поиска")
parser.add_argument("search_word", help="Слово для поиска")
parser.add_argument(
    "-i", "--ignore-case",
    action="store_true", # Создает булев флаг
    help="Игнорировать регистр при поиске"
)

# Парсим аргументы командной строки
args = parser.parse_args()

# Используем значения из args
filename = args.filename
search_word = args.search_word
ignore_case = args.ignore_case

print(f"--- Поиск слова '{search_word}' в файле '{filename}' (параметры Python) ---")
if ignore_case:
    print("--- Режим поиска: без учета регистра ---")

found_something = False # Флаг для отслеживания, найдено ли что-то

try:
    with open(filename, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, 1):
            # Применяем ignore_case если нужно
            line_to_check = line
            word_to_check = search_word
            if ignore_case:
                line_to_check = line.lower()
                word_to_check = search_word.lower()

            # Проверяем наличие слова
            if word_to_check in line_to_check:
                print(f"{line_number}: {line.strip()}")
                found_something = True

    # Сообщение, если ничего не найдено
    if not found_something:
        print(f"\nСлово '{search_word}' не найдено в файле '{filename}'.")
        sys.exit(1) # Выходим с кодом 1, если ничего не найдено (по аналогии с grep)

except FileNotFoundError:
    print(f"Ошибка: Файл '{filename}' не найден.")
    sys.exit(2) # Другой код ошибки для отличия
except PermissionError:
     print(f"Ошибка: Недостаточно прав для чтения файла '{filename}'.")
     sys.exit(3) # Другой код ошибки
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")
    sys.exit(4) # Другой код ошибки

print(f"--- Поиск завершен ---")
# Если дошли сюда и что-то нашли, выходим с кодом 0
sys.exit(0) 