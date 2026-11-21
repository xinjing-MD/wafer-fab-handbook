# 02 · SECS/GEM 状态机、E84 握手与报文编解码仿真 (`02_SECS_GEM状态机仿真`)

> 在晶圆厂 CIM 系统中，一台机台如果无法与 EAP（设备自动化程序）及 OHT（空中天车）通过标准协议对话，就只能停在昂贵的洁净室里等待人工手推车。本目录用纯 Python 还原 SEMI 核心自动化协议。

---

## 脚本清单与学习要点

| 脚本名 | 模拟协议与标准 | 运行可观察内容 |
| :--- | :--- | :--- |
| [e10_state_machine_sim.py](./e10_state_machine_sim.py) | SEMI E10（设备六态机） + SEMI E84（OHT-LP 并行光电握手） | 设备在 `PRD / SBY / ENG / SDT / UDT / NST` 间的切换逻辑、OEE 可用率统计以及天车交接 8 针脚 I/O 时序 |
| [secs2_sml_codec_sim.py](./secs2_sml_codec_sim.py) | SEMI E5 (SECS-II) + HSMS SML 报文树 (`L / A / U4 / B`) + E87 SlotMap | 自动序列化并打印 EAP 与 `LAM-ETCH-03` 之间的 `S1F1/S1F2` 在线心跳、`S2F41/S2F42 (PP-SELECT)` 远程选配方、`S6F11/S6F12` SlotMap 上报（24 片有片 `'2'` + 第 25 槽空槽 `'1'`） |

---

## 关联参考文档

- [SECS/GEM 与 GEM300 标准详解](../../06_天车与CIM系统/02_SECS_GEM与SEMI标准/笔记/01_SECS_GEM与GEM300标准详解.md)
- [晶圆厂 CIM 软件金字塔与 E84 闭环图 (SVG)](../../06_天车与CIM系统/02_SECS_GEM与SEMI标准/图解/晶圆厂CIM软件金字塔与E84闭环图.svg)
