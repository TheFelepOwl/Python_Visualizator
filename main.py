import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import psycopg2
from sqlalchemy import create_engine
import sys
import os

# З'єднання з базою даних PostgreSQL
db_params = {
    'host': 'localhost',
    'port': '5432',
    'user': 'postgres',
    'password': 'denisanime04',
    'database': 'Lab_2_Havryliuk',
}

connection_str = f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"
engine = create_engine(connection_str)

# Получение значений из аргументов командной строки
start_date = sys.argv[1]
end_date = sys.argv[2]

# SQL-запрос с использованием параметров
sql_query = """
SELECT
    s.city AS Місто,
    mu.Title AS Назва_параметру,
    MAX(mv.value_) AS Результат_вимірювання
FROM
    Station s
JOIN
    Measurment mv ON s.ID_station = mv.station_ID
JOIN
    Measurment_Unit mu ON mv.measurement_unit_ID = mu.ID_Measurment_Unit
WHERE
    mu.Title IN ('PM2.5', 'PM10')
    AND mv.measurement_time >= %(start_date)s
    AND mv.measurement_time <= %(end_date)s
GROUP BY
    s.city, mu.Title;
"""

# Отримання даних з бази даних у вигляді DataFrame
df = pd.read_sql_query(sql_query, engine, params={"start_date": start_date, "end_date": end_date})
filename = "C:\\Users\\TheFelepOwl\\Documents\\nubip\\Tech_DataBase\\DataBase_visualizer\\grafix.png"
if not df.empty:

    # Візуалізація в табличному вигляді за допомогою Seaborn
    table_plot = sns.catplot(x='Місто', y='Результат_вимірювання', hue='Назва_параметру', data=df, kind='bar', height=6, aspect=2)
    plt.title('Максимальні значень шкідливих частинок PM2.5, PM10')
    plt.xlabel('Місто')
    plt.ylabel('Максимальне значення')

    # Візуалізація в графічному вигляді за допомогою Seaborn
    # fig, ax = plt.subplots(figsize=(10, 6))
    # line_plot = sns.lineplot(x='Місто', y='Результат_вимірювання', hue='Назва_параметру', data=df, marker='o', markersize=10, ax=ax)
    # plt.title('Максимальні значення PM2.5 та PM10 за областями')
    # plt.xlabel('Місто')
    # plt.ylabel('Максимальне значення')
    # plt.legend(title='Одиниця виміру', loc='upper right')
    # plt.show()

   


    # Сохранение изображения с проверкой наличия файла
    if os.path.exists(filename):
        os.remove(filename)  # Удаляем существующий файл

    # Сохранение изображения
    table_plot.savefig(filename)

else:
    # Создаем пустой график
    plt.figure()
    plt.savefig(filename)  # Сохраняем пустой график