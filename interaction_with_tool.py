def search_tool(query):
    return f"Search results for {query}"

def interaction(user_input):
    tool_result = search_tool(user_input)
    return f"Final answer using {tool_result}"


print(interaction("AI agent frameworks"))
