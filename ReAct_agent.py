import json
from typing import Sequence, List

from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
from llama_index.core.tools import BaseTool, FunctionTool

import nest_asyncio

nest_asyncio.apply()

llm = OpenAI(model="gpt-3.5-turbo")


from llama_index.core.agent import AgentRunner
from llama_index.agent.openai import OpenAIAgentWorker, OpenAIAgent

# Option 1
agent = OpenAIAgent.from_tools(tools, llm=llm, verbose=True)




# # Option 2
# openai_step_engine = OpenAIAgentWorker.from_tools(tools, llm=llm, verbose=True)
# agent = AgentRunner(openai_step_engine)

#agent.chat("こんにちは！")


tasks = agent.list_tasks()
print(len(tasks))


task_state = tasks[-1]
task_state.task.input