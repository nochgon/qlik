from typing import Deque, Tuple, Optional
import traceback

from .parsed_result import ParsedResult


def create(deques_tokens: Deque[Tuple[int, Deque[str]]]
           ) -> Optional[ParsedResult]:
    try:
        return ParsedResult(deques_tokens)
    except Exception as e:
        traceback.format_exception_only(type(e), e)
        return
