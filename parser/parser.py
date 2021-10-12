from typing import List

from .lexical_analysis import split_token
from . import parsed_result as pr


class LoadScriptParser:
    def __init__(self) -> None:
        pass

    def parse(self, scripts_rows: List[str]) -> pr.ParsedResult:
        deques_tokens = split_token(scripts_rows)
        return pr.create(deques_tokens)
