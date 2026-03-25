from services.gemini_service import get_gemini_response

def handle(text: str) -> str:
    prompt = f"""
    You are a Summarizer Agent. Your job is to extract the key points and provide a 
    concise, easy-to-read summary of the following text:
    
    TEXT:
    {text}
    """
    return get_gemini_response(prompt)