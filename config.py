import os 
DATABASE_USER = "root"
DATABASE_PASSWORD = "ramazan20021117"
DATABASE_HOST = "localhost"
DATABASE_NAME = "car_db"

# Ссылка на базу данных
MYSQL_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

CSV_FILE_NAME = "mashina_kg.csv"