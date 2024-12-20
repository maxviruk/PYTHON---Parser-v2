# Задаём имя входного и выходного файла (в формате .txt)
input_file = 'input.txt'
output_file = 'output.txt'

# Читаем содержимое текстового файла
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Удаляем символы новой строки и лишние пробелы
lines = [line.strip() for line in lines if line.strip()]

# Обрабатываем строки: разделяем по запятой, не разделяя внутри кавычек ''
result = []
for line in lines:
    parts = []
    buffer = ''
    inside_quotes = False
    for char in line:
        if char == "'":
            inside_quotes = not inside_quotes
        if char == ',' and not inside_quotes:
            parts.append(buffer.strip())
            buffer = ''
        else:
            buffer += char
    if buffer:
        parts.append(buffer.strip())
    result.extend(parts)

# Убираем дубликаты
unique_data = list(set(result))

# Сохраняем результат в выходной текстовый файл
with open(output_file, 'w', encoding='utf-8') as file:
    for item in unique_data:
        file.write(item + '\n')

print(f"Результат сохранён в файле: {output_file}")
