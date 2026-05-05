import pymongo
import time
import random
from datetime import datetime

MONGO_URI = "mongodb+srv://viniciuszapella_db_user:VDCkhL8dliaUVFR9@cluster0.vcouow0.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(MONGO_URI)

db = client["variante_motores-db"]
collection = db["kotlin"]

def simular_sensor():
    temp_atual = 55.0  
    print(" Populador iniciado. Enviando dados para o Atlas...")

    while True:
        variacao = random.uniform(-1.5, 2.0)
        temp_atual += variacao
        
        envio_sucesso = random.random() > 0.1
        valor_final = round(temp_atual, 2) if envio_sucesso else None

        payload = {
            "motor_id": 101,
            "temperatura": valor_final,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }

        try:
            collection.insert_one(payload)
            status = f" {valor_final}°C" if envio_sucesso else " SENSOR OFF (NULL)"
            print(f"[LOG] {payload['timestamp']} - {status}")
        except Exception as e:
            print(f"Erro ao inserir: {e}")
        
        time.sleep(1) 

if __name__ == "__main__":
    simular_sensor()