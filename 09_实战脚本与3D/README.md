# 09 · 实战代码、仿真脚本与三维可视化资产 (`09_实战脚本与3D`)

> “光背公式不够，亲手跑一遍工艺物理仿真、R2R 反馈控制、Little's Law 排队曲线、SECS-II 报文与三维空间标高模型，才能真正建立产线工程直觉。”

本模块全部 Python 脚本均**零第三方依赖**（仅使用 Python 3 标准库 `math` / `random` / `statistics` / `csv` / `dataclasses`），可直接本地运行；三维 HTML5 场景内置于单文件内，下载或克隆后用任意现代浏览器即可交互旋转预览。

---

## 模块结构总览

| 子目录 | 核心资产与工程能力 | 推荐实践任务 |
| :--- | :--- | :--- |
| [01_Python良率与SPC仿真](./01_Python良率与SPC仿真/README.md) | 6 个零依赖工程仿真脚本 + 1 份合成分腔量测 CSV 数据集 | 运行 R2R Double-EWMA 对比开环漂移、用 Kingman 公式算瓶颈排队爆炸点 |
| [02_SECS_GEM状态机仿真](./02_SECS_GEM状态机仿真/README.md) | SEMI E10 六态机、E84 OHT-LP 光通信握手、SECS-II/HSMS SML 编解码器 | 追踪 EAP 与 Etch 机台间 `S1F1`、`S2F41 (PP-SELECT)`、`S6F11` 完整报文 |
| [03_工艺流程Mermaid图](./03_工艺流程Mermaid图/README.md) | 3 套可直接在 GitHub 渲染的高清工程流程图与异常排错决策树 | 对比 28nm CMOS/CIM 闭环、2nm GAA+BSPDN 与 OOC 排错决策树 |
| [04_三维建模与视觉参考](./04_三维建模与视觉参考/README.md) | 7 份 300mm Fab 三维建模专著 + Blender `bpy` 参数化脚本 + Three.js 交互式 3D 洁净室预览 | 浏览器打开 `08_交互式3D洁净室CleanBay结构预览.html`，切换 589nm 黄光与 OHT 巡航 |

---

## 文件清单直达

### 1. `01_Python良率与SPC仿真/`（工程计算、SPC 与产线 IE 仿真）
- [yield_and_dpw_calculator.py](./01_Python良率与SPC仿真/yield_and_dpw_calculator.py) —— 300mm 晶圆 Gross Die 几何排布计算 + 四大良率模型对比（Poisson / Murphy / Seeds / 负二项）
- [spc_cpk_demo.py](./01_Python良率与SPC仿真/spc_cpk_demo.py) —— SPC $C_p / C_{pk}$ 计算 + Western Electric Rule 1~4 判异检查器
- [wafer_map_pattern_simulator.py](./01_Python良率与SPC仿真/wafer_map_pattern_simulator.py) —— CP Wafer Map 四大典型失效图谱模拟（边缘环 / 中心靶心 / 划痕 / 光罩周期重复点）与根因提示
- [process_physics_simulator.py](./01_Python良率与SPC仿真/process_physics_simulator.py) —— 核心单元工艺物理模型三合一：Deal-Grove 热氧化动力学、瑞利公式（KrF/ArF/ArFi/EUV/High-NA EUV 的 CD 与 DOF 对比）、LSS 高斯离子注入分布 $N(x)$ 与结深 $X_j$ 估算
- [apc_r2r_ewma_simulator.py](./01_Python良率与SPC仿真/apc_r2r_ewma_simulator.py) —— 双权重 EWMA（Butler & Stefani）Run-to-Run 先进过程控制仿真，演示机台线性漂移与 Lot #25 PM 阶跃扰动下的闭环稳态误差抑制
- [fab_wip_littles_law_sim.py](./01_Python良率与SPC仿真/fab_wip_littles_law_sim.py) —— 基于 Kingman 排队公式（G/G/m）与 Little's Law 的晶圆厂运作曲线（Operating Curve），对比高波动线与精益产线在 85%~96% 利用率下的 X-Factor 指数膨胀
- [sample_datasets/lot_cd_metrology.csv](./01_Python良率与SPC仿真/sample_datasets/lot_cd_metrology.csv) —— 18 组合成 `GATE_AEI` 量测实战数据集（含 `PM-A` / `PM-B` 双腔线宽失配、随时间漂移及 `LOT2026_016` 颗粒骤增案例）

### 2. `02_SECS_GEM状态机仿真/`（CIM / EAP / AMHS 自动化）
- [e10_state_machine_sim.py](./02_SECS_GEM状态机仿真/e10_state_machine_sim.py) —— SEMI E10 设备六态机与 SEMI E84 OHT-LoadPort 交接握手模拟
- [secs2_sml_codec_sim.py](./02_SECS_GEM状态机仿真/secs2_sml_codec_sim.py) —— SEMI E5 (SECS-II) 树状数据结构（`L / A / U4 / B`）与 SML 文本编解码演示，覆盖 `S1F1/S1F2`、`S2F41/S2F42 (PP-SELECT)` 与 GEM300 E87 `S6F11/S6F12` 槽位图上报

### 3. `03_工艺流程Mermaid图/`（流程图与故障树）
- [01_CMOS工艺与CIM数据闭环Mermaid图.md](./03_工艺流程Mermaid图/01_CMOS工艺与CIM数据闭环Mermaid图.md) —— 经典 CMOS 全流程与 CIM 数据闭环 Mermaid 图
- [02_GAA纳米片与背面供电工艺流程Mermaid图.md](./03_工艺流程Mermaid图/02_GAA纳米片与背面供电工艺流程Mermaid图.md) —— 3nm/2nm GAA 纳米片沟道释放与背面供电（BSPDN / PowerVia）双面加工流程图
- [03_Fab厂务动力与OOC异常排错决策树Mermaid图.md](./03_工艺流程Mermaid图/03_Fab厂务动力与OOC异常排错决策树Mermaid图.md) —— Utility/Cleanroom/Sub-Fab 水电气化尾气闭环与产线 OOC（失控报警）分流排查决策树

### 4. `04_三维建模与视觉参考/`（数字孪生、Blender 与 WebGL 3D）
- [README.md](./04_三维建模与视觉参考/README.md) —— 现代晶圆厂三维建模与科普可视化全套专著索引（含建筑、9 大机台、运动学、Blender 着色节点规范）
- [07_Blender_bpy_300mm晶圆厂标准件生成脚本.py](./04_三维建模与视觉参考/07_Blender_bpy_300mm晶圆厂标准件生成脚本.py) —— Blender 4.x/5.x `bpy` 自动化脚本，1:1 公制单位生成 300mm 晶圆、25 片装 10mm Pitch FOUP、Z=900mm Load Port、600×600mm 架高地板与 Z=3.50m OHT 天轨
- [08_交互式3D洁净室CleanBay结构预览.html](./04_三维建模与视觉参考/08_交互式3D洁净室CleanBay结构预览.html) —— Three.js（v0.170.0）单文件交互式 3D Clean Bay 与 Cluster Tool（EFEM → LoadLock → VTM → 4×PM + OHT 天车）模型；点击 GitHub 查看源码，克隆到本地双击即可在浏览器体验

---

## 本地一键验证命令

```bash
# 在仓库根目录 wafer-fab-handbook 下执行
python 09_实战脚本与3D/01_Python良率与SPC仿真/yield_and_dpw_calculator.py
python 09_实战脚本与3D/01_Python良率与SPC仿真/spc_cpk_demo.py
python 09_实战脚本与3D/01_Python良率与SPC仿真/wafer_map_pattern_simulator.py
python 09_实战脚本与3D/01_Python良率与SPC仿真/process_physics_simulator.py
python 09_实战脚本与3D/01_Python良率与SPC仿真/apc_r2r_ewma_simulator.py
python 09_实战脚本与3D/01_Python良率与SPC仿真/fab_wip_littles_law_sim.py
python 09_实战脚本与3D/02_SECS_GEM状态机仿真/e10_state_machine_sim.py
python 09_实战脚本与3D/02_SECS_GEM状态机仿真/secs2_sml_codec_sim.py
```
