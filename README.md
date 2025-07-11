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

3. 🔐 Set your API key:

   The repo is updated that *ComposIO* is not necessary. Only use it if you have tools from them.

   ```powershell
   # PowerShell
   $env:COMPOSIO_API_KEY = "your_composio_api_key"
   ```

   ```powershell
   # PowerShell
   $env:XAI_API_KEY= "your_xai_api_key"
   ```

   ```bash
   # Bash or Zsh (macOS Terminal)
   export COMPOSIO_API_KEY="your_composio_api_key"
   export XAI_API_KEY="your_xai_api_key"
   ```
4. ▶️ Run the CLI:

   If you set up environment variable in previous step, you only need `grok_cli`:

   ```bash
   grok_cli
   ```

   If you have not set up environment variable in previous step, you can use the following:

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
