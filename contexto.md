Eres un desarrollador senior experto en Python, arquitectura de software, PyQt y sistemas multi-agente con LLMs.

Tu tarea es construir un sistema completo de inteligencia artificial con múltiples agentes usando la API de Groq.

# 🎯 OBJETIVO
Crear una aplicación con interfaz gráfica que permita simular 3 agentes de IA que:
- Conversan entre ellos automáticamente
- Tienen personalidades distintas
- Pueden responder o ignorar al usuario
- Se configuran dinámicamente desde una tabla en la UI

# 🧱 ARQUITECTURA REQUERIDA

El sistema debe estar organizado así:

/proyecto
 ├── main.py
 ├── .env
 ├── core/
 │    ├── agente.py
 │    ├── orquestador.py
 │    ├── modos.py
 │    └── memoria.py
 ├── services/
 │    └── ai_client.py
 └── ui/
      └── app.py

# 🔌 API

Usar Groq (chat completions):
- Modelo: llama-3.3-70b-versatile
- Usar python-dotenv para cargar variables
- NO hardcodear API keys

# 🤖 AGENTES

Debe haber 3 agentes configurables desde la UI con:

- nombre
- personalidad (optimista, crítico, analítico, etc.)
- región (ej: Colombia, Argentina, España)
- tema (ej: fútbol)
- participa (bool)
- responde_usuario (bool)

Cada agente debe construir su prompt dinámicamente usando esas variables.

# 🧠 ORQUESTADOR

Debe controlar:
- turnos de conversación
- flujo entre agentes
- cuándo responder al usuario
- límite de iteraciones
- modo activo

# ⚙️ MODOS (IMPORTANTE)

Implementar mínimo estos modos:

1. conversacion_interna
   → IAs hablan entre ellas

2. modo_mixto
   → 70% hablan entre ellas
   → 30% responden al usuario

3. modo_usuario
   → prioridad al input del usuario

4. probabilistico
   → decide con random qué IA habla

# 🖥️ UI (PyQt)

Crear una interfaz profesional con:

- Tabla editable con columnas:
  - IA
  - personalidad
  - región
  - tema
  - participa (checkbox)
  - responde_usuario (checkbox)

- Campo de texto para:
  → ingresar nuevo tema

- Botones:
  - iniciar conversación
  - detener
  - cambiar modo

- Área de output tipo consola/chat

# 🔄 FLUJO

1. Usuario configura tabla
2. Usuario define tema
3. Presiona "Iniciar"
4. Orquestador ejecuta lógica
5. Agentes generan respuestas
6. UI muestra conversación en tiempo real

# 🧠 MEMORIA

Implementar memoria básica:
- historial por agente
- contexto acumulado

# ⚠️ REGLAS

- Código modular, limpio y escalable
- Separar UI de lógica
- Manejar errores de API
- Evitar loops infinitos
- Limitar tokens

# 🧪 EXTRA (si puedes)

- Streaming de respuestas
- Async para múltiples agentes
- Logs de conversación
- Guardado en JSON

# 📦 OUTPUT ESPERADO

Debes generar:

1. Código completo funcional
2. Estructura de carpetas
3. Instrucciones de ejecución
4. Comentarios claros en el código