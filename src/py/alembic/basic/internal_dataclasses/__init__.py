from datetime import datetime
from typing import Optional
from sqlmodel import Field, Index, SQLModel

class Member(SQLModel, table=True):
    __tablename__ = "member"

    id: Optional[int] = Field(None, primary_key=True)
    name: str = Field(index=True)
    # created_at: datetime = Field(default_factory=datetime.utcnow(), nullable=False)
