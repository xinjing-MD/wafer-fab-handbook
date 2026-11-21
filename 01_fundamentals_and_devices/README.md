# 01 · 半导体基础、硅片制备与核心器件 (`01_fundamentals_and_devices`)

本模块建立进入晶圆厂前的底层认知：**“晶圆厂到底在硅片上制造什么结构，以及物理极限在哪里？”**

## 目录内容
- `01_crystal_growth_and_wafer/` —— CZ/FZ 单晶生长、300mm 硅片标准、Epi 外延、SOI
- `02_semiconductor_physics/` —— 能带理论、载流子漂移扩散、PN 结/MOS 电容 C-V 特性、短沟道效应（SCE）与漏电
- `03_logic_devices/` —— Planar MOSFET → FinFET → GAA → CFET 演进
- `04_memory_and_specialty/` —— SRAM、DRAM、3D NAND、CIS 与 SiC/GaN 功率器件

## 学习 Checklist
- [x] [CZ 单晶与 300mm 硅片关键工程参数](./01_crystal_growth_and_wafer/notes/01_cz_silicon_and_wafer_specs.md)
  - 🎨 矢量架构图：[CZ 硅棒提拉与切磨抛加工矢量全景图](./01_crystal_growth_and_wafer/diagrams/cz_silicon_and_wafer_process.svg)
- [x] 半导体物理核心理论与测量：
  - [x] [能带理论、费米能级与载流子输运特性](./02_semiconductor_physics/notes/01_energy_band_and_carriers.md)
  - [x] [PN 结势垒电容与 MOS 结构 C-V 特性精解](./02_semiconductor_physics/notes/02_pn_junction_and_mos_cv.md)
  - [x] [短沟道效应（SCE）全景：DIBL、SS 摆幅与六大漏电流源](./02_semiconductor_physics/notes/03_short_channel_effects.md)
- [x] [逻辑器件演进：Planar → FinFET → GAA → CFET](./03_logic_devices/notes/01_planar_to_finfet_gaa_cfet.md)
- [x] [存储与特色器件概览：SRAM / DRAM / 3D NAND / CIS](./04_memory_and_specialty/notes/01_dram_3dnand_sram_overview.md)
