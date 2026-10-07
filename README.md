# cx-agent-lab

A starter Python project for a customer-support agent built on Claude.

## Setup

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
uv venv --python 3.13
uv pip install -r requirements.txt
cp .env.example .env   # then add your Anthropic API key to .env
```

## Run

```bash
.venv/bin/python hello_claude.py
```

## License

MIT. See [LICENSE](LICENSE).
