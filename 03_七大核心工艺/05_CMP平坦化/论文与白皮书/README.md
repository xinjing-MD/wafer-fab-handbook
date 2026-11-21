# CMP 化学机械平坦化经典论文、顶级会议讲义与技术白皮书精读指南

本目录用于收纳化学机械抛光（CMP）研磨机理、Slurry 浆料胶体化学、终点检测（EPD）与缺陷控制的**经典学术文献、ICPT / MRS 研讨会 Slides 与设备商白皮书（Applied Materials / Ebara / Cabot / DuPont）**。

---

## 1. 必读里程碑经典学术论文（Seminal Papers）

### （1）微电子 CMP 接触力学与磨削机理
- **文献标题**：*Mechanisms of Chemical Mechanical Polishing in ULSI Applications*
- **作者与机构**：F. B. Kaufman 等 (IBM Thomas J. Watson Research Center)
- **发表出处**：*Journal of The Electrochemical Society*, 1991.
- **核心贡献**：IBM 团队首次向全球半导体产业系统展示了如何将传统光学镜头抛光转化为亚微米金属多层互连的关键平坦化工艺；提出表面化学改性软化薄层与磨料机械去除的动态平衡模型。

### （2）铜 CMP 碟形凹陷（Dishing）与侵蚀（Erosion）建模
- **文献标题**：*Modeling and Characterization of Pattern-Dependent Variation in Copper Chemical Mechanical Polishing*
- **作者与机构**：Duane S. Boning 教授团队 (MIT Microsystems Technology Laboratories)
- **发表出处**：*IEEE Transactions on Semiconductor Manufacturing*, 2002.
- **核心贡献**：建立了基于图形密度（Pattern Density）的物理接触力学高度演化模型，揭示抛光垫弹性形变如何跨越宽铜线造成局部碟形下陷，奠定了当今 EDA 物理验证中“自动插入 Dummy Fill 与 CMP 规则检查”的标准工业算法。

### （3）CMP 磨料流变学与划伤（Scratch）生成机理
- **文献标题**：*Particle Agglomeration and Micro-Scratching in CMP Slurries*
- **发表出处**：*Journal of Colloid and Interface Science*, 2012.
- **核心贡献**：阐明了研磨液在输送泵剪切力与温度变化下，二次团聚体（Large Particle Count, LPC > 1μm）的产生规律，指导晶圆厂在 POU（机台使用端）部署高精滤芯防晶圆大面积刮伤。

---

## 2. 厂商白皮书与技术 Slides 索引

1. **Applied Materials Reflexion LK & EPD Whitepaper**
   - 重点关注：FullScan 在线全反射光谱终点检测系统与多区（Multi-zone）气囊压力闭环调节技术。
2. **Ebara 荏原抛光系统技术讲义**
   - 重点关注：原子级混合键合（Hybrid Bonding）专用 CMP 工艺中，将表面粗糙度降低至 $R_q < 0.1\,\text{nm}$ 并实现铜焊盘特定纳米级微凹下压（Dishing < 3nm）的高难度控制。
