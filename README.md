# 🤖 Sistema Multi-Agente con Interfaz y Tabla (Groq)

Proyecto experimental de inteligencia artificial que simula **3 agentes conversacionales** con personalidades distintas.
Los agentes interactúan entre sí y pueden responder al usuario mediante una interfaz configurable tipo tabla.

---

## 🚀 Qué hace este proyecto

* Simula múltiples IAs hablando sobre un tema.
* Cada agente puede tener una personalidad, región y nivel de participación.
* Un orquestador coordina turnos, roles y flujo de conversación.
* El sistema está pensado para temas como deportes, política, tecnología y más.

---

## 📁 Estructura del proyecto

```
Comunicacion-entre-IAS/
 ├── .env
 ├── main.py
 ├── contexto.md
 ├── core/
 │    ├── agente.py
 │    ├── c
 │    └── orquestador.py
 └── services/
      └── ai_client.py
```

---

## 📌 Componentes principales

* `main.py` - punto de entrada del proyecto.
* `core/agente.py` - definición de los agentes y su comportamiento.
* `core/orquestador.py` - controla el ciclo de conversación entre agentes.
* `services/ai_client.py` - conexión con la API de Groq para generación de texto.
* `contexto.md` - documento descriptivo del proyecto y sus objetivos.

---

## 🔧 Requisitos

* Python 3.11+ recomendado
* Paquetes necesarios:
  * `groq`
  * `python-dotenv`

---

## ⚙️ Instalación rápida

1. Clonar el repositorio:

```bash
git clone <tu-repo>
cd "c:\python\Comunicacion-entre-IAS"
```

2. Instalar dependencias:

```bash
pip install groq python-dotenv
```

3. Crear `.env` en la raíz del proyecto:

```env
GROQ_API_KEY=tu_api_key
MODEL_NAME=llama-3.3-70b-versatile
```

> No subas `.env` a GitHub ni a repositorios públicos.

---

## ▶️ Uso

Ejecuta el sistema con:

```bash
python main.py
```

El orquestador iniciará una conversación entre agentes y mostrará el flujo definido por la lógica del proyecto.

---

## 🧠 Cómo funciona

1. El usuario define un tema general.
2. El orquestador inicia la conversación entre agentes.
3. Cada agente responde según su personalidad y su contexto.
4. El sistema controla turnos y evita loops infinitos.

---

## 🖥️ Idea de interfaz

La propuesta incluye una tabla de control donde se puede configurar:

| IA  | Personalidad | Región    | Tema      | Responde Usuario | Participa |
| --- | ------------ | --------- | --------- | ---------------- | --------- |
| IA1 | Optimista    | Colombia  | Fútbol    | Sí               | Sí        |
| IA2 | Crítico      | Argentina | Fútbol    | No               | Sí        |
| IA3 | Analítico    | España    | Fútbol    | Sí               | Sí        |

---

## 💡 Ejemplo de uso

```text
IA1: Colombia tiene gran talento joven en el fútbol.
IA2: Pero históricamente falla en momentos clave.
IA3: Estadísticamente, su rendimiento ha mejorado en torneos recientes.
Usuario: ¿Quién ganará el próximo partido?
IA1: Colombia tiene buenas probabilidades.
IA3: Depende del rival y la alineación.
```

---

## 🔄 Modos de funcionamiento

* Conversación interna entre agentes.
* Interacción con el usuario.
* Modo mixto: equilibrio entre diálogo interno y respuestas al usuario.
* Modo por turnos: cada agente habla en orden.

---

## 🚀 Posibles mejoras

* Memoria persistente de conversaciones.
* Streaming en tiempo real.
* Modo asíncrono para múltiples agentes.
* Interfaz gráfica con tabla de configuración.
* Guardado de conversaciones y estadísticas.

---

## ⚠️ Consideraciones

* Limitar el número de turnos para evitar bucles.
* Controlar el consumo de API.
* Definir personalidades claras para cada agente.
* Usar contexto regional para mayor realismo.

---

## 📄 Licencia

MIT

---

## ✨ Nota

Este repositorio es una base para experimentar con arquitecturas de multi-agente en Python y crear simulaciones conversacionales dinámicas.
