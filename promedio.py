from pymongo import MongoClient

# Conectarse a la base de datos de MongoDB
client = MongoClient('mongodb+srv://anemone:3mbF4repnPWfbLof@meu.vvjxgc6.mongodb.net/')
db = client['testMeu']
collection = db['interacciones']

# Definir la operación de agregación
pipeline = [
    {"$match": {"panel": "true", "mes": "04"}},
    {"$group": {"_id": None, "avg_calif": {"$avg": "$calif",},}}
]

# Ejecutar la operación de agregación
resultado_agregacion = list(collection.aggregate(pipeline))

# Guardar el resultado en un archivo o en otra colección
with open('resultado_agregacion.json', 'w') as f:
    for documento in resultado_agregacion:
        f.write(str(documento) + '\n')
