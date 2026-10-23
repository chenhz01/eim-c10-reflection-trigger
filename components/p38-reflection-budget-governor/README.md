# P38 · reflection-budget-governor

> 机制簇：**反思触发** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
反思很贵，次数要封顶，防止无限反省。

**L1 · 机制本质**
计数超 cap 即 deny。

**L2 · 怎么用上**
govern(count, cap) → 'allow'/'deny'。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P38] ['allow', 'allow', 'allow', 'deny', 'deny']
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 长任务、易死循环/原地打转、需要「意识到自己卡住了」的 agent。 |
| **不该用** | 短任务（一次调用即可完成）；反思成本高于收益的链路。 |
| **常见误用** | 每步都反思——预算爆炸且引入自我怀疑式抖动。要的是「触发」不是「常开」。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P36` probing-reflection-trigger · `P37` stuck-detector · `P39` reflection-loop-breaker
- 本仓是 **P38 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P38-reflection-budget-governor/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P38 · reflection-budget-governor © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](NOTICE)。
