from fastapi import FastAPI

app = FastAPI()

@app.get("/buzondevoz/{numero}")
def buzon(numero):
    return {
        "respuesta": "El buzón de voz del número: " + numero + " está lleno"
    }

@app.get("/estudiante/{nombre}/{carnet}/")
def estudiante(nombre, carnet, carrera):
    return {
        "nombre": nombre,
        "carnet": carnet,
        "carrera": carrera,
        "respuesta": "El estudiante " + nombre + " con carnet " + carnet + " de la carrera " + carrera + " ha sido inscrito exitosamente"
    }

@app.get("/coordenadas/{X}/{Y}")
def coordenadas(X, Y):
    return {
        "X": X,
        "Y": Y,
        "respuesta": "Las coordenadas son: (" + X + ", " + Y + ")"
    }
