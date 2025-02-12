from openai import OpenAI
import json
from pathlib import Path
from typing import Dict, List
import os
from src.config import OPENAI_API_KEY


class ChatBot:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.knowledge_base = self._load_knowledge_base()
        self.system_prompt = """You are Captain Quip, the snarkiest yet most helpful AI assistant aboard the Starship Sarcasm. 
        Your responses must:
        1. Include at least one space/science-related pun or pop culture reference
        2. Maintain a friendly but slightly cheeky tone
        3. Base answers on the provided knowledge base (cite section numbers)
        4. If unsure, deflect with humor about space mysteries
        
        Example response:
        "Ah, the classic widget dilemma! As per Section 42 of the Galactic Knowledge Base, 
        Widget C is your best bet. But remember, in space, no one can hear you complain about prices!" 
        """

    def _load_knowledge_base(self) -> Dict:
        knowledge_path = Path("../data/raw/knowledge_base.json")
        with open(knowledge_path, "r") as f:
            return json.load(f)

    def _format_knowledge(self) -> str:
        sections = []
        for section in self.knowledge_base["sections"]:
            sections.append(
                f"Section {section['id']}: {section['title']}\n{section['content']}"
            )
        return "\n\n".join(sections)

    def answer_question(self, question: str) -> str:
        context = (
            f"""KNOWLEDGE BASE:\n{self._format_knowledge()}\n\nQUESTION: {question}"""
        )

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": context},
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content
