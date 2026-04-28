# 🤖 Multi-Agent AI System (Groq)

Sistema experimental de **multi-agentes conversacionales** usando la API de Groq.
Permite simular múltiples IAs con diferentes roles interactuando entre sí (debates, análisis, pipelines, etc.).

---

## 🚀 Características

* 🧠 Arquitectura basada en **Orquestador + Agentes**
* 🤖 Múltiples roles (optimista, crítico, juez, etc.)
* ⚡ Integración con Groq (alta velocidad de inferencia)
* 🔐 Manejo seguro de credenciales con `.env`
* 🧩 Código modular y escalable

---

## 📁 Estructura del proyecto

```
proyecto/
 ├── .env
 ├── main.py
 ├── core/
 │    ├── agente.py
 │    └── orquestador.py
 └── services/
      └── ai_client.py
```

---

## ⚙️ Instalación

### 1. Clonar repositorio

```
git clone <tu-repo>
cd proyecto
```

### 2. Instalar dependencias

```
pip install groq python-dotenv
```

---

## 🔐 Configuración

Crear archivo `.env` en la raíz:

```
GROQ_API_KEY=tu_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

> ⚠️ No subir este archivo a GitHub

---

## ▶️ Uso

Ejecutar:

```
python main.py
```

Esto iniciará una conversación automática entre agentes definidos en el sistema.

---

## 🧠 Ejemplo de agentes

* **Optimista** → Defiende la IA
* **Crítico** → Cuestiona riesgos
* **Juez** → Analiza y concluye

---

## 🔄 Flujo de ejecución

```
Usuario → Orquestador → Agente 1 → Agente 2 → Agente 3 → ...
```

El orquestador controla:

* turnos
* flujo de mensajes
* límite de iteraciones

---

## ⚡ Roadmap

* [ ] Memoria de conversación (contexto persistente)
* [ ] Streaming en tiempo real
* [ ] Async multi-agente
* [ ] Interfaz gráfica (PyQt)
* [ ] Persistencia (JSON / DB)

---

## 🧪 Casos de uso

* Simulación de debates
* Generación de ideas
* Validación de decisiones
* Sistemas autónomos experimentales

---

## ⚠️ Notas

* Controlar número de turnos para evitar loops infinitos
* Ajustar temperatura según tipo de interacción
* Definir roles claros para mejores resultados

---

## 📄 Licencia

MIT

---

## ✨ Autor

Proyecto experimental de arquitectura multi-agente en Python
