# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P38 reflection-budget-governor — 反思触发

L0: 反思很贵，次数要封顶，防止无限反省。
L1: 计数超 cap 即 deny。
L2: govern(count, cap) → 'allow'/'deny'。
"""

def govern(count, cap=3):
    return "allow" if count < cap else "deny"

def demo():
    print("[P38]", [govern(i) for i in range(5)])


if __name__ == "__main__":
    demo()
