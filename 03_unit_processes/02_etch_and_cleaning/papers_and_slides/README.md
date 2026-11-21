# 刻蚀与清洗经典论文、顶级会议讲义与技术白皮书精读指南

本目录用于收纳等离子体干法刻蚀、原子层刻蚀（ALE）与湿法清洗领域的**核心学术论文（Coburn & Winters 开山之作等）、AVS / IEEE / IEDM 会议 Slides 与设备商白皮书（Lam Research / TEL / ACM Research）**。

---

## 1. 必读里程碑经典学术论文（Seminal Papers）

### （1）等离子体刻蚀物理机理奠基作（离子辅助刻蚀）
- **文献标题**：*Ion-surface interactions in plasma etching*
- **作者与出处**：J. W. Coburn & H. F. Winters, *Journal of Applied Physics*, 1979.
- **核心贡献**：**半导体干法刻蚀历史上最著名的经典实验**！通过独立控制中性 $\text{XeF}_2$ 气体分子和 $\text{Ar}^+$ 氩离子束轰击单晶硅表面，证实：
  - 单独通 $\text{XeF}_2$ 气体：硅刻蚀速率极低；
  - 单独用 $\text{Ar}^+$ 离子轰击：物理溅射速率极慢；
  - **两者同时作用：刻蚀速率瞬间暴增近十倍！**
  - **结论**：证明干法刻蚀本质是**“高能离子垂直轰击损伤晶格表面键合 + 中性自由基高效化学络合反应”**的协同效应，奠定了各向异性等离子体刻蚀的理论基石。

### （2）原子层刻蚀（Atomic Layer Etch, ALE）系统性综述
- **文献标题**：*Overview of atomic layer etching in the semiconductor industry*
- **作者与机构**：K. J. Kanarik 等 (Lam Research)
- **发表出处**：*Journal of Vacuum Science & Technology A*, 2015.
- **核心贡献**：定义了准原子层自限制反应刻蚀循环（ALE Synergy 参数），拆解了氟化/氯化表面改性层与低能离子轰击脱附机理，阐明其在 GAA 纳米片纳米级选择比释放中的不可替代性。

### （3）湿法清洗颗粒去除与表面张力干燥机理
- **文献标题**：*The Evolution of Silicon Wafer Cleaning Technology*
- **作者**：Werner Kern (RCA 清洗标准发明人)
- **发表出处**：*Journal of The Electrochemical Society*, 1990.
- **核心贡献**：系统阐述 RCA 标准配方（SC-1、SC-2）在消除金属离子吸附能级、调节硅表面 Zeta 电位使颗粒自发排斥剥离的电化学热力学原理。

---

## 2. 厂商核心技术白皮书与 Slides 关注点

1. **Lam Research Sense.i & Kiyo Etch Platform**
   - 重点关注：等离子体腔室内部微秒级多频脉冲射频控制（Pulsed RF）、边缘聚焦环（Focus Ring）自动电学高度补偿以消除 Edge Exclusion 边界效应。
2. **TEL Tactras & Unity CCP Dielectric Etch**
   - 重点关注：针对 3D NAND 上百层极深孔道（HARC）在低温（-60°C ~ -80°C Cryogenic Etch）下的各向异性刻蚀技术，利用超低温在孔壁形成高保护性冷凝钝化层。
3. **ACM Research 盛美上海单片兆声波清洗白皮书**
   - 重点关注：SAPS（空间交变相位移动兆声波）技术，如何消除驻波局部空化破坏脆弱纳米微结构（Fin 鳍片或 Gate 倒塌）。
