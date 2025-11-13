from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from chat_svc.agent import agent
router = APIRouter(prefix="/api/chat", tags=["chat"])

class QueryRequest(BaseModel):
    query: str = "tìm cho tôi mã object type của máy nén khí"

class QueryResponse(BaseModel):
    query: str
    response: str
    status: str = "success"

def get_agent_response(query: str) -> str:
    """Execute agent with query and return response"""
    try:
        result = agent.invoke(
            {"messages": [{"role": "user", "content": query}]}
        )
        
        # Extract the final AI response
        messages = result.get("messages", [])
        if messages:
            # Get the last AIMessage which contains the final response
            for msg in reversed(messages):
                if hasattr(msg, 'content') and msg.content:
                    return msg.content
        
        # Fallback to output field
        return result.get("output", "No response generated")
    except Exception as e:
        return f"Error processing query: {str(e)}"


@router.post("/query", response_model=QueryResponse)
async def query_chatbot(request: QueryRequest):
    """
    Query the chatbot to find object type codes
    
    Example:
    {
        "query": "tìm cho tôi mã object type của máy nén khí"
    }
    """
    try:
        if not request.query or not request.query.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")
        
        response = get_agent_response(request.query)
        
        return QueryResponse(
            query=request.query,
            response=response,
            status="success"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
