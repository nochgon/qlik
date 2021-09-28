from collections import deque
from typing import Deque, List
import re


def split_token(scripts_rows: List[str]) -> Deque[str]:
    """
    ロードしたスクリプトのリストをトークンに分割する。
    　・コメントの除去もここで行う。
    　・スプリット対象: ',' or '(', or ')' or スペース or 改行
    　・文字のスプリット対象はトークンに含まれる。
    """
    # 正規表現の準備
    re_comment_block = re.compile(r'/\*.*?\*/')
    re_comment_line = re.compile(r'//.*?\n')
    re_element_block = re.compile(r'\[.*?\]')
    re_split = re.compile(r'[,\s\n]')

    # scripts_rowsを一つの文字列に統合。
    # 改行部分には改行コードを挿入
    script = '\n'.join(scripts_rows)

    # コメントを削除
    script = re_comment_line.sub('', script)
    script = re_comment_block.sub('', script)

    # トークン化
    deque_result: Deque[str] = deque()
    for script in scripts_rows:
        # [~]は列名のブロックになり、スプリット対象の例外扱いとなるので、
        # まずはそこのところを分割、抽出
        index_start = 0
        script_raw = script
        for re_result_split in re_element_block.finditer(script):
            # 列ブロックより前をsplitし格納
            script_target = script[index_start:re_result_split.start()]
            deque_result.extend(split_by_re(script_target, re_split))

            # ブロック部分はそのまま格納
            deque_result.append(re_result_split.group())

            # script, index_startを更新
            script = script_raw[re_result_split.end()]
            index_start = re_result_split.end()

        # ブロックが無いscript or 残ったscriptをsplitし格納
        deque_result.extend(split_by_re(script, re_split))
        deque_result.append('\n')
    deque_result.pop()  # 最後に追加した改行コードを除去
    return deque_result


def split_by_re(script: str, re_split: re.Pattern) -> List[str]:
    index_start = 0
    script_raw = script
    list_result: List[str] = []
    for re_result_split in re_split.finditer(script):
        # スプリット対象より前のものを格納
        list_result.append(script[index_start:re_result_split.start()])
        # スプリット対象を格納
        list_result.append(re_result_split.group())
        # スプリット対象より後の文字列でscriptを更新
        script = script_raw[re_result_split.end():]

    if len(script):
        list_result.append(script)
    return list_result
