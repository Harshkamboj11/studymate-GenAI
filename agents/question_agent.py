from services.gemini_service import get_gemini_response

def handle(text: str) -> str:
    prompt = f"""
    You are a Quiz Master Agent. Your job is to generate 3 to 5 thoughtful quiz questions 
    based on the following text to test the user's understanding. Provide the answers 
    at the very end.
    
    TEXT:
    {text}
    """
    return get_gemini_response(prompt)