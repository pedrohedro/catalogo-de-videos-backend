from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional

@dataclass() #init, repr, equal
class Category:
    
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now()
     )
    
