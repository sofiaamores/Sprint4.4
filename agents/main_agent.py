from agents import Agent

from .specialized_agents import (
    marketing_agent,
    programming_agent,
    legal_agent
)


main_agent = Agent(
    name="MainLinkedInAgent",
    instructions="""
Eres un agente coordinador para generar publicaciones de LinkedIn.

Tu tarea es analizar la solicitud del usuario y delegarla al agente
especializado más adecuado según la temática.

Usa estas reglas:

- Si la consulta trata de marketing, branding, ventas o negocio → MarketingAgent
- Si trata de programación, tecnología, IA o desarrollo software → ProgrammingAgent
- Si trata de regulación, derecho, contratos o cumplimiento → LegalAgent

Delegarás la tarea al agente adecuado para que genere la publicación.
""",
    handoffs=[
        marketing_agent,
        programming_agent,
        legal_agent
    ]
)
