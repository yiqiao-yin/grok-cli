```

██████╗ ██████╗  ██████╗ ██╗  ██╗    ██╗  ██╗     ██████╗██╗     ██╗
██╔════╝ ██╔══██╗██╔═══██╗██║ ██╔╝    ██║  ██║    ██╔════╝██║     ██║
██║  ███╗██████╔╝██║   ██║█████╔╝     ███████║    ██║     ██║     ██║
██║   ██║██╔══██╗██║   ██║██╔═██╗     ╚════██║    ██║     ██║     ██║
╚██████╔╝██║  ██║╚██████╔╝██║  ██╗         ██║    ╚██████╗███████╗██║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝         ╚═╝     ╚═════╝╚══════╝╚═╝

````

> 💬 **Chat with Grok 4 in your terminal.**  
> 🛑 Type `'exit'` to quit.

---

# 🚀 Grok 4 CLI

A sleek, terminal-based LLM interface powered by **xAI's Grok 4** API.  
Supports intelligent tool use with 🎯 [Composio], integrated memory with 🧠 LangChain, and OpenAI compatibility.


## ⚙️ Setup

1. 🔑 Get your **API key** from [https://x.ai/api](https://x.ai/api)
2. 🛠️ Install dependencies:
    ```bash
    pip install -r requirements.txt
    pip install -e .
    ```

3. 🔐 Set your Composio API key:

   ```powershell
   # PowerShell
   $env:COMPOSIO_API_KEY = "your_composio_api_key"
   ```

4. ▶️ Run the CLI:

   ```bash
   grok_cli --api-key YOUR_KEY
   ```

## 💡 Usage

* Just start typing at the `You:` prompt and have a conversation!
* Tool use is automatic when needed (thanks to Composio integrations ⚙️).
* 🔁 Context is preserved via memory.
* 💥 Type `"exit"` to quit gracefully.

---

## 🤝 Credits

This project wouldn’t be possible without:

* 🤖 **[xAI](https://x.ai/)** for the powerful Grok 4 model
* 🧩 **[Composio](https://composio.dev/)** for seamless tool integrations
* 🧠 **[LangChain](https://www.langchain.com/)** for agent orchestration and memory
* ✨ **[OpenAI](https://openai.com/)** for pushing the boundaries of what LLMs can do

---

## 🧙 Tips

* Want to add your own tools? Check out [`composio_langchain`](https://github.com/composio-dev/composio-python)!
* You can modify memory or prompts directly in `grok_cli/agent.py`.

---

🛠 Built with ❤️ by your terminal.
