from enum import Enum


class GameResult(Enum):
    WIN = "win"
    DRAW = "draw"
    LOSS = "loss"

def points_for_result(
    result: GameResult,
) -> int:
    if result == GameResult.WIN:
        return 3
    if result == GameResult.DRAW:
        return 1
    return 0
