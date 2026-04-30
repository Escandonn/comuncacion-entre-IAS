# 🤖 Sistema Multi-Agente con Interfaz y Tabla (Groq)

Este proyecto crea una aplicación de escritorio que simula una conversación entre tres agentes de IA.
Cada agente tiene:

* nombre
* personalidad
* región
* tema
* participación dinámica
* opción de responder al usuario

La aplicación utiliza la API de Groq para generar texto y una interfaz PyQt para configurar los agentes y ver la conversación en tiempo real.

---

## 📁 Estructura del proyecto

```
Comunicacion-entre-IAS/
 ├── .env
 ├── main.py
 ├── contexto.md
 ├── core/
 │    ├── agente.py
 │    ├── modos.py
 │    ├── memoria.py
 │    └── orquestador.py
 ├── services/
 │    └── ai_client.py
 └── ui/
      ├── app.py
      └── __init__.py
```

---

## 🔧 Requisitos

* Python 3.11+
* Paquetes:
  * groq
  * python-dotenv
  * PyQt5

---

## ⚙️ Instalación

1. Clona el repositorio:

```bash
git clone <tu-repo>
cd "c:\python\Comunicacion-entre-IAS"
```

2. Instala dependencias:

```bash
pip install groq python-dotenv PyQt5
```

3. Crea el archivo .env en la raíz:

```env
GROQ_API_KEY=tu_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

> No subas .env a repositorios públicos.

---

## ▶️ Uso

Ejecuta la aplicación con:

```bash
python main.py
```

La interfaz abrirá una tabla editable con los agentes, el tema, una entrada de usuario y botones para iniciar o detener la conversación.

---

## 🧠 Modos de conversación

* conversacion_interna → sólo los agentes hablan entre sí.
* modo_mixto → 70% interna, 30% respuesta al usuario.
* modo_usuario → prioridad a los agentes que responden al usuario.
* probabilistico → el orquestador elige agentes al azar.

---

## 💡 Flujo de uso

1. Configura los agentes en la tabla.
2. Ingresa un tema principal.
3. Opcional: escribe una entrada de usuario.
4. Elige un modo.
5. Presiona "Iniciar conversación".

---

## 🧠 Memoria y registros

* El sistema guarda el historial por agente.
* El contexto acumulado se usa para mantener coherencia.
* Al finalizar, el historial se exporta a memoria.json.

---

## 🧪 Mejora y extensiones

* Agregar streaming en tiempo real.
* Hacer la llamada a la API asíncrona.
* Guardar conversaciones adicionales en JSON.
* Añadir más agentes y temas dinámicos.

---

## 📄 Licencia

MIT
