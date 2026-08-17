from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()


def call_agent(system_instructions: str, context: str) -> str:
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1500,
        system=context,
        messages=[{"role": "user", "content": system_instructions}],
    )
    # print(response.usage)
    text = "".join(block.text for block in response.content if block.type == "text")
    return text
