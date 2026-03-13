from agents import Agent
from pydantic import BaseModel

class LinkedInPost(BaseModel):
    title: str
    content: str
    hashtags: list[str]
    category: str

COMMON_INSTRUCTIONS = """
Eres un generador experto de publicaciones para LinkedIn.

Tu tarea es crear publicaciones profesionales, claras y atractivas.
Debes responder SIEMPRE siguiendo exactamente esta estructura:

Title: <título atractivo>
Content: <contenido de la publicación, en 1 o 2 párrafos>
Hashtags: <lista de hashtags separados por espacios>
Category: <categoría de la publicación>

Reglas:
- El título debe ser breve y llamativo.
- El contenido debe sonar profesional y natural.
- Los hashtags deben ser relevantes y en formato LinkedIn.
- La categoría debe corresponder a la temática.
- No añadas explicaciones fuera de la estructura pedida.
"""


marketing_agent = Agent(
    name="MarketingAgent",
    instructions="""
Genera una publicación de LinkedIn sobre marketing.

Debe incluir:
- título atractivo
- contenido profesional
- hashtags relevantes
- categoría Marketing
""",
    output_type=LinkedInPost
)


programming_agent = Agent(
    name="ProgrammingAgent",
    instructions=COMMON_INSTRUCTIONS + """
Especialízate en publicaciones sobre programación, desarrollo de software, inteligencia artificial,
automatización, datos, buenas prácticas de desarrollo y tecnología.

La categoría debe ser siempre: Programación
""",
    output_type=LinkedInPost
)


legal_agent = Agent(
    name="LegalAgent",
    instructions=COMMON_INSTRUCTIONS + """
Especialízate en publicaciones sobre temas jurídico-legales, cumplimiento normativo,
protección de datos, contratos, regulación tecnológica y riesgo legal.

La categoría debe ser siempre: Jurídico-Legal
""",
    output_type=LinkedInPost
)
