from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

async def get_response_from_ai_agents(llm_model, query, allow_search, system_prompt):
    llm = ChatGroq(model=llm_model)

    tools = [TavilySearch(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools
    )

    user_input = "\n".join(query)

    state = {
        "messages": [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_input)
        ]
    }

    response = await agent.ainvoke(state)

    messages = response.get("messages", [])
    ai_messages = [m.content for m in messages if isinstance(m, AIMessage)]

    return ai_messages[-1] if ai_messages else ""
