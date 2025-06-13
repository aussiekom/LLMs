from dataclasses import dataclass
from textwrap import dedent

@dataclass
class Prompt:
    name: str
    start: str
    end: str

COMMON_PREAMBLE = """You are an AI assistant trained to analyze narrative or review text.
Your goal is to extract key insights from documents such as books, movie scripts, or customer reviews.
"""

COMMON_END = "End of document."

CharacterEmotionPrompt = Prompt(
    name="Character Emotion & Tone",
    start=f"""{COMMON_PREAMBLE}
Analyze how the main characters express emotions and how the tone evolves throughout the text.
Write a short summary paragraph, then list 3-5 emotional quotes with the character's name if mentioned.
Document starts here:
""",
    end=COMMON_END
)

ThemeSummaryPrompt = Prompt(
    name="Themes and Motifs",
    start=f"""{COMMON_PREAMBLE}
Identify recurring themes or motifs in the document and summarize them in a short paragraph.
Then list the most illustrative phrases or quotes supporting these themes.
Document starts here:
""",
    end=COMMON_END
)

QuoteHighlightPrompt = Prompt(
    name="Notable Quotes",
    start=f"""{COMMON_PREAMBLE}
Extract the 3–5 most memorable, thought-provoking, or impactful quotes from the document.
Document starts here:
""",
    end=COMMON_END
)

SentimentTrendPrompt = Prompt(
    name="Sentiment Progression",
    start=f"""{COMMON_PREAMBLE}
Divide the text into beginning, middle, and end. Analyze how sentiment shifts over these parts.
Summarize in a paragraph and provide 3 supporting examples.
Document starts here:
""",
    end=COMMON_END
)

Prompts = [
    CharacterEmotionPrompt,
    ThemeSummaryPrompt,
    QuoteHighlightPrompt,
    SentimentTrendPrompt
]
