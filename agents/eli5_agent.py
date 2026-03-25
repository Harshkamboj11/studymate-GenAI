from services.gemini_service import get_gemini_response

def handle(text: str) -> str:
    prompt = f"""
    You are an Expert Teacher Agent. Your job is to explain the following text or concept 
    simply, as if you were speaking to a 5-year-old (ELI5). Use simple analogies.
    
    TEXT:
    {text}
    """
    return get_gemini_response(prompt)