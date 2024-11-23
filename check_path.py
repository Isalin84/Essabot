import os

# Путь к файлу, который вы хотите проверить
file_path = "docs/H&S_Policy.docx"

# Проверяем существование файла
if os.path.exists(file_path):
    print(f"Файл найден: {os.path.abspath(file_path)}")
else:
    print("Файл не найден. Проверьте путь или наличие файла.")
