from fastapi import FastAPI
import pymongo

app = FastAPI()
MONGO_URI = "mongodb+srv://viniciuszapella_db_user:VDCkhL8dliaUVFR9@cluster0.vcouow0.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGO_URI)
db = client["variante_motores-db"]
collection = db["kotlin"]

@app.get("/status")
def get_status():
    lista_motores = [101, 102, 103, 104, 105]
    status_atual = []
    
    for mid in lista_motores:

        leitura = collection.find({"motor_id": mid}, {"_id": 0}).sort("timestamp", -1).limit(1)
        res = list(leitura)
        if res:
            status_atual.append(res[0])
            
    return status_atual

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)