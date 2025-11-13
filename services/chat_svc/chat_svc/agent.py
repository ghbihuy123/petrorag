import os
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from chat_svc.tools.find_object_info import find_object_info
from chat_svc.settings import common_config

os.environ['OPENAI_API_KEY'] = common_config.openai_key

# Initialize the cheapest OpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",  # Cheapest OpenAI model
    temperature=0,
)

# Define tools
tools = [find_object_info]

# Create the agent
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant",
)

# # Run the agent
# response = agent.invoke(
#     {"messages": [{"role": "user", "content": "tìm cho tôi mã object type của máy khí nen"}]}
# )

