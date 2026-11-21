# 半导体晶圆厂 4 阶段系统学习路线（16 周参考版）

> 可按个人每周投入时间灵活拉长或压缩；核心原则是**每个阶段必须有可提交进 GitHub 的产出物**（笔记、流程图或脚本），避免只看不练。

---

## Phase 1：筑基与全局视野（Week 1 - Week 3）

**对应目录**：`01_fundamentals_and_devices` + `02_fab_architecture_and_facilities`

- **Week 1：硅片与器件物理基础**
  - 掌握直拉法单晶硅（CZ）、300mm 硅片关键几何参数（直径、厚度、晶向、Notch）。
  - 理解 MOSFET 基本开关原理、亚阈值摆幅、短沟道效应为何推动结构演进。
- **Week 2：主流逻辑与存储器件结构**
  - 对比 Planar → FinFET → GAA Nanosheet → CFET 的栅控能力变化。
  - 搞懂 SRAM（6T）、DRAM（1T1C）、3D NAND（电荷俘获 + 多层堆叠）核心结构。
- **Week 3：现代 12 寸晶圆厂建筑与厂务系统**
  - 理解三明治垂直布局（Plenum → Cleanroom → Waffle Slab → Sub-Fab → Basement）与 Bay/Chase 格局。
  - 掌握 ISO 洁净等级、FFU 层流、超纯水（UPW）、特气/CDS 及 EHS 基础安全规范。
- **阶段产出**：提交 2~3 篇结构对比笔记 + 1 张自己整理的晶圆厂分层示意图。

---

## Phase 2：攻克七大核心单项工艺（Week 4 - Week 9）

**对应目录**：`03_unit_processes/01 ~ 07`

| 周次 | 工艺模块 | 重点攻克知识点 | 关键 KPI 指标 |
| :---: | :--- | :--- | :--- |
| Week 4 | **光刻** (`01_lithography`) | 瑞利判据、DUV/ArFi/EUV 光源与光路、Track 涂胶显影、OPC/多重曝光 | CD、DOF、Overlay、Throughput (WPH) |
| Week 5 | **刻蚀与清洗** (`02_etch_and_cleaning`) | CCP vs ICP 等离子体、各向异性机制、ALE；RCA SC-1/SC-2/DHF/SPM 清洗 | Etch Rate、Selectivity、Profile、Particle |
| Week 6 | **薄膜沉积** (`03_thin_film_deposition`) | LPCVD/PECVD/HDPCVD、ALD 自限制反应、PVD 磁控溅射、Epi 外延 | Step Coverage、Thickness Uniformity、Stress |
| Week 7 | **热处理与注入** (`04_thermal_and_ion_implant`) | Deal-Grove 氧化模型、RTP/LSA 退火、离子注入能量/剂量/沟道效应 | $R_s$ 方阻、结深 $X_j$、热预算 (Thermal Budget) |
| Week 8 | **CMP 与金属化** (`05_cmp` + `06_metallization`) | Preston 公式、Slurry/Pad；Cu 双大马士革、Barrier/Seed、ECP 电镀 | MRR、WIWNU、Dishing & Erosion、Void |
| Week 9 | **量测与检测** (`07_metrology_and_inspection`) | CD-SEM、椭偏仪/OCD、Overlay 量测、明/暗场缺陷检测、TEM/FIB | Precision/TMU、Sensitivity、Capture Rate |

- **阶段产出**：7 个子目录各至少沉淀 1~2 篇结构化笔记，并补全 `external_links.md`。

---

## Phase 3：工艺整合与软硬件联动（Week 10 - Week 13）

**对应目录**：`04_process_integration_and_nodes` + `05_equipment_and_subsystems` + `06_fab_automation_and_cim`

- **Week 10：CMOS 全流程串联与重入式（Re-entrant）逻辑**
  - 把七大工艺串成 FEOL（STI → 井 → 栅极 → 源漏）→ MOL（接触孔）→ BEOL（多层金属互连）。
  - 理解晶圆为什么会在光刻/刻蚀/薄膜之间循环往返数百至上千道工序。
- **Week 11：先进节点与前道-封装衔接**
  - 梳理 28nm → FinFET → GAA → 背面供电（BSPDN）的演进痛点；了解 TSV、RDL 与 Hybrid Bonding 如何衔接 CoWoS/HBM。
- **Week 12：核心设备架构与卡脖子零部件**
  - 拆解 Cluster Tool（EFEM + Load Port + Transfer Chamber + Process Module）。
  - 了解 RF 电源/匹配器、ESC 静电吸盘、MFC、干泵/分子泵的作用及国内外主流设备厂商。
- **Week 13：天车物流（AMHS）与 CIM/MES 软件栈**
  - 理解 FOUP 载具、OHT 天车与 Stocker 如何搬运晶圆；看懂 SECS/GEM、E84/E87/E90/E94 以及 MES/EAP/RTD/APC 的分工。
- **阶段产出**：用 Mermaid 绘制 CMOS 全流程与 CIM 数据流图；运行并理解 `E10/E84` 仿真脚本。

---

## Phase 4：良率工程、运营分析与实战（Week 14 - Week 16）

**对应目录**：`07_yield_spc_and_failure_analysis` + `08_fab_operations_and_industry` + `09_labs_code_and_visuals`

- **Week 14：良率数学模型、SPC 与 FDC**
  - 掌握 Line Yield vs Die Yield，对比 Poisson / Murphy / Seeds / 负二项模型；掌握 $C_p/C_{pk}$ 与判异规则。
- **Week 15：WAT、CP Wafer Map 与失效分析（FA）**
  - 区分 inline 量测、WAT、CP、FT 的测试对象；识别典型 Wafer Map 缺陷分布模式并理解 EFA/PFA（EMMI/OBIRCH/FIB/TEM）。
- **Week 16：晶圆厂成本经济账与材料供应链复盘**
  - 建立晶圆单片成本直觉（折旧、良率、Gross Die per Wafer、Cycle Time 与瓶颈机台管理）；整理个人术语词典与求职/项目作品集。
- **阶段产出**：运行 Python 良率/SPC 脚本并尝试修改参数做敏感性分析；完成个人求职/研究专题总结。
