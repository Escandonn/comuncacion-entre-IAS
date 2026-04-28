from services.ai_client import GroqClient
from core.agente import Agente
from core.orquestador import Orquestador

def main():
    client = GroqClient()

    agente1 = Agente(
        "Optimista",
        "Eres una IA optimista que cree en el progreso tecnológico.",
        client
    )

    agente2 = Agente(
        "Crítico",
        "Eres una IA crítica que cuestiona riesgos de la IA.",
        client
    )

    agente3 = Agente(
        "Juez",
        "Eres un juez neutral que analiza ambas posturas y da una conclusión.",
        client
    )

    agentes = [agente1, agente2, agente3]

    orquestador = Orquestador(agentes, max_turnos=6)

    orquestador.iniciar("¿La IA es una amenaza o una oportunidad?")

if __name__ == "__main__":
    main()