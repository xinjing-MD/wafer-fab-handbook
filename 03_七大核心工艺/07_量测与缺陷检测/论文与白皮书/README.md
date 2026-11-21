# 量测与检测经典论文、顶级会议讲义与技术白皮书精读指南

本目录用于收纳在线关键尺寸测量（CD-SEM）、光学散射测量（OCD）、套刻精度（Overlay）、明暗场缺陷检测及电子束电压衬度检测的**经典学术论文、SPIE Advanced Lithography & Patterning / ASMC 会议 Slides 与设备商白皮书（KLA / ASML YieldStar / Applied Materials）**。

---

## 1. 必读里程碑经典学术论文（Seminal Papers）

### （1）光学临界尺寸散射量测（OCD / Scatterometry）模型反演
- **文献标题**：*Specular Spectroscopic Scatterometry for CD and Profile Measurement of Sub-0.10 μm Features*
- **作者与机构**：Chuan-Pu Lee, Costas J. Spanos 等 (UC Berkeley)
- **发表出处**：*SPIE Microlithography Proceedings*, 2001.
- **核心贡献**：系统建立了严格耦合波分析算法（RCWA, Rigorous Coupled Wave Analysis）用于求解麦克斯韦电磁方程组，成功从偏振反射光谱中高精度逆向推导出纳米级光栅线宽、高度、下陷深度与侧壁倾角，奠定了非破坏性在线三维轮廓检测的工业基石。

### （2）套刻精度高阶数学模型与网格残差分解
- **文献标题**：*Advanced Overlay Modeling and High-Order Field Corrections in Sub-20nm Manufacturing*
- **来源**：*SPIE Metrology, Inspection, and Process Control for Microlithography*, 2013.
- **核心贡献**：将传统的线性曝光场对准模型扩展至 3 阶与 5 阶非对称热膨胀及透镜畸变修正；解析了应力引起的片内晶圆网格畸变（Non-Rigid Wafer Distortion）以及在 CMP 抛光和极高应力薄膜后如何有效补偿套刻漂移。

### （3）先进逻辑节点随机缺陷与极限检出率（Stochastics Detection）
- **文献标题**：*Stochastic Defectivity in EUV Lithography: Detection, Review, and Impact on Yield*
- **发表出处**：*SPIE Advanced Lithography*, 2019 (KLA & IMEC 联合研究).
- **核心贡献**：分析了单台芯片上数百亿个接触孔（Contact Holes）中由极紫外光子散粒噪声导致的随机微桥接（Micro-bridge）与漏开孔（Missing Vias），给出了大面积宽带明场光学检测（Broadband Plasma）与超高速多束电子束扫描（Multi-beam SEM）的最优采样数学模型。

---

## 2. 厂商白皮书与技术 Slides 索引

1. **KLA Process Control & Yield Management Handbook**
   - 重点关注：如何构建产线抽检优化矩阵——在牺牲产线产能（Throughput / WPH）与降低漏检风险（Capture Rate）之间寻找黄金平衡点；如何利用电压衬度（Voltage Contrast）抓出微小开路隐性失效。
2. **ASML YieldStar DBO (Diffraction-Based Overlay) Whitepaper**
   - 重点关注：基于第一级衍射光强不对称度（Asymmetry）实时反算上下层光栅对准误差，精度达到令人惊叹的 `< 0.15 nm`。
