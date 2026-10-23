# C10 · Reflection Trigger

> **机制簇**：反思触发 ｜ **家族**：EIM-1.0（Emergent Intelligence Mechanisms）｜ **组件数**：4
>
> 本仓是 EIM-1.0 的**簇级入口**：一个机制簇 + 该簇全部可运行参考实现。
> 单组件仓与旗舰合集见文末「家族」段。

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
让 AI 卡住时知道「我该停下来想想」，而不是原地打转十分钟。

**L1 · 机制本质**
用停滞信号（动作重复、无进展、熵塌缩）触发反思，并设反思预算上限防止无限自省。

**L2 · 怎么用上**
stuck-detector 检测停滞；probe-generator 生成诊断问题；reflection-budget 控次数。

## 30 秒跑起来

```bash
git clone https://github.com/chenhz01/eim-c10-reflection-trigger.git && cd eim-c10-reflection-trigger
python run_all.py        # 跑全簇 4 个组件，逐个 selftest + 输出快照比对
```

单个组件也可独立跑：

```bash
python components/p36-probing-reflection-trigger/impl.py        # 看 demo 输出
python components/p36-probing-reflection-trigger/selftest.py    # 断言 + 与 golden_output.txt 比对
```

零第三方依赖，Python 3.9+ 即可。

## 本簇组件

| ID | 组件 | 机制本质 | 目录 |
|---|---|---|---|
| `P36` | probing-reflection-trigger | 多信号探针：低置信/高冲突/无进展 → 触发反思。 | `components/p36-probing-reflection-trigger/` |
| `P37` | stuck-detector | 检测最近 window 步状态是否重复。 | `components/p37-stuck-detector/` |
| `P38` | reflection-budget-governor | 计数超 cap 即 deny。 | `components/p38-reflection-budget-governor/` |
| `P39` | reflection-loop-breaker | 检测状态序列中的循环 (a->b->a)，返回跳出建议。 | `components/p39-reflection-loop-breaker/` |

## 该用 / 不该用 / 常见误用

**该用**
长任务智能体、调试循环、自动化流水线的卡死处置。

**不该用**
单轮问答；有严格时延上限且无法中断的路径。

**常见误用（这条最重要）**
每一步都反思。反思成本可能高于收益——必须由信号触发，而不是定时触发。

## 这份代码是什么、不是什么

- **是**：可直接运行、带断言与输出快照的最小参考实现。每个 `impl.py` 都能单独跑出 demo，`selftest.py` 会在行为漂移时报错。
- **不是**：生产级库。缺少配置化、并发安全、错误恢复、性能优化。**生产使用请按自己的约束扩展**，不要原样上生产。
- **诚实边界**：本簇解决的是「机制怎么落地」这个问题，不承诺在任何数据分布下都优于基线。基准数据请自测。

## 家族

- **旗舰合集（55 组件）**：https://github.com/chenhz01/emergent-mechanisms
- **单组件仓**：`eim-p01-…` ~ `eim-p55-…`，与 `components/` 内文件一致，任一处修复会双向同步。

## 许可（双许可）

- **代码**：**Apache-2.0**（Apache License 2.0）— 见 [LICENSE](LICENSE)
- **规范/文档**：**CC BY 4.0**（Creative Commons Attribution 4.0 International）— 见 [LICENSE-SPEC](LICENSE-SPEC)

声明符合 EIM-1.0 规范时须署名：

```
EIM-1.0 · C10 · Reflection Trigger © 2026 chenhz01, CC BY 4.0
```

详见 [NOTICE](NOTICE)。
