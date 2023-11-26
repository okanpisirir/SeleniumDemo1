import mysql.connector
import time
import json


with open('./dbconn.json', 'r') as file:
    config_data = json.load(file)

db_connection = mysql.connector.connect(
        host=config_data['host'],
        port=config_data['port'],
        user=config_data['user'],
        password=config_data['password'],
        database=config_data['database']
    )

def log_at(funcname, basarili, isSuccess):
    try:
        # Her çağrı öncesi bağlantı oluştur
        db_connection = mysql.connector.connect(
            host=config_data['host'],
            port=config_data['port'],
            user=config_data['user'],
            password=config_data['password'],
            database=config_data['database']
        )

        if db_connection.is_connected():
            cursor = db_connection.cursor()

            # Tabloya veri ekleyin
            insert_query = "INSERT INTO log (funcname, detail, isSuccess, processtime) VALUES (%s, %s, %s, %s)"
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            data_to_insert = (funcname, basarili, isSuccess, current_time)
            cursor.execute(insert_query, data_to_insert)

            # Değişiklikleri kaydet
            db_connection.commit()

    except Exception as e:
        print(f"Hata: {e}")

    finally:
        # Her durumda cursor ve bağlantıyı kapat
        if 'cursor' in locals():
            cursor.close()
        if db_connection.is_connected():
            db_connection.close()
