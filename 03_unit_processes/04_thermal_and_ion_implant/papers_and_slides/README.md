# 热处理与离子注入经典论文、顶级会议讲义与技术白皮书精读指南

本目录用于收纳热氧化、快速退火（RTP/LSA）与离子注入掺杂领域的**奠基性理论论文（Deal-Grove 模型、LSS 理论）、IEDM / IIT 会议 Slides 与设备商白皮书（Axcelis / Applied Materials / TEL）**。

---

## 1. 必读里程碑经典学术论文（Seminal Papers）

### （1）硅热氧化动力学基石（Deal-Grove 经典模型）
- **文献标题**：*General Relationship for the Thermal Oxidation of Silicon*
- **作者与机构**：B. E. Deal & A. S. Grove (Fairchild Semiconductor / Intel 联合创始人安迪·格鲁夫)
- **发表出处**：*Journal of Applied Physics*, 1965.
- **核心贡献**：推导了半导体物理中著名的热氧化线性-抛物线生长动力学方程：
  $$x_o^2 + A x_o = B(t + \tau)$$
  给出了薄层氧化下的表面反应速率常数 $k_s$ 与厚层氧化下的氧扩散扩散系数 $D$，解释了干氧（质量高致密）与湿氧（生长速率快）的根本区别，是整个半导体热氧化工艺的理论基石。

### （2）离子注入射程理论基石（LSS 理论）
- **文献标题**：*Range concepts and heavy ion ranges*
- **作者**：J. Lindhard, M. Scharff, & H. E. Schiøtt (LSS 理论)
- **发表出处**：*Mat. Fys. Medd. Dan. Vid. Selsk*, 1963.
- **核心贡献**：将高能离子打入晶格的能量损失拆解为两项：**核能损（Nuclear Stopping，与晶格原子碰撞导致位移损伤）** 与 **电子能损（Electronic Stopping，非弹性电子碰撞）**，建立了离子投影射程 $R_p$ 与纵向离散偏差 $\Delta R_p$ 的高斯统计分布预测模型。

### （3）超浅结（USJ）与毫秒激光退火突破
- **文献标题**：*Sub-10nm Ultra-Shallow Junction Formation by Millisecond Laser Spike Annealing*
- **发表出处**：*IEDM Technical Digest*, 2007.
- **核心贡献**：系统证明通过利用波长被硅强烈吸收的红外激光，在毫秒级时间内将硅片表面几微米薄层瞬间加热至 1300°C 并在数毫秒内降温，可彻底激活高浓度掺杂原子且让杂质扩散距离小于 1nm。

---

## 2. 推荐研读的技术白皮书与 Slides 索引

1. **Axcelis Purion Platform Technical Papers**
   - 重点关注：Purion H（大束流注入机）在先进制程源漏超浅结与晶圆表面微颗粒防爆控制、Purion M（中束流）的高精度倾角能量纯度控制。
2. **Applied Materials Centura & Vantage RTP Whitepapers**
   - 重点关注：多通道高温计（Pyrometer）片内实时快速测温补偿算法，消除晶圆表面不同图样反射率差异对退火温度的测量失真。
