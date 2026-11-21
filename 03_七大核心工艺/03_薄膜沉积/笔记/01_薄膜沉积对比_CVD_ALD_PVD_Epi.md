# 薄膜沉积工艺对比：CVD / ALD / PVD / 外延（Epi）

- **所属模块**：`03_七大核心工艺 / 03_薄膜沉积`

---

## 1. 四大沉积技术选型全景与反应动力学本质

### 1.1 技术选型对比矩阵

| 技术分支 | 核心物理/化学本质 | 工程典型温度与腔压区间 | 台阶覆盖率 (Step Coverage) | 典型工业设备架构 | 300mm 产线典型应用场景 |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **LPCVD** | 热驱动低压表面化学反应 | 高温 $500\sim 900^\circ\text{C}$<br>低压 $0.1\sim 2\,\text{Torr}$ | 极佳（表面反应控制区，$90\%\sim 99\%$） | 立式批量炉管 (Vertical Batch Furnace，如 TEL / ASM A412，一次 $50\sim 150$ 片) | 多晶硅假栅、$\text{Si}_3\text{N}_4$ 阻挡/硬掩模、TEOS 高温氧化硅（FEOL 为主） |
| **PECVD** | 等离子体电子碰撞解离激发低温反应 | 低温 $200\sim 400^\circ\text{C}$<br>中压 $1\sim 10\,\text{Torr}$ | 中等（自由基粘附系数高，常规 $30\%\sim 60\%$；可借助 HDP/FCVD 填隙） | 多腔室单片簇集系统（如 AMAT Producer / Lam Vector 双频电容耦合 CCP） | BEOL 低 $k$ 介质 (SiCOH)、$\text{SiCN}$ 刻蚀阻挡层、芯片钝化层（保护后道低熔点金属） |
| **ALD** | 前驱体交替脉冲 + **自限制表面半反应** | 低温 $100\sim 380^\circ\text{C}$<br>低压 $0.1\sim 5\,\text{Torr}$ | **接近 $100\%$**（高深宽比 $AR>50:1$ 仍具原子级保形性） | 单片高速切换腔 / Spatial 空间隔离 / Batch ALD（如 ASM Pulsar/XP8、Lam Striker） | HKMG $\text{HfO}_2$ 栅介质、GAA 内侧墙、高 $AR$ 阻挡层 (TiN/TaN)、SAQP 芯轴侧墙 |
| **PVD** | 高能 $\text{Ar}^+$ 磁控溅射靶材原子物理飞溅 | 室温 $\sim 350^\circ\text{C}$<br>高真空 $1\sim 10\,\text{mTorr}$ | 较差（直射弹道流易在沟槽口产生悬垂 Overhang；I-PVD 可改善底角覆盖） | 旋转磁控 + 自离化离子辅助腔体（如 AMAT Endura I-PVD / SIP） | Ta/TaN 阻挡层、Cu Seed 种子层、Ti/TiN 粘附层、Al 焊盘金属、背面金属化 |
| **Epi** | 沿单晶衬底晶格延续的外延晶体生长 | 中高温 $550\sim 1100^\circ\text{C}$<br>常压至减压 $5\sim 760\,\text{Torr}$ | 晶向依赖各向异性生长（或基于 $\text{HCl}$ 的选择性外延 SEG） | 单片减压外延腔（RPCVD，如 AMAT Centura Epi / ASM Epsilon，辐射灯加热） | 源漏应力工程 ($\text{SiGe}:B$ / $\text{Si}:P$)、GAA $\text{Si/SiGe}$ 超晶格叠层、外延硅片衬底 |

---

### 1.2 CVD 气相输运与边界层动力学（Grove 传质—反应竞争模型）

化学气相沉积（CVD）速率并非单纯由加热温度决定，而是**气相边界层传质通量**与**晶圆表面化学反应通量**串联耦合的结果（A. S. Grove 经典模型）：

1. **气相边界层传质通量 $J_1$**：反应物从主流气体穿过厚度为 $\delta$ 的滞流边界层（Boundary Layer）向晶圆表面扩散：
   $$J_1 = h_g (C_g - C_s), \quad h_g \approx \frac{D_g}{\delta}$$
   其中 $C_g$ 为主气流反应物浓度，$C_s$ 为晶圆表面反应物浓度，$D_g$ 为气相扩散系数，$h_g$ 为气相传质系数。
2. **表面化学反应通量 $J_2$**：到达表面的反应物按一级反应速率常数 $k_s$ 发生热分解成膜：
   $$J_2 = k_s C_s, \quad k_s = k_0 \exp\left(-\frac{E_a}{k_B T}\right)$$
3. **稳态串联通量与生长速率 $G$**：令 $J_1 = J_2 = J_{total}$，消去未知量 $C_s$ 并除以薄膜分子密度 $N_0$：
   $$G = \frac{1}{N_0} \cdot \frac{h_g k_s}{h_g + k_s} C_g$$

这一经典公式直接划分了晶圆厂 CVD 的两大动力学工作区及机台架构选择逻辑：

```text
  ln(G)
   ▲       [低温: 表面反应控制区]         [高温: 气相传质控制区]
   │        k_s << h_g (斜率 -E_a/k_B)     h_g << k_s (几乎平坦)
   │             ╱                        ───────────────────
   │            ╱                         (速率受边界层δ和气流速度制约)
   │           ╱   ← 转折温度 T_c
   │          ╱   (LPCVD 必须工作在左侧，严禁落入右侧！)
   └─────────┴────────────────────────────────────────────────▶ 1000/T (K⁻¹)
    高温                                                      低温
```

- **表面反应控制区（$k_s \ll h_g$，即 LPCVD 典型区）**：生长速率 $G \approx \frac{k_s C_g}{N_0}$ 仅对温度敏感，对气流几何分布和边界层厚度 $\delta$ 极不敏感。由于气相扩散系数满足动力学关系 $D_g \propto \frac{T^{3/2}}{P}$，**LPCVD 刻意将腔压抽低至 $0.1\sim 1\,\text{Torr}$（降压千倍使 $D_g$ 暴涨千倍）**。这使得立式炉管内间距仅 $4\sim 6\,\text{mm}$ 的上百片 300mm 晶圆之间能够瞬间补足反应物浓度，片内非均匀性（WiWNU）和片间非均匀性（WtWNU）均可控在 $1\%$ 以内，同时避免高温常压下前驱体在气相过早碰撞产生均相成核颗粒（Gas-phase Nucleation / Snowing）。
- **气相传质控制区（$h_g \ll k_s$，APCVD 或高温常压外延区）**：速率 $G \approx \frac{D_g C_g}{\delta N_0}$ 直接受限于边界层厚度 $\delta \propto \sqrt{\mu x / (\rho v)}$。晶圆必须水平放置并高速旋转（通过离心流减薄并均一化 $\delta$），且进气口需设计多区气流调节阀（Showerhead 或 Cross-flow 喷嘴分流），否则晶圆迎风面与背风面将出现严重的膜厚斜坡（Thickness Tilt）。

---

## 2. 核心工程概念与微观物理机制拆解

### 2.1 台阶覆盖率、粘附系数（$S_c$）与高深宽比 Gap Fill 工程演进

在先进节点高深宽比（High Aspect Ratio, $AR = H/W > 10:1\sim 50:1$）的 STI 浅槽隔离或金属间介质缝隙中，分子自由程 $\lambda$ 远大于沟槽宽度 $W$（克努森数 $Kn = \lambda / W \gg 1$），沟槽内部进入**弹道分子流输运**。此时台阶覆盖率由**反应物在壁面的粘附系数（Sticking Coefficient, $S_c$）**决定：
- 当 $S_c \to 1$（如传统 PVD 飞溅金属原子、传统硅烷 $\text{SiH}_4$ 等离子体生成的极高活性自由基），粒子撞到槽口顶部侧壁即“一粘就停”。由于槽口几何接收立体角（Solid Angle）大于槽底，顶部横向快速长厚并形成**悬垂（Overhang）**，在底部填满之前槽口便发生**夹断（Pinch-off）**，遗留致命的 **Keyhole / Void（空洞）**——在后续 CMP 或刻蚀打开顶部后，Void 会成为铜电镀短路或漏电的隐形杀手。
- 要获得接近 $100\%$ 的保形覆盖，前驱体的等效 $S_c$ 必须低至 $10^{-3}\sim 10^{-5}$ 量级，使分子能在槽壁间经历数百次无损弹跳并抵达槽底。

**产线四大高深宽比 Gap Fill 工程路线与 Trade-off**：
1. **HDPCVD（高密度等离子体化学气相沉积，如 AMAT Ultima HDP）**：
   - 采用电感耦合等离子体（ICP）配合晶圆底座偏压（Bias RF），在通入 $\text{SiH}_4/\text{O}_2$ 沉积 $\text{SiO}_2$ 的同时引入高能 $\text{Ar}^+$ 离子对膜层进行原位物理微溅射；
   - 根据物理溅射产额随入射角变化规律，**$\text{Ar}^+$ 对 $45^\circ$ 倾角的刻蚀速率是水平面的 $3\sim 4$ 倍**，恰好将槽口堆积出的 $45^\circ$ 悬垂棱角连续削平（保持沟槽口始终张开）；
   - 工程核心指标为**沉积/溅射比（Deposition/Sputter Ratio, D/S 比，工程典型区间 $3.0\sim 5.5$）**。缺点是 $AR > 6:1$ 时沟槽底部再沉积效率下降且高能离子易损伤脆弱鳍片或窄栅线。
2. **SA-CVD / HARP（臭氧—TEOS 亚常压沉积）**：利用 $\text{O}_3$ 与正硅酸乙酯（TEOS）产生低粘附系数（$S_c \approx 10^{-3}$）的硅氧烷中间体，实现接近流变态的表面迁移率填充，可解决 $AR \approx 8:1\sim 12:1$ 的 STI 填充，无需高能离子轰击。
3. **FCVD（流动性 CVD，如 AMAT Eterna / Lam 等）**：
   - 在接近室温至 $100^\circ\text{C}$ 下将胺基硅烷与自由基聚合成**液态低聚硅氮烷/聚硅氧烷（Flowable Oligomer）**，利用毛细管力像水流一样完全零空洞灌满 $AR > 20:1$ 且带倒梯形（Re-entrant）的极端沟槽；
   - 随后经蒸汽退火（Steam Cure，$350\sim 550^\circ\text{C}$ 水汽置换 $-\text{NH}-$ 键）+ 高温/UV 固化氧化将聚合物转化为致密 $\text{SiO}_2$（伴随约 $15\%\sim 20\%$ 体积收缩，需精准匹配张应力防止把 Fin 拽歪）。
4. **I-PVD（离化物理气相沉积）克服金属 Overhang**：
   - 传统磁控溅射靠中性的飞溅原子各向同性到达沟槽口，极易在深宽比 $4:1$ 的通孔入口形成铜/钽悬垂。先进 300mm 机台采用 **SIP（自离化等离子体，如 AMAT Endura）** 或空心阴极磁控靶，瞬间施加极高靶功率使溅射出的金属原子（如 $\text{Cu}^+, \text{Ta}^+$）自身发生高达 $30\%\sim 70\%$ 的电离；
   - 通过调节晶圆卡盘 RF Bias，使带正电金属离子在鞘层电场下垂直轰击沟槽底部，并将槽底厚积的金属通过**再溅射（Resputtering）**均匀涂抹到极难覆盖的下端侧壁，实现超薄连续阻挡层与无空洞电镀种子层覆盖（但 Bias 过强会击穿底部介质或打薄通孔拐角）。

---

### 2.2 ALD 表面饱和动力学、生长窗口与量产提速架构

**原子层沉积（ALD）** 源于 1974 年 Tuomo Suntola 提出的原子层外延（ALE）及 Steven M. George 等人完善的表面配体交换化学理论。其核心在于将传统 CVD 的连续气相混合反应拆分为空间与时间彻底隔离的两组**自限制（Self-limiting）半反应**。

以产线最经典的 $\text{Al}_2\text{O}_3$（三甲基铝 $\text{TMA}, \text{Al(CH}_3)_3$ + $\text{H}_2\text{O}$）为例，其表面化学反应如下：
- **半反应 A（TMA 脉冲）**：
  $$\text{Si-OH}^* + \text{Al(CH}_3)_3(g) \longrightarrow \text{Si-O-Al(CH}_3)_2^* + \text{CH}_4(g)\uparrow$$
  当所有表面活性羟基（$-\text{OH}^*$）被 $-\text{CH}_3$ 封端消耗殆尽，后续到达的 TMA 分子无法再化学吸附（饱和覆盖度 $\theta \to 1$），生长在单原子层水平自动锁死。
- **半反应 B（$\text{H}_2\text{O}$ 脉冲，经惰性 $\text{N}_2/\text{Ar}$ 充分 Purge 后）**：
  $$\text{Si-O-Al(CH}_3)_2^* + 2\text{H}_2\text{O}(g) \longrightarrow \text{Si-O-Al(OH)}_2^* + 2\text{CH}_4(g)\uparrow$$
  氧化剂剥除甲基并再生全新的 $-\text{OH}^*$ 表面，完成 1 个 Cycle（工程典型每循环生长量 **GPC, Growth Per Cycle $\approx 0.9\sim 1.1\,\text{\AA}$**，受空间位阻限制并非完整单晶层而是约 $1/3$ 单分子层）。

**ALD 温度窗口（ALD Window）失效边界**：
```text
  GPC (Å/cycle)
   ▲
   │  ╲    凝结/冷凝(物理吸附)               前驱体热分解(CVD化)   ╱
   │   ╲                                                        ╱
   │    ╲       ┌──────────────────────────────┐               ╱
   │     └──────┤     最佳 ALD 工艺温度窗口      ├──────────────┘
   │   反应速率不足  GPC 恒定、自限制保形性最佳   ╲  前驱体热脱附
   │   (动力学受限)                               ╲  (活性位点覆盖↓)
   └────────────┴──────────────────────────────┴──────────────▶ Temperature (°C)
               100°C                          350°C
```

- **Thermal ALD vs PEALD（等离子体增强 ALD）的工程 Trade-off**：
  - **PEALD** 在半反应 B 通入远程或直接 $\text{O}_2 / \text{N}_2 / \text{H}_2$ 等离子体自由基替代 $\text{H}_2\text{O}$，能将成膜温度骤降到 $50\sim 200^\circ\text{C}$ 且大幅提高膜层致密度（例如低损伤 $\text{SiN}$ 侧墙）。
  - 但其致命弱点在于**自由基壁面复合损失（Surface Recombination Loss）**：自由基撞击深沟槽侧壁极易复合猝灭为普通稳定分子，导致 PEALD 在超高深宽比结构（$AR > 20:1$）底部出现保形性衰减，而 Thermal ALD 则几乎不受沟槽深度限制。
- **破解 ALD 产能（WPH）瓶颈的两大工业量产方案**：
  - 传统单腔时间隔离 ALD（Temporal ALD）大量时间浪费在脉冲后的抽气吹扫（Purge），导致 50~100 循环单腔有效产能极低（$<10\sim 15\,\text{WPH}$）。
  - **Batch ALD（立式批量炉管，如 TEL / ASM）**：一次装入 $50\sim 100$ 片晶圆同时运行几十秒一个 Cycle，摊薄单片时间至数秒，适合 $\text{SiO}_2/\text{SiN}$ 侧墙等大批量保形沉积。
  - **Spatial ALD（空间隔离式，如 ASM XP8 等高速旋转/多槽架构）**：晶圆在高速旋转下连续扫过被惰性气体幕墙（Gas Curtain）严格隔离的“前驱体 A 区 → 吹扫幕 → 前驱体 B 区 → 吹扫幕”，**时间吹扫被空间位移替代**，将单 Cycle 压缩至 $<0.5\,\text{s}$，等效生长速率飙升 5~10 倍！

---

### 2.3 薄膜内应力（Stoney 公式）与应变硅工程

任何沉积薄膜均带有残余应力 $\sigma_f$（负值为**压应力 Compressive**，薄膜企图膨胀将硅片弯成凸面；正值为**张应力 Tensile**，薄膜企图收缩将硅片弯成凹面）。晶圆厂普遍通过激光扫描晶圆曲率半径变化，采用 **Stoney 公式** 精准反演膜层应力：
$$\sigma_f = \frac{E_s}{6(1 - \nu_s)} \frac{t_s^2}{t_f} \left(\frac{1}{R} - \frac{1}{R_0}\right)$$
其中 $E_s/(1-\nu_s)$ 为硅衬底双轴弹性模量（$(100)$ 硅约为 $180.5\,\text{GPa}$），$t_s$ 为晶圆厚度（300mm 标准厚度约 $775\,\mu\text{m}$），$t_f$ 为膜厚，$R_0, R$ 为沉积前后的晶圆曲率半径。

- **应力两大来源**：
  1. **热失配应力 $\sigma_{th} = \frac{E_f}{1-\nu_f}(\alpha_f - \alpha_s)(T_{dep} - T_{room})$**：由薄膜与硅热膨胀系数 $\alpha$ 差异在降温时产生；
  2. **本征应力 $\sigma_{int}$**：在 PECVD/PVD 中，若增加低频射频（Low-Frequency RF，典型 $380\sim 400\,\text{kHz}$）激励重离子高速轰击刚沉积的薄膜表面，会产生类似铁匠锤击的**“原子喷丸效应（Atomic Peening）”**——将多余原子强行楔入晶格间隙，产生高达 $-1\sim -3\,\text{GPa}$ 的强压应力；反之，高温 LPCVD $\text{Si}_3\text{N}_4$ 在晶粒合并收缩或释放氢键时则表现为 $+1.0\sim +1.5\,\text{GPa}$ 的极强张应力。
- **应力失控危机与正面工程利用（Strained Silicon）**：
  - **失效红线**：若 300mm 晶圆总翘曲度（Warp / Bow）因叠加厚膜应力超过 $150\sim 300\,\mu\text{m}$，光刻机静电/真空吸盘（Chuck）将无法吸平（导致严峻的散焦 Defocus），甚至在传送机械手上触发夹爪报警或直接膜层剥落（Peeling）。
  - **PMOS 嵌入式 SiGe（eSiGe）**：在凹槽源漏区选择性外延生长 $\text{Si}_{1-x}\text{Ge}_x$（$x \approx 0.25\sim 0.45$，由于 Ge 晶格比 Si 大约 $4.2\%$），强行挤压中间沟道产生 $>1\,\text{GPa}$ 单轴压应力，将空穴迁移率提升 $50\%\sim 80\%$；
  - **NMOS 高张应力衬层（CESL）**：利用富硅/低氢高张应力 $\text{Si}_3\text{N}_4$（结合 UV 固化驱氢收缩）产生 $+1.5\sim +2.0\,\text{GPa}$ 张应力拉伸沟道，降低有效质量并提高电子迁移率。

---

### 2.4 外延（Epi）前处理、选择性生长（SEG）与 GAA 超晶格极限

外延生长（典型气源为 $\text{SiH}_4$ / 二氯二氢硅 $\text{DCS, SiH}_2\text{Cl}_2$ + $\text{GeH}_4$ + $\text{HCl}$）的晶体完美度完全取决于硅基底接口原子洁净度与动力学匹配：

1. **原子级零氧零碳前清洗（Pre-clean）**：哪怕表面残留 $0.1$ 单层自然氧化硅或痕量碳污染，都会立刻破坏外延晶体模板导致**堆垛层错（Stacking Faults）**、孪晶乃至长出多晶硅颗粒。产线在进外延腔前须经过稀 HF 氢钝化（H-passivation），再进入与外延腔集成的真空预处理腔执行低温干法去氧化（如 **Siconi 技术**：利用 $\text{NF}_3/\text{NH}_3$ 等离子体在 $<100^\circ\text{C}$ 生成固体 $(\text{NH}_4)_2\text{SiF}_6$ 盐并在 $>120^\circ\text{C}$ 升华脱离，无高能轰击损伤）或 $800\sim 850^\circ\text{C}$ 原位 $\text{H}_2$ 烘烤。
2. **选择性外延（SEG）化学机理与加载效应**：在反应气体中精准掺入 $\text{HCl}$ 刻蚀气；由于 $\text{HCl}$ 对绝缘介质（$\text{SiO}_2/\text{SiN}$）表面刚刚落地的随机孤立晶核的刻蚀速率远高于单晶硅表面外延生长速率，从而实现“只在裸硅窗口长晶体、绝不在侧墙表面成核”。但大面积图形开口率差异会导致局部气相 $\text{HCl}/\text{DCS}$ 耗尽不均，诱发**图形加载效应（Pattern Loading Effect）**。
3. **GAA 纳米片超晶格极限（Matthews-Blakeslee 临界厚度）**：全环绕栅极（GAA）需要周期性外延生长 $3\sim 6$ 对厚仅 $7\sim 12\,\text{nm}$ 的 $\text{Si}/\text{Si}_{0.7}\text{Ge}_{0.3}$ 超晶格（随后侧向高选择比刻蚀掏空牺牲层 $\text{SiGe}$）。每层 $\text{SiGe}$ 厚度必须严格控制在 **Matthews-Blakeslee 临界厚度** 之下，否则压应力将以生成失配位错（Misfit Dislocations）的方式瞬间弛豫（Relaxation），毁掉整个沟道载流子迁移率。
4. **产线薄膜常规表征监控矩阵**：工程上利用 **椭圆偏振仪（Ellipsometry）** 测薄膜厚度与光学折射率 $n/k$、**X 射线反射率（XRR）** 测 $1\sim 20\,\text{nm}$ 超薄膜物理密度/厚度与粗糙度、**FTIR 傅里叶红外光谱** 追踪 $\text{Si}-\text{H}/\text{N}-\text{H}/\text{Si}-\text{CH}_3$ 键合密度、以及 **SIMS** 监控外延接口氧/碳沾污（必须 $< 10^{18}\,\text{atoms/cm}^3$）。

---

## 3. 典型量产故障排查（Troubleshooting）与工艺判断

| 产线异常现象 | 物理化学根因剖析 | 工程排查与机台级解决对策 |
| :--- | :--- | :--- |
| **高深宽比填充出现 Keyhole / Void** | 前驱体粘附系数过高造成槽口 Overhang；HDP D/S 比偏高导致削角不足；FCVD 低聚物预凝胶流动性下降 | 降低 HDP D/S 比加强 $\text{Ar}^+$ 削角；切换更低 $S_c$ 前驱体或引入 FCVD / Batch ALD；检查晶圆边缘 Bias 功率匹配度 |
| **膜层剥落（Peeling / Blistering）** | 界面残余污染物或水汽（$\text{OH}$）在后续升温退火时受热汽化膨胀；膜层内压/张应力与基底热失配超出界面结合韧性 | 强化前清洗与原位等离子体预处理；优化 PECVD 低频/高频功率比或掺碳过渡层调节界面应力至微压应力区间 |
| **CVD/ALD 颗粒暴增（Particle Burst）** | ALD 吹扫时间不足造成 A/B 前驱体在气相/喷淋头提前混合；PECVD 腔室内壁附着厚膜热震碎裂；管路冷凝 | 延长 Purge 时间并核查高速气阀（ALD Valve）密封磨损；缩短干法自清洗（$\text{NF}_3$ Remote Plasma Clean）周期；排查前驱体伴热线冷点（Cold Spot） |
| **选择性外延（SEG）表面加载效应（Loading Effect）** | 不同版图区域（大窗口 vs 密集小窗口）局部消耗前驱体速率不同，导致图形密度越高区域生长越薄甚至晶面（Facet）畸变 | 调整 $\text{HCl}/\text{DCS}$ 分压比平衡刻蚀与沉积；在总气流中添加大量 $\text{H}_2$ 载气抑制局部浓度耗尽；版图引入 Dummy Pattern 均衡开口率 |
| **PVD 靶材微电弧（Arcing）与溅射掉渣** | 介质膜反应溅射（如 $\text{TiN}$）时靶材非冲蚀区积聚绝缘层（Target Poisoning）积累电荷击穿放电；靶材边缘再沉积片剥落 | 调整反应气体 $\text{N}_2/\text{Ar}$ 滞后曲线（Hysteresis Curve）工作点；引入脉冲直流（Pulsed-DC）电源周期反偏中和电荷；定期执行靶材清理（Burn-in） |
