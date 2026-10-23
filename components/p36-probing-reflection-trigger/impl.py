# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P36 probing-reflection-trigger — 反思触发

L0: 不是每次都反思，而是先探一探'是不是该反思了'。
L1: 多信号探针：低置信/高冲突/无进展 → 触发反思。
L2: should(signals) → (bool, reasons)。
"""

def should(signals):
    reasons = []
    if signals.get("confidence", 1) < 0.4: reasons.append("low_conf")
    if signals.get("conflict", 0) > 0.5: reasons.append("conflict")
    if signals.get("progress", 1) == 0: reasons.append("no_progress")
    return bool(reasons), reasons

def demo():
    print("[P36]", should({"confidence":0.3,"conflict":0.1}), should({"confidence":0.9}))


if __name__ == "__main__":
    demo()
