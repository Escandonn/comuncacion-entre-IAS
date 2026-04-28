class Orquestador:
    def __init__(self, agentes, max_turnos=6):
        self.agentes = agentes
        self.max_turnos = max_turnos

    def iniciar(self, mensaje_inicial):
        mensaje = mensaje_inicial

        for i in range(self.max_turnos):
            agente = self.agentes[i % len(self.agentes)]

            print(f"\n🟡 Turno {i+1} - {agente.nombre}")

            try:
                respuesta = agente.responder(mensaje)
                print(f"💬 {respuesta}")
                mensaje = respuesta

            except Exception as e:
                print(f"❌ Error en {agente.nombre}: {e}")
                break