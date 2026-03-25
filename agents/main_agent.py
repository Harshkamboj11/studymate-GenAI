from agents import summarizer_agent, eli5_agent, question_agent

def process_request(user_input: str) -> dict:
    """
    Routes the user input to the appropriate agent based on keywords.
    """
    lower_input = user_input.lower()

    if "summarize" in lower_input:
        agent_name = "Summarizer Agent"
        response = summarizer_agent.handle(user_input)
        
    elif "question" in lower_input or "quiz" in lower_input:
        agent_name = "Question Generator Agent"
        response = question_agent.handle(user_input)
        
    elif "explain" in lower_input:
        agent_name = "Explain Agent (ELI5)"
        response = eli5_agent.handle(user_input)
        
    else:
        # Default fallback
        agent_name = "Explain Agent (ELI5)"
        response = eli5_agent.handle(user_input)

    return {
        "agent": agent_name,
        "response": response
    }