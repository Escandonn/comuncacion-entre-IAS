import random
import time
from typing import Callable, List, Optional

from .agente import Agente
from .memoria import Memoria
from .modos import (
    CONVERSACION_INTERNA,
    MODO_MIXTO,
    MODO_USUARIO,
    PROBABILISTICO,
)


class Orquestador:
    def __init__(
        self,
        agentes: List[Agente],
        memoria: Optional[Memoria] = None,
        max_turnos: int = 8,
        delay: float = 1.0,
    ):
        self.agentes = agentes
        self.memoria = memoria or Memoria()
        self.max_turnos = max_turnos
        self.delay = delay

    def iniciar(
        self,
        tema: str,
        usuario_texto: str = "",
        modo: str = MODO_MIXTO,
        callback: Optional[Callable[[str], None]] = None,
        stop_checker: Optional[Callable[[], bool]] = None,
    ) -> None:
        participantes = [agente for agente in self.agentes if agente.participa]

        if not participantes:
            raise ValueError("No hay agentes activos. Activa al menos un agente en la UI.")

        for agente in self.agentes:
            agente.memoria = self.memoria

        self.memoria.reset()
        self.memoria.guardar("Sistema", f"Tema: {tema}", origen="usuario")

        if usuario_texto:
            self.memoria.guardar("Usuario", usuario_texto, origen="usuario")

        ultimo_mensaje = usuario_texto or f"Iniciemos la conversación sobre {tema}."

        for turno in range(self.max_turnos):
            if stop_checker and stop_checker():
                break

            agente = self._seleccionar_agente(turno, modo, participantes)
            if agente is None:
                break

            entrada = self._construir_entrada(agente, ultimo_mensaje, usuario_texto, modo)
            if callback:
                callback(f"🟡 Turno {turno + 1} - {agente.nombre}")

            respuesta = agente.responder(entrada, contexto=self.memoria.obtener_contexto())
            if callback:
                callback(f"{agente.nombre}: {respuesta}")

            ultimo_mensaje = respuesta
            time.sleep(self.delay)

        self.memoria.exportar_json()

    def _seleccionar_agente(
        self,
        turno: int,
        modo: str,
        participantes: List[Agente],
    ) -> Optional[Agente]:
        agentes_usuario = [agente for agente in participantes if agente.responde_usuario]

        if modo == CONVERSACION_INTERNA:
            return participantes[turno % len(participantes)]

        if modo == MODO_MIXTO:
            if agentes_usuario and random.random() < 0.3:
                return random.choice(agentes_usuario)
            return participantes[turno % len(participantes)]

        if modo == MODO_USUARIO:
            if agentes_usuario:
                return agentes_usuario[turno % len(agentes_usuario)]
            return participantes[turno % len(participantes)]

        if modo == PROBABILISTICO:
            return random.choice(participantes)

        return participantes[turno % len(participantes)]

    def _construir_entrada(
        self,
        agente: Agente,
        ultimo_mensaje: str,
        usuario_texto: str,
        modo: str,
    ) -> str:
        if agente.responde_usuario and usuario_texto and modo in {MODO_MIXTO, MODO_USUARIO, PROBABILISTICO}:
            return f"Usuario pregunta: {usuario_texto}\nContexto: {ultimo_mensaje}"

        return ultimo_mensaje
