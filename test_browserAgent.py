import os
from dotenv import load_dotenv
import openai
#import llama_index 
# import dotenv

from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.llms import ChatMessage
from llama_index.core.tools import BaseTool, FunctionTool


load_dotenv(dotenv_path="/Users/markirwin/AIfes_hackathon_browser_agent/.gitignore/.env")
openai.api_key = os.environ["OPENAI_API_KEY"]


#headers = {"Authorization": "Bearer "}


def multiply(a: int, b: int) -> int:
    """Multiply two integers and returns the result integer"""
    return a * b


multiply_tool = FunctionTool.from_defaults(fn=multiply)


def click():
    """clicks button"""
    import subprocess
    command = "pytest test_click.py --headed --slowmo 1000"  
    subprocess.run(command, shell=True)


click_tool = FunctionTool.from_defaults(fn=click)

def login():
    """login"""
    import subprocess
    command = "pytest test_login.py --headed --slowmo 1000"  
    subprocess.run(command, shell=True)


login_tool = FunctionTool.from_defaults(fn=login)

def press_button():
    """press_button"""
    import subprocess
    command = "pytest test_press_button.py --headed --slowmo 1000"  
    subprocess.run(command, shell=True)


press_button = FunctionTool.from_defaults(fn=press_button)


def shibuya_sushi_reserve_tabelog():
    """Reserves tables for sushi in shibuya"""
    import subprocess
    command = "pytest test_shibuya_sushi_tabelog.py --headed --slowmo 1000"  
    subprocess.run(command, shell=True)

shibuya_sushi_tabelog_tool = FunctionTool.from_defaults(fn=shibuya_sushi_reserve_tabelog)



llm = OpenAI(model="gpt-4") #gpt-4 #gpt-3.5-turbo-instruct
agent = ReActAgent.from_tools([multiply_tool, add_tool], llm=llm, verbose=True)

# response = agent.chat("渋谷の寿司を食べログで予約したい")
# response = agent.chat("I want to reserve a table for sushi in shibuya")
agent.chat("what is 101-89+88")







# # Only output the answer. Make sure to delete the ReAct code above ! 
# response_gen = agent.stream_chat("What is 20+2*4? Calculate step by step")
# response_gen.print_response_stream()

# # View the system prompts and shit for debugging !

# prompt_dict = agent.get_prompts()
# for k, v in prompt_dict.items():
#     print(f"Prompt: {k}\n\nValue: {v.template}")


# # customizing the pompts !!!
# from llama_index.core import PromptTemplate

# react_system_header_str = """\

# You are designed to help with a variety of tasks, from answering questions \
#     to providing summaries to other types of analyses.

# ## Tools
# You have access to a wide variety of tools. You are responsible for using
# the tools in any sequence you deem appropriate to complete the task at hand.
# This may require breaking the task into subtasks and using different tools
# to complete each subtask.

# You have access to the following tools:
# {tool_desc}

# ## Output Format
# To answer the question, please use the following format.

# ```
# Thought: I need to use a tool to help me answer the question.
# Action: tool name (one of {tool_names}) if using a tool.
# Action Input: the input to the tool, in a JSON format representing the kwargs (e.g. {{"input": "hello world", "num_beams": 5}})
# ```

# Please ALWAYS start with a Thought.

# Please use a valid JSON format for the Action Input. Do NOT do this {{'input': 'hello world', 'num_beams': 5}}.

# If this format is used, the user will respond in the following format:

# ```
# Observation: tool response
# ```

# You should keep repeating the above format until you have enough information
# to answer the question without using any more tools. At that point, you MUST respond
# in the one of the following two formats:

# ```
# Thought: I can answer without using any more tools.
# Answer: [your answer here]
# ```

# ```
# Thought: I cannot answer the question with the provided tools.
# Answer: Sorry, I cannot answer your query.
# ```

# ## Additional Rules
# - The answer MUST contain a sequence of bullet points that explain how you arrived at the answer. This can include aspects of the previous conversation history.
# - You MUST obey the function signature of each tool. Do NOT pass in no arguments if the function expects arguments.

# ## Current Conversation
# Below is the current conversation consisting of interleaving human and assistant messages.

# """
# react_system_prompt = PromptTemplate(react_system_header_str)


# agent.get_prompts()

# agent.update_prompts({"agent_worker:system_prompt": react_system_prompt})

# agent.reset()
# response = agent.chat("What is 5+3+2")
# print(response)








# そのほか terminal 上でのメモ
# USE python3 !!!! python3 test_browserAgent.py
# use pip3 !!!
# Below is the shit that fixed my crcular import module error
# pip3 uninstall llama-index
# pip3 install llama-index --upgrade --no-cache-dir --force-reinstall