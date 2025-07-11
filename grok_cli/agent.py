from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from composio_langchain import ComposioToolSet, App

class GrokAgent:
    def __init__(self, api_key, model: str = "grok-4-0709", base_url: str = "https://api.x.ai/v1"):
        self.llm = ChatOpenAI(
            api_key=api_key,
            model=model,
            base_url=base_url,
            temperature=0.7,
            max_tokens=1000
        )
        self.composio_toolset = ComposioToolSet()
        self.tools = self.composio_toolset.get_tools(apps=[App.FILETOOL])
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI assistant with access to file tools. Use the tools when needed to help the user."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        self.agent = create_openai_functions_agent(self.llm, self.tools, self.prompt)
        self.agent_executor = AgentExecutor(
            agent=self.agent,
            tools=self.tools,
            memory=self.memory,
            verbose=False,  
            max_iterations=10
        )

    def chat(self, user_message):
        """Chat with the agent using LangChain's built-in tool calling"""
        try:
            response = self.agent_executor.invoke({"input": user_message})
            output = response.get("output", "Sorry, I couldn't generate a response.")
            print("Bot: ", output)  
            return output
        except Exception as e:
            if "rate_limit" in str(e).lower() or "429" in str(e):
                error_msg = "Rate limit exceeded. Please try again later."
                print(error_msg)
                return error_msg
            error_msg = f"An error occurred: {str(e)}"
            print(error_msg)
            return error_msg
