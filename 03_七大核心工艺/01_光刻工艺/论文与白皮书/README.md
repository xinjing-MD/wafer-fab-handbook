# 光刻领域经典论文、顶级会议讲义与技术白皮书精读指南

本目录用于收纳光刻方向的**里程碑学术论文、顶级行业研讨会（SPIE Advanced Lithography / IEDM）核心 Slides 与厂商官方白皮书（ASML / Zeiss / Nikon / TEL）**。

> 💡 **上传建议**：单篇论文 PDF（< 10MB）可直接存放于本目录；整套厚讲义或视频教程请在同级 `外部资料索引.md` 中维护网盘/外部链接。

---

## 1. 必读里程碑经典学术论文（Seminal Papers）

### （1）浸没式光刻（Immersion Lithography）奠基作
- **文献标题**：*Immersion Lithography and Its Impact on Semiconductor Manufacturing*
- **作者与机构**：Burn J. Lin (林本坚, TSMC)
- **发表出处**：*Journal of Micro/Nanolithography, MEMS, and MOEMS (JM3)*, 2004.
- **核心贡献**：打破了 193nm 干法光刻的瓶颈，提出在最后一片物镜与晶圆之间注入去离子纯水（折射率 $n=1.44$），将有效波长压缩至 $134\,\text{nm}$，并将数值孔径推至 $NA > 1.0$（最终达到 $NA=1.35$），拯救了全球半导体工业并支撑摩尔定律推进了四代节点。
- **精读重点**：水中微气泡（Micro-bubbles）对散射缺陷的影响、偏振光效应（Polarization Effect）与超高 NA 下的成像退化。

### （2）EUV 极紫外光刻物理与光源突破
- **文献标题**：*Extreme Ultraviolet Lithography: From Laboratory Curiosity to High-Volume Manufacturing*
- **来源**：*SPIE Advanced Lithography Keynote*, ASML / Zeiss 联合研发团队.
- **核心贡献**：系统拆解了通过高功率 $\text{CO}_2$ 激光器两级轰击熔融锡液滴（Sn Droplet）产生 13.5nm 等离子体软 X 射线机理、Mo/Si 多层膜布拉格反射镜（反射率极限 ~70%）以及反射式光罩（Reticle）设计难题。
- **精读重点**：EUV 随机效应（Stochastics：Nano-bridging 与 Line-break）、光子散粒噪声（Photon Shot Noise）对线边缘粗糙度（LER）的根本限制。

### （3）计算光刻与光学邻近修正（OPC / SMO）
- **文献标题**：*The Optical Proximity Correction: Physics, Algorithms, and Industrial Implementation*
- **作者**：Chris A. Mack 等
- **核心贡献**：推导衍射截断导致直角变圆角、孤立线与密集线线宽偏移的物理模型，确立基于模型（Model-based OPC）与光源-掩模协同优化（SMO, Source-Mask Optimization）的标准工业算法。

---

## 2. 推荐研读的官方技术白皮书与 Slides 索引

1. **ASML EUV & High-NA Technology Whitepapers**
   - 重点关注：High-NA EUV ($NA=0.55$) 的变形物镜设计（Anamorphic Optics，水平与垂直方向放大倍率不同：4X vs 8X）与曝光场减半对光罩拼接的影响。
2. **TEL Lithius Pro Track Technical Bulletins**
   - 重点关注：曝光后烘烤（PEB）热板温度均匀性补偿算法（Multi-zone Heater Plate Tuning，精度达到 $\pm 0.01^\circ\text{C}$）与减少显影残留缺陷（Defect-free Development Nozzle）。
3. **Zeiss Starlith Optics Monograph**
   - 重点关注：原子级抛光精度镜面、热透镜效应（Lens Heating）主动自适应波前形变修正。

---

## 3. 本地论文文件命名与归档规范

如果向本目录添加 PDF 文件，请统一遵循以下命名格式：
```text
[年份]_[会议或期刊]_[第一作者]_[关键词简写].pdf
例如：
2004_JM3_Lin_Immersion_Lithography.pdf
2020_SPIE_ASML_High_NA_EUV_Progress.pdf
2023_IEDM_TSMC_N2_Nanosheet_Litho.pdf
```
