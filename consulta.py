import json
import sys
from urllib import request, error


API_URL = "http://localhost:5600/preguntar"


def obtener_pregunta():
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:]).strip()
    return input("Escribe tu pregunta: ").strip()


def consultar_ia(pregunta):
    payload = json.dumps({"pregunta": pregunta}).encode("utf-8")
    req = request.Request(
        API_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with request.urlopen(req) as response:
        body = response.read().decode("utf-8")
        return json.loads(body)


def main():
    pregunta = obtener_pregunta()

    if not pregunta:
        print("Debes ingresar una pregunta.")
        return

    try:
        data = consultar_ia(pregunta)
        print("\nRespuesta de la IA:\n")
        print(data.get("respuesta", "Sin respuesta"))
    except error.URLError:
        print("No se pudo conectar con la API. Verifica que IA/app.py este ejecutandose.")
    except Exception as exc:
        print(f"Ocurrio un error: {exc}")


if __name__ == "__main__":
    main()
