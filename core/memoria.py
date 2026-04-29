import json
from datetime import datetime
from typing import Dict, List, Optional

class Memoria:
    def __init__(self):
        self.historial_agentes: Dict[str, List[Dict[str, str]]] = {}
        self.contexto: List[str] = []

    def reset(self) -> None:
        self.historial_agentes = {}
        self.contexto = []

    def guardar(self, agente_nombre: str, texto: str, origen: str = "agente") -> None:
        registro = {
            "origen": origen,
            "texto": texto,
            "fecha": datetime.utcnow().isoformat() + "Z",
        }

        if origen == "agente":
            self.historial_agentes.setdefault(agente_nombre, []).append(registro)
            self.contexto.append(f"{agente_nombre}: {texto}")
        else:
            self.contexto.append(f"Usuario: {texto}")

    def obtener_contexto(self, max_mensajes: int = 8) -> str:
        return "\n".join(self.contexto[-max_mensajes:])

    def exportar_json(self, ruta: str = "memoria.json") -> None:
        resultado = {
            "historial_agentes": self.historial_agentes,
            "contexto": self.contexto,
        }

        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(resultado, archivo, indent=2, ensure_ascii=False)
