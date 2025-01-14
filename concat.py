# Задаём имя входного файла и готовим SQL-запрос
input_file = 'output.txt'
output_sql_file = 'insert_data.sql'

# Читаем содержимое текстового файла
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Удаляем символы новой строки и лишние пробелы
lines = [line.strip() for line in lines if line.strip()]

# Соединяем данные через запятую
data_string = ', '.join(lines)

# Формируем SQL-запрос
table_name = 'your_table_name'  # Замените на имя вашей таблицы
sql_query = f"INSERT INTO {table_name} (your_column_name) VALUES ({data_string});"

# Сохраняем SQL-запрос в файл
with open(output_sql_file, 'w', encoding='utf-8') as file:
    file.write(sql_query)

print(f"SQL-запрос сохранён в файле: {output_sql_file}")
