# 01 · Python 良率、SPC 判异与产线运营仿真 (`01_Python良率与SPC仿真`)

> 本目录全部 Python 脚本均基于**纯 Python 3 标准库**编写，零第三方包依赖，适合直接运行并结合参数修改做工程敏感性分析。

---

## 脚本与数据清单

| 文件名 | 模拟对象与核心算法 | 关联理论模块 |
| :--- | :--- | :--- |
| [yield_and_dpw_calculator.py](./yield_and_dpw_calculator.py) | 300mm Gross Die 几何切分 + Poisson / Murphy / Seeds / Negative Binomial 良率对比 | [07 · 良率层级与四大模型](../../07_良率SPC与FA/01_良率模型与缺陷密度/笔记/01_良率层级与四大数学模型对比.md) |
| [spc_cpk_demo.py](./spc_cpk_demo.py) | $C_p / C_{pk}$ 计算 + Western Electric Rule 1~4 判异报警器 | [07 · 良率SPC与FA](../../07_良率SPC与FA/README.md) |
| [wafer_map_pattern_simulator.py](./wafer_map_pattern_simulator.py) | Edge Ring / Center Bullseye / Scratch / Reticle Shot 四大 CP 图谱模拟与 ASCII 可视化 | [07 · WAT/CP 与 FA](../../07_良率SPC与FA/03_WAT_CP与失效分析FA/笔记/01_WAT_CP晶圆分布图与失效分析FA.md) |
| [process_physics_simulator.py](./process_physics_simulator.py) | Deal-Grove 热氧化、瑞利光刻窗口（CD/DOF）与 LSS 高斯离子注入深度分布 $N(x)$ | [03 · 七大核心工艺](../../03_七大核心工艺/README.md) |
| [apc_r2r_ewma_simulator.py](./apc_r2r_ewma_simulator.py) | Double-EWMA（Butler & Stefani）闭环 APC 与无控制开环漂移 + PM 阶跃对比 | [06 · CIM/APC 与自动化](../../06_天车与CIM系统/README.md) |
| [fab_wip_littles_law_sim.py](./fab_wip_littles_law_sim.py) | Kingman G/G/m 排队论与 Little's Law Operating Curve（85%~96% 利用率瓶颈对比） | [08 · 运营与产业链](../../08_运营与产业链/README.md) |
| [sample_datasets/lot_cd_metrology.csv](./sample_datasets/lot_cd_metrology.csv) | 18 组合成 `GATE_AEI` 量测数据集（可用于练习双腔配对与漂移诊断） | [09 · 实战练习数据集](#合成数据集分析提示) |

---

## 合成数据集分析提示

打开 [sample_datasets/lot_cd_metrology.csv](./sample_datasets/lot_cd_metrology.csv)，里面刻意埋入了三类经典产线异常现象供你用 Python / Excel 做诊断练习：
1. **双腔失配（Chamber Mismatch / WECO Rule 4 类特征）**：奇数 Lot 固定走 `ETCH-01 / PM-A`（初期 CD 约 `19.92~19.98 nm`），偶数 Lot 固定走 `PM-B`（初期 CD 即高达 `20.41~20.46 nm`），同一台机台不同腔室存在约 `+0.48 nm` 系统性偏置。
2. **随批次累计的腔壁漂移（Chamber Drift）**：随着聚合物沉积与腔内环境老化，两条腔室各自均呈缓慢上升漂移趋势（到第 15~16 批 `PM-A` 升至 `20.15 nm`，`PM-B` 升至 `20.89 nm`），需要 R2R Double-EWMA APC 自动收紧刻蚀时间进行补偿。
3. **末批颗粒爆点（Defect Spike）**：`LOT2026_016` 在 `PM-B` 上 `defect_count` 突然从常规的 `2~8` 颗跳变到 `19` 颗，提示应立即 Hold 批次并排查 `PM-B` 腔室剥落（Peeling）或 ESC 背面氦气冷却异常。
