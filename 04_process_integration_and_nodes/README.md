# 04 · 工艺整合与节点演进 (`04_process_integration_and_nodes`)

> 单项工艺（Unit Process）关心“这一步膜长得好不好、孔刻得直不直”；**工艺整合（PIE, Process Integration Engineering）**关心“把 1000 步拼在一起，最终芯片的电学性能 $V_{th}/I_{on}/I_{off}$ 和良率能不能达标”。

## 目录内容
- `01_cmos_full_flow/` —— FEOL / MOL / BEOL 完整制造链与重入式流片逻辑
- `02_logic_node_evolution/` —— 从 28nm HKMG 到 GAA、BSPDN 背面供电的演进
- `03_memory_process_flows/` —— DRAM（1T1C/深圆柱电容）与 3D NAND（百层堆叠/HARC/阶梯）工艺流
- `04_specialty_technologies/` —— CIS 背照堆叠工艺、碳化硅（SiC）与氮化镓（GaN）功率工艺
- `05_advanced_packaging_bridge/` —— 前道 Fab 与先进封装（TSV / RDL / Hybrid Bonding / CoWoS / HBM）衔接

## 学习 Checklist
- [x] [完整 CMOS 工艺串联：FEOL → MOL → BEOL 与重入流转逻辑](./01_cmos_full_flow/notes/01_feol_mol_beol_walkthrough.md)
- [x] [先进逻辑节点核心技术跃迁：HKMG → SAQP → GAA → BSPDN](./02_logic_node_evolution/notes/01_node_scaling_hkmg_to_bspdn.md)
- [x] 主流存储器制造全流程拆解：
  - [x] [1T1C DRAM 制造全流程、深圆筒微电容与微缩挑战](./03_memory_process_flows/notes/01_dram_process_flow_and_capacitor.md)
  - [x] [3D NAND 百层制造全流程、超高深宽比孔刻蚀（HARC）与字线替换](./03_memory_process_flows/notes/02_3d_nand_process_flow_and_harc.md)
- [x] 特色与宽禁带工艺实战：
  - [x] [CMOS 图像传感器（CIS）：背照式（BSI）与三维堆叠键合工艺](./04_specialty_technologies/notes/01_cis_bsi_and_stacked_process.md)
  - [x] [碳化硅（SiC）与氮化镓（GaN）宽禁带功率晶圆厂工艺](./04_specialty_technologies/notes/02_sic_gan_power_fab_process.md)
- [x] [晶圆厂与先进封装的桥梁：TSV / RDL / Hybrid Bonding](./05_advanced_packaging_bridge/notes/01_cowos_hbm_tsv_hybrid_bonding.md)
