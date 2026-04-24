# IA

Ejemplo minimo para consultar un modelo local en Ollama usando la misma configuracion base del proyecto principal:

- `base_url`: `http://localhost:11434/v1`
- `api_key`: `ollama`
- `model`: `llama2:7b`

## Archivos

- `app.py`: API Flask con un endpoint para hacer preguntas al modelo.
- `consulta.py`: script simple para enviar una pregunta desde consola.
- `requirements.txt`: dependencias minimas para este ejemplo.

## Requisitos

Necesitas tener Ollama corriendo localmente y el modelo disponible:

```powershell
ollama run llama2:7b
```

## Instalacion

```powershell
cd IA
pip install -r requirements.txt
python app.py
```

Si estas usando el entorno virtual creado dentro de `IA`, puedes ejecutar asi:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

El servicio quedara disponible en:

```text
http://localhost:5600
```

## Ejemplo de uso

```powershell
Invoke-RestMethod `
  -Method Post `
  -Uri "http://localhost:5600/preguntar" `
  -ContentType "application/json" `
  -Body '{"pregunta":"Dime 5 pokemones"}'
```

Tambien puedes usar el script de consola:

```powershell
python consulta.py "Dime 3 pokemones de agua"
```

O con la `.venv` local:

```powershell
.\.venv\Scripts\python.exe consulta.py "Dime 3 pokemones de agua"
```

## Respuesta esperada

```json
{
  "pregunta": "Dime 3 pokemones de agua",
  "respuesta": "1. Squirtle\n2. Blastoise\n3. Gyarados"
}
```

## Nota

El modelo genera la respuesta. Si Ollama falla o el modelo no esta disponible, `app.py` actualmente devuelve un fallback fijo para no romper el endpoint.
