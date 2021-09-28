from typing import List
from .preprocess import split_token


class LoadScriptParser:
    def __init__(self) -> None:
        pass

    def parse(self, scripts_rows: List[str]) -> str:
        deque_tokens = split_token(scripts_rows)
        pass
