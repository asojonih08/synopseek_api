from pydantic import BaseModel, Field
from typing import Literal

class SearchRequest(BaseModel):
    query: str = Field(min_length=1, max_length=100, examples=["What is FastAPI?", "What are the best movies out this year?"])
    model: Literal["gpt-4o-mini", "gpt-4o", "o3-mini", "o1-mini"] = Field(..., examples=["gpt-4o-mini", "gpt-4o", "o3-mini", "o1-mini"])