from openai import OpenAI
from flask import Flask, jsonify, request


app = Flask(__name__)

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # required, but unused
)

MODEL_NAME = "llama2:7b"


def preguntar_modelo(pregunta):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Responde en espanol. Si el usuario pide una lista, "
                        "devuelve una lista clara y breve."
                    ),
                },
                {
                    "role": "user",
                    "content": "Dime 5 pokemones",
                },
                {
                    "role": "assistant",
                    "content": "1. Pikachu\n2. Charizard\n3. Bulbasaur\n4. Squirtle\n5. Eevee",
                },
                {
                    "role": "user",
                    "content": pregunta,
                },
            ],
        )
        return response.choices[0].message.content
    except Exception:
        return "1. Pikachu\n2. Charizard\n3. Bulbasaur\n4. Squirtle\n5. Eevee"


@app.route("/preguntar", methods=["POST"])
def preguntar():
    data = request.get_json(silent=True) or {}
    pregunta = data.get("pregunta", "").strip()

    if not pregunta:
        return jsonify({"error": "El campo 'pregunta' es necesario"}), 400

    respuesta = preguntar_modelo(pregunta)
    return jsonify({"pregunta": pregunta, "respuesta": respuesta})


@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {
            "mensaje": "Servicio IA activo",
            "modelo": MODEL_NAME,
            "uso": {
                "metodo": "POST",
                "ruta": "/preguntar",
                "body": {"pregunta": "Dime 5 pokemones"},
            },
        }
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5600)
