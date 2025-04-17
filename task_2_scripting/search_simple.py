#!/usr/bin/env python3
import sys

# Простой скрипт для поиска фиксированного слова в фиксированном файле

FILENAME = "config.txt"
SEARCH_WORD = "path"

print(f"--- Поиск слова '{SEARCH_WORD}' в файле '{FILENAME}' (простой Python) ---")

found_lines = []
try:
    # Используем 'with open' для гарантированного закрытия файла
    with open(FILENAME, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, 1):
            # Проверяем, содержит ли строка искомое слово
            if SEARCH_WORD in line:
                # Выводим найденную строку с номером
                # line.strip() убирает пробельные символы (включая \n) по краям
                print(f"{line_number}: {line.strip()}")
                found_lines.append(line)

    if not found_lines:
         print(f"Слово '{SEARCH_WORD}' не найдено в файле '{FILENAME}'.")

except FileNotFoundError:
    print(f"Ошибка: Файл '{FILENAME}' не найден.")
    sys.exit(1) # Выход с кодом ошибки
except Exception as e:
    print(f"Произошла ошибка при чтении файла: {e}")
    sys.exit(1) # Выход с кодом ошибки

print(f"--- Поиск завершен ---")