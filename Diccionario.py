meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CHEVERE" : "Algo genial",
            "ROFL" : "Una respuesta a una broma",
            "SHEESH" : "Ligera desaprobación"
            }

user = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ").upper()

if user in meme_dict.keys():
    print(meme_dict[user])
else :
    print("La palabra no existe")
