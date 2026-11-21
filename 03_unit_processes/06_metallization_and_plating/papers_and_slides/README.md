# 金属化与电镀经典论文、顶级会议讲义与技术白皮书精读指南

本目录用于收纳铜双大马士革（Dual Damascene）、ECP 超填电镀、电迁移（EM）可靠性及 Co/Ru 先进互连替代的**核心学术论文、IEDM / IITC (IEEE International Interconnect Technology Conference) 论文与厂商白皮书（Lam Research / Applied Materials）**。

---

## 1. 必读里程碑经典学术论文（Seminal Papers）

### （1）IBM 铜双大马士革颠覆铝互连奠基作
- **文献标题**：*Full copper wiring in a sub-0.25 μm CMOS ULSI technology*
- **作者与机构**：D. Edelstein 等 (IBM Microelectronics Division)
- **发表出处**：*IEDM Technical Digest*, 1997.
- **核心贡献**：**芯片制造史上最著名的技术转折点之一**。IBM 正式向全球展示了采用铜作为片上多层互连导线的全套可量产工艺方案；彻底解决了深亚微米下 RC 延迟恶化与铝导线电迁移（Electromigration）烧断的物理极限，将芯片互连速度推升了 30% 以上。

### （2）电化学电镀“自底向上超填（Superfilling）”动力学理论
- **文献标题**：*Superconformal electrodeposition of copper: Theory and experiment*
- **作者与机构**：T. P. Moffat, D. Wheeler, W. H. Schwarzacher, & D. Josell (NIST 美国国家标准与技术研究院)
- **发表出处**：*Electrochemical and Solid-State Letters*, 2001.
- **核心贡献**：提出著名的**曲率增强加速剂吸附模型（CEAC, Curvature Enhanced Accelerator Coverage）**，从反应电化学和流体力学微观层面数学推导了：为什么在槽底面积随填充收缩时加速剂聚集浓度暴增，从而使底部铜生长速度数倍于槽口，实现完美的“无空洞由下至上超填”。

### （3）先进纳米互连（Ru / Co / Mo）尺寸效应物理极限
- **文献标题**：*Limits of Interconnect Scaling: Resistance and Electromigration in Sub-10nm Nodes*
- **发表出处**：*IEEE IITC Keynote Paper*, 2021.
- **核心贡献**：系统测试并分析了电子表面非弹性散射与晶界散射（Mayadas-Shatzkes 模型）对极细导线电阻率的暴击机制；阐明钌（Ru）由于电子平均自由程极短（仅 ~6.6nm，远小于 Cu 的 ~39nm），在 10nm 以下细间距互连中线电阻反超铜的临界转变点。

---

## 2. 厂商白皮书与技术 Slides 索引

1. **Lam Research SABRE 3D & ECP Solutions**
   - 重点关注：针对 2.5D/3D TSV 高深宽比硅通孔快速电镀填铜的无空洞电解液配方与流体力学喷流设计。
2. **Applied Materials Endura Volta Selective Deposition**
   - 重点关注：无阻挡层（Barrierless）自对准金属覆盖层（Cobalt Capping Layer）技术，如何将铜互连的抗电迁移（EM）寿命提高 80 倍。
