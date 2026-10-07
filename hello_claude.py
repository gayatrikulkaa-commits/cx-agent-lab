from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Say hello!"}],
)
print(next(b.text for b in message.content if b.type == "text"))
