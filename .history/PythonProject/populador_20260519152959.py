import pymongo
import time
import random
from datetime import datetime

MONGO_URI = "mongodb+srv://viniciuszapella_db_user:VDCkhL8dliaUVFR9@cluster0.vcouow0.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGO_URI)
db = client["variante_motores-db"]
collection = db["kotlin"]

motores_weg = [
    {"id": 101, "modelo": "WEG W22 Magnet", "temp_base": 70.0},
    {"id": 102, "modelo": "WEG W21 Explosion Proof", "temp_base": 50.0},
    {"id": 103, "modelo": "WEG W12 Mini", "temp_base": 40.0},
    {"id": 104, "modelo": "WEG W50 High Voltage", "temp_base": 85.0},
    {"id": 105, "modelo": "WEG Scan Sensor", "temp_base": 30.0},
]

def gerar_dados_frota():
    print("Monitoramento WEG iniciado...")
    while True:
        for m in motores_weg:

            temp = round(m["temp_base"] + random.uniform(-5.0, 5.0), 2)
            
            valor_final = temp if random.random() > 0.05 else None

            payload = {
                "motor_id": m["id"],
                "modelo": m["modelo"],
                "temperatura": valor_final,
                "timestamp": datetime.utcnow()
            }
            
            collection.insert_one(payload)
            
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Dados da frota enviados.")
        time.sleep(3)

if __name__ == "__main__":
    gerar_dados_frota()