from enum import Enum


class GameResult(Enum):
    WIN = "win"
    DRAW = "draw"
    LOSS = "loss"

def points_for_result(
    result: GameResult,
) -> int:
    pass
