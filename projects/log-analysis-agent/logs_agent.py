from strands import Agent  # Importing Agentic AI Framework
from strands_tools import file_read
from strands.models.ollama import OllamaModel

SYSTEM_PROMPT = """
You are a log analysis agent.
You are excellent is reading and understanding logs.
You can deduce results in short and crisp manner.
You are helpful and use a DevOps mindset in Log analysis and root cause analysis.
You won't hallucinate and suggest new changes.
You will not engage in any production actions, but suggest changes and ideas to DevOps Engineers.
"""

ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="llama3.2",  # Specify which model to use
)


agent = Agent(
    system_prompt=SYSTEM_PROMPT, model=ollama_model, tools=[file_read]
)  # Calling Bedrock LLMs

agent(
    "Detect how many times the INFO, WARNING, ERROR occurs and return the counts only from app.log using only read mode"
)
