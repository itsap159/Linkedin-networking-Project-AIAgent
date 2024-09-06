from typing import List, Dict, Any

from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")
    ice_breakers: List[str] = Field(description="Couple of ice breakers to talk with the person")
    topics_of_interest: List[str] = Field(description="Topics of interest of the person")
    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts,
                "ice_breakers":self.ice_breakers,
                "topics_of_interest":self.topics_of_interest}


# class IceBreaker(BaseModel):
#     ice_breakers: List[str] = Field(description="ice breaker list")

#     def to_dict(self) -> Dict[str, Any]:
#         return {"ice_breakers": self.ice_breakers}


# class TopicOfInterest(BaseModel):
#     topics_of_interest: List[str] = Field(
#         description="topic that might interest the person"
#     )

#     def to_dict(self) -> Dict[str, Any]:
#         return {"topics_of_interest": self.topics_of_interest}


summary_parser = PydanticOutputParser(pydantic_object=Summary)
# ice_breaker_parser = PydanticOutputParser(pydantic_object=IceBreaker)
# topics_of_interest_parser = PydanticOutputParser(pydantic_object=TopicOfInterest)

