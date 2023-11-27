from pydantic import BaseModel

class FootballPlayer(BaseModel):
    Age: int
    MP: int
    Starts: int
    Min: float
    nineties: float
    Gls: int
    Ast: int
    GA: int
    GnoPK: int
    Pk: int
    PKatt: int
    CrdY: int
    CrdR: int
    xG: float
    npxG: float
    xAG: float
    npxGxAG: float
    PrgC: float
    PrgP: float
    PrgR: float
