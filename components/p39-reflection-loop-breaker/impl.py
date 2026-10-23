# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P39 reflection-loop-breaker — 反思触发

L0: 如果反思本身绕成一个圈，这个工具负责一脚踹出去。
L1: 检测状态序列中的循环 (a->b->a)，返回跳出建议。
L2: break_loop(seq) → bool。
"""

def break_loop(seq):
    for size in range(1, len(seq)//2 + 1):
        if seq[-2*size:-size] == seq[-size:]:
            return True
    return False

def demo():
    print("[P39]", break_loop(["a","b","a","b"]), break_loop(["a","b","c"]))


if __name__ == "__main__":
    demo()
