# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P37 stuck-detector — 反思触发

L0: AI 原地打转就提醒它换个思路。
L1: 检测最近 window 步状态是否重复。
L2: stuck(history, window) → bool。
"""

def stuck(history, window=3):
    if len(history) < window: return False
    tail = history[-window:]
    return len(set(map(str, tail))) < window

def demo():
    print("[P37]", stuck(["a","b","a","b","a"]), stuck(["a","b","c"]))


if __name__ == "__main__":
    demo()
