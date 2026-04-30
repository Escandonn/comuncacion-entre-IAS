from pathlib import Path
from string import Template
from typing import Optional

from services.ai_client import GroqClient
from .memoria import Memoria


class Agente:
    PROMPT_TEMPLATE_PATH = Path(__file__).resolve().parents[1] / "pront.md"

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
        pais: str = "Colombia",
    ):
        self.nombre = nombre
        self.personalidad = personalidad
        self.region = region
        self.tema = tema
        self.participa = participa
        self.responde_usuario = responde_usuario
        self.client = client
        self.memoria = memoria
        self.pais = pais

    @classmethod
    def _leer_prompt_template(cls) -> str:
        if not cls.PROMPT_TEMPLATE_PATH.exists():
            raise FileNotFoundError(f"No se encontró el archivo de prompt: {cls.PROMPT_TEMPLATE_PATH}")
        return cls.PROMPT_TEMPLATE_PATH.read_text(encoding="utf-8")

    def _build_system_prompt(self, mensaje: str) -> str:
        prompt_raw = self._leer_prompt_template()
        plantilla = Template(prompt_raw)

        tipo_interaccion = "responde" if self.responde_usuario else "pregunta"
        responde_a = "Usuario" if self.responde_usuario else "otros participantes"
        tiempo_respuesta = "medio"

        return plantilla.safe_substitute(
            tema=self.tema or "general",
            personalidad=self.personalidad or "neutral",
            pais=self.pais,
            region=self.region,
            tipo_interaccion=tipo_interaccion,
            responde_a=responde_a,
            tiempo_respuesta=tiempo_respuesta,
            mensaje=mensaje or f"Continúa la conversación sobre {self.tema}.",
        )

    def _build_user_message(self, mensaje: str, contexto: Optional[str] = None) -> str:
        partes = []
        if contexto:
            partes.append(f"Contexto de conversación:\n{contexto}")
        partes.append(f"Mensaje actual: {mensaje}")
        partes.append("Responde usando tu personalidad y el contexto anterior.")
        return "\n\n".join(partes)

    def responder(self, mensaje: str, contexto: Optional[str] = None) -> str:
        system_prompt = self._build_system_prompt(mensaje)
        user_message = self._build_user_message(mensaje, contexto)

        respuesta = self.client.chat(system_prompt, user_message)

        if self.memoria is not None:
            self.memoria.guardar(self.nombre, respuesta, origen="agente")

        return respuesta
