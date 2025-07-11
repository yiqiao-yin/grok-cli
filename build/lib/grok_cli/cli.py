import click
import os
from .agent import GrokAgent

@click.command()
@click.option('--api-key', default=None, help='xAI API key. If not provided, uses XAI_API_KEY env var.')
@click.option('--dev', is_flag=True, help='Use cheaper OpenAI model for development (requires OPENAI_API_KEY)')
def main(api_key, dev):
    """CLI tool for interacting with xAI Grok 4."""
    if dev:
        # Development mode with cheaper OpenAI model
        openai_key = os.getenv('OPENAI_API_KEY')
        if not openai_key:
            raise click.UsageError("Development mode requires OPENAI_API_KEY environment variable. Get it from https://platform.openai.com/api-keys")
        agent = GrokAgent(api_key=openai_key, model="gpt-3.5-turbo", base_url="https://api.openai.com/v1")
        print("🚧 DEVELOPMENT MODE: Using OpenAI gpt-3.5-turbo (cheaper)")
    else:
        # Production mode with Grok
        api_key = api_key or os.getenv('XAI_API_KEY')
        if not api_key:
            raise click.UsageError("API key is required. Provide via --api-key or XAI_API_KEY environment variable. Get it from https://x.ai/api.")
        agent = GrokAgent(api_key=api_key)

    print("""
 ██████╗ ██████╗  ██████╗ ██╗  ██╗    ██╗  ██╗     ██████╗██╗     ██╗
██╔════╝ ██╔══██╗██╔═══██╗██║ ██╔╝    ██║  ██║    ██╔════╝██║     ██║
██║  ███╗██████╔╝██║   ██║█████╔╝     ███████║    ██║     ██║     ██║
██║   ██║██╔══██╗██║   ██║██╔═██╗     ╚════██║    ██║     ██║     ██║
╚██████╔╝██║  ██║╚██████╔╝██║  ██╗         ██║    ╚██████╗███████╗██║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝         ╚═╝     ╚═════╝╚══════╝╚═╝
    """)
    print("Chat with Grok 4 in your terminal.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("User: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting Grok CLI. Goodbye!")
            break
        agent.chat(user_input)