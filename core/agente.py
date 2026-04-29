from typing import Optional

from services.ai_client import GroqClient
from .memoria import Memoria


class Agente:
    def __init__(
        self,
        nombre: str,
        personalidad: str,
        region: str,
        tema: str,
        participa: bool,
        responde_usuario: bool,
        client: GroqClient,
        memoria: Optional[Memoria] = None,
    ):
        self.nombre = nombre
        self.personalidad = personalidad
        self.region = region
        self.tema = tema
        self.participa = participa
        self.responde_usuario = responde_usuario
        self.client = client
        self.memoria = memoria

    def _build_system_prompt(self) -> str:
        instrucciones = [
            f"Eres {self.nombre}, un agente de IA con personalidad {self.personalidad}.",
            f"Tu región de referencia es {self.region} y el tema central de la conversación es {self.tema}.",
            "Mantén el tono y estilo de tu personalidad, protege la coherencia y evita contradicciones.",
            "Si el usuario envía una pregunta, responde de forma concisa, contextualizada y respetuosa.",
        ]

        if not self.participa:
            instrucciones.append("No participes activamente en la conversación si no estás marcado como participante.")

        if not self.responde_usuario:
            instrucciones.append("No asumas que debes responder al usuario a menos que se te solicite explícitamente.")

        return " ".join(instrucciones)

    def _build_user_message(self, mensaje: str, contexto: Optional[str] = None) -> str:
        partes = []
        if contexto:
            partes.append(f"Contexto de conversación:\n{contexto}")
        partes.append(f"Instrucción para el agente: {mensaje}")
        partes.append("Responde como este agente con la personalidad definida y usando el contexto disponible.")
        return "\n\n".join(partes)

    def responder(self, mensaje: str, contexto: Optional[str] = None) -> str:
        system_prompt = self._build_system_prompt()
        user_message = self._build_user_message(mensaje, contexto)

        respuesta = self.client.chat(system_prompt, user_message)

        if self.memoria is not None:
            self.memoria.guardar(self.nombre, respuesta, origen="agente")

        return respuesta
