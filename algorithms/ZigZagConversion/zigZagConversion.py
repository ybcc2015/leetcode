# -*- coding: utf-8 -*-
"""
@Author: Yi Bin
@Date: 2019/8/22
@Source: https://leetcode.com/problems/zigzag-conversion/
@Description:

    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
    (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   row_index
    A P L S I I G
    Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"

    Example 1:
        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"

    Example 2:
        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:
            P     I    row_index
            A   L S  I G
            Y A   H R
            P     I
"""


def convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s):
        return s
    
    rows = [""] * num_rows
    row_index = 0
    for c in s:
        rows[row_index] += c
        if row_index == 0:
            go_down = True
        if row_index == num_rows - 1:
            go_down = False
        row_index += 1 if go_down else -1

    return "".join(rows)


if __name__ == '__main__':
    test = [("PAYPALISHIRING", 3), ("PAYPALISHIRING", 4)]
    for _input in test:
        print(convert(*_input))
