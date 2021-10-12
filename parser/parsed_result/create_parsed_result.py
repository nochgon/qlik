from typing import Deque, Tuple
import traceback

from .parsed_result import ParsedResult


def create(deques_tokens: Deque[Tuple[int, Deque[str]]]) -> Union(ParsedResult, None):
    try:
        return ParsedResult(deques_tokens)
    except Exception as e:
        traceback.format_exception_only(type(e), e)
        return
