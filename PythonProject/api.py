from fastapi import FastAPI
import pymongo

app = FastAPI()
MONGO_URI = "mongodb+srv://viniciuszapella_db_user:VDCkhL8dliaUVFR9@cluster0.vcouow0.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGO_URI)
db = client["variante_motores-db"]
collection = db["kotlin"]

@app.get("/status")
def get_status():

    cursor = collection.find({}, {"_id": 0}).sort("_id", -1).limit(5)
    return list(cursor)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)