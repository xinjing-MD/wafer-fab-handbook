# 能带理论、费米能级与载流子输运特性

- **所属模块**：`01_fundamentals_and_devices / 02_semiconductor_physics`

---

## 1. 硅的能带结构与费米-狄拉克分布

### （1）能带参数（室温 300K 条件下）
- **禁带宽度（Bandgap）**：硅的禁带宽度 $E_g \approx 1.12\,\text{eV}$，属于**间接带隙半导体**（导带底不在 $k=0$ 点，电子跃迁需声子协助，发光效率极低，因此硅不适合直接做激光器/发光管，但极适合做开关逻辑器件）。
- **本征载流子浓度（Intrinsic Carrier Concentration）**：
  $$n_i \approx 1.5 \times 10^{10}\,\text{cm}^{-3} \quad (T = 300\text{K})$$
- **费米能级（Fermi Level $E_F$）**：
  - 本征半导体：$E_i$ 位于禁带中央略偏下（考虑有效状态密度 $N_c, N_v$）；
  - **N 型掺杂（掺 P/As/Sb）**：施主能级靠近导带，$E_F$ 向上移动接近 $E_c$；
  - **P 型掺杂（掺 B/BF₂）**：受主能级靠近价带，$E_F$ 向下移动接近 $E_v$。
  - 热平衡质量作用定律：恒满足 $n \cdot p = n_i^2$。

---

## 2. 载流子输运的两大机制：漂移与扩散

### （1）漂移运动（Drift）与迁移率退化
在外部电场 $\mathcal{E}$ 驱动下载流子产生定向运动，电流密度由迁移率 $\mu$ 决定：
$$J_{drift, n} = q n \mu_n \mathcal{E}, \quad J_{drift, p} = q p \mu_p \mathcal{E}$$

- **电子 vs 空穴迁移率（低掺杂室温硅）**：
  - 电子迁移率 $\mu_n \approx 1350\sim 1400\,\text{cm}^2/(\text{V}\cdot\text{s})$
  - 空穴迁移率 $\mu_p \approx 450\sim 500\,\text{cm}^2/(\text{V}\cdot\text{s})$
  - **工程影响**：NMOS 驱动电流天然比 PMOS 大约 2~3 倍。为了对称上拉/下拉延迟，传统电路中 PMOS 宽度往往需要做成 NMOS 的 2 倍。
- **高场速度饱和（Velocity Saturation）**：
  当沟道纵向横向电场超过临界值 $\mathcal{E}_{sat} \approx 10^4\,\text{V/cm}$ 时，载流子与光学声子频繁碰撞，漂移速度不再随电场增加，达到极限饱和速度 $v_{sat} \approx 10^7\,\text{cm/s}$。先进短沟道 MOSFET 的驱动电流从原来的平方律变成一次线性关系。

### （2）扩散运动（Diffusion）与爱因斯坦关系式
由于载流子浓度梯度产生热运动扩散：
$$J_{diff, n} = q D_n \frac{dn}{dx}, \quad J_{diff, p} = -q D_p \frac{dp}{dx}$$
扩散系数与迁移率满足爱因斯坦关系式（Einstein Relation）：
$$\frac{D}{\mu} = \frac{k_B T}{q} = V_t \approx 25.9\,\text{mV} \quad (300\text{K})$$

---

## 3. 晶圆厂工艺对迁移率与输运的影响

1. **杂质电离散射（Ionized Impurity Scattering）**：
   - 掺杂浓度越高，离子杂质对载流子的库仑散射越剧烈，迁移率急剧下降。
   - 先进节点采用 **Halo / Pocket 注入** 时，必须权衡阈值调整与迁移率折损。
2. **表面粗糙度散射（Surface Roughness Scattering）**：
   - 当栅极强反型电场把电子紧紧压在 $\text{Si}-\text{SiO}_2$ 界面时，原子级起伏会导致迁移率滚降。
   - 这也是为什么 CMP 和前道清洗后对晶圆表面粗糙度（AFM 测 $R_a < 0.1\,\text{nm}$）要求极严的原因。
3. **应变工程（Strained Silicon）对能带的重构**：
   - 双轴/单轴拉应力：分裂导带能谷简并度，降低电子有效质量，**提升 NMOS 电子迁移率 50%+**；
   - 单轴压应力（源漏嵌入 SiGe）：分裂价带重空穴与轻空穴能带，**提升 PMOS 空穴迁移率 100%+**。
