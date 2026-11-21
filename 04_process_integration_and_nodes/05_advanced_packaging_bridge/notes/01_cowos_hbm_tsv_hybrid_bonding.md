# 晶圆厂与先进封装的桥梁：TSV / RDL / Hybrid Bonding / CoWoS

- **所属模块**：`04_process_integration_and_nodes / 05_advanced_packaging_bridge`

## 1. 为什么传统晶圆厂开始“向后延伸”做先进封装？
摩尔定律单颗芯片面积逼近光刻机曝光场极限（Reticle Limit 约 $858\,\text{mm}^2$），且 HBM 高带宽内存需要数千根超短互连线直连 GPU。传统封测厂（OSAT）的引线键合与基板精度远不够用，必须动用**晶圆厂级别的精密光刻、PVD/ECP 与 CMP 设备**（即 **Middle-End / Wafer-Level Packaging**）。

---

## 2. 四大核心衔接技术

| 技术 | 英文全称 | 核心制造步骤与归属设备 | 典型应用 |
| :--- | :--- | :--- | :--- |
| **RDL** | 重布线层 (Redistribution Layer) | 光刻聚酰亚胺(PI)介质 + PVD Ti/Cu Seed + ECP 镀铜 + Flash Etch（类似简版粗线宽 BEOL） | Fan-Out（InFO）、硅中介层互连 |
| **TSV** | 硅通孔 (Through-Silicon Via) | **Bosch 深硅刻蚀** → 侧壁低温绝缘层 → PVD 阻挡/种子层 → **自底向上铜电镀填孔** → 晶圆背面研磨露铜（Reveal） | **HBM 堆叠内存**、3D SoIC、CoWoS 硅中介层 |
| **Micro-bump** | 微凸点 | 在晶圆表面镀铜柱（Cu Pillar）+ 锡银焊料帽，间距可微缩至 ~25~40μm | 2.5D CoWoS 芯片贴装、早期 HBM 堆叠 |
| **Hybrid Bonding** | 混合键合（无凸点直连） | **极高精度超平坦 CMP** + 等离子体表面活化 → **亚微米高精度贴片对准** → 室温预键合 + 低温退火实现 **$\text{SiO}_2-\text{SiO}_2$ 与 $\text{Cu}-\text{Cu}$ 同步原子级键合**；间距突破 `< 10μm` | AMD 3D V-Cache、堆叠式 CIS、下一代 HBM4 |
