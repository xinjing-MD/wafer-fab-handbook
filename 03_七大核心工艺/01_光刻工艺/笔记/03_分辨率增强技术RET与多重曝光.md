# 分辨率增强技术（RET）与多重曝光（SADP / SAQP）

- **所属模块**：`03_七大核心工艺 / 01_光刻工艺`

---

## 1. 当瑞利判据碰到物理天花板：为什么必须用 RET？

在 $193\,\text{nm}$ 浸没式光刻（ArFi, $NA = 1.35$）的光学物理极限下，即使把工艺因子 $k_1$ 榨干到单次曝光的理论衍射极限 $0.25$，最小可分辨半节距（Half-Pitch）也被物理定律锁死在：
$$\text{HP}_{\min} = 0.25 \times \frac{193\,\text{nm}}{1.35} \approx 35.7\,\text{nm} \quad (\text{对应最小节距 } P_{\min} \approx 71.5\,\text{nm})$$
计入物镜残余像差、光刻胶化学扩散模糊与工艺冗余余量，量产单次曝光实际 $k_1$ 下限通常停留在 $0.28\sim 0.30$（$\text{HP} \approx 40\sim 43\,\text{nm}$）。

随着 $k_1$ 逼近衍射红线，空间像对比度迅速恶化，光刻工程师必须死盯两个决定工艺窗口生死的量化指标：
1. **归一化图像对数斜率（NILS, Normalized Image Log Slope）**：
   $$\text{NILS} = w \cdot \left.\frac{d \ln I(x)}{dx}\right|_{\text{edge}}$$
   - NILS 衡量线条边缘光强由暗转亮的相对陡峭度。
   - 量产可靠窗口要求 **$\text{NILS} \ge 2.0\sim 2.5$**；一旦 NILS 跌破 $1.5$，微小的剂量波动或光子散粒噪声就会引发剧烈的线宽粗糙度（LWR）暴涨与随机桥接。
2. **掩模误差增强因子（MEEF, Mask Error Enhancement Factor）**：
   $$\text{MEEF} = \frac{\partial \text{CD}_{\text{wafer}}}{\partial (\text{CD}_{\text{mask}} / M)}$$
   - 其中 $M=4$ 为投影缩小倍率。常规图形 $\text{MEEF} \approx 1$；但当 $k_1 \to 0.25\sim 0.28$ 时，高阶衍射分量在光瞳外流失，**$\text{MEEF}$ 急剧飙升至 $3\sim 6$**。
   - 这意味着掩模版制造中区区 $1\,\text{nm}$（$1\times$ 等效）的偏差，投影到晶圆上会被放大成 $4\sim 6\,\text{nm}$ 的致命线宽漂移！

因此，先进光刻必须先依托 **RET（Resolution Enhancement Techniques）** 将单次曝光压至极限 $k_1 \approx 0.27\sim 0.28$ 并救回 NILS，再通过 **多重图形化（Multi-Patterning）** 将等效 $k_{1,\text{eff}}$ 强行压破 $0.25$ 物理底线。

---

## 2. 三大核心 RET 光学魔法与计算光刻演进

### 2.1 OAI（Off-Axis Illumination，离轴照明）与矢量偏振控制

```text
[传统垂直照明 vs 离轴双光束对称干涉光瞳对比]
  传统垂直照明 (Conventional):             偶极离轴照明 (Dipole OAI, sinθ = λ/2P):
      -1级        0级        +1级             0级(斜入射)              +1级(斜衍射)
        \         |         /                   \                        /
    -----[========O========]----- 物镜瞳面    ---[O====================O]--- 对称落入瞳面边缘！
    小Pitch下 ±1级全部飞出瞳外 (无像!)         双光束对称干涉：分辨率翻倍 + 离焦光程差完全抵消!
```

- **物理痛点**：传统垂直入射圆盘照明（Conventional $\sigma$）下，极小节距图形的 $\pm 1$ 级衍射角满足 $\sin\theta = \lambda / P > NA$，高阶衍射光全部飞出物镜收集孔径外，无法成像。
- **双光束对称干涉解法**：利用照明瞳面光阑或衍射光学元件（DOE）将光源改造为斜入射的**环形（Annular）、偶极（Dipole）、四极（Quasar）或 C-Quad**。当斜入射角满足 $\sin\theta_{\text{ill}} = \frac{\lambda}{2P}$ 时，**$0$ 级直流光与一侧 $+1$ 级衍射光对称贴着物镜瞳面边缘穿过**：
  - 分辨率上限翻倍（最高空间频率推进至 $2NA/\lambda$）；
  - 因 $0$ 级与 $+1$ 级光线相对光轴对称，离焦 $\Delta z$ 引起的波前相位漂移在两束光之间完全一致并相互抵消（$\Delta\phi_0 = \Delta\phi_{+1}$），使该主节距下的**理论焦深（DOF）趋于无穷大**！
- **高 $NA$ 矢量偏振效应（TE vs TM）**：在 $NA = 1.35$ 浸没光刻中，两束干涉光线在胶内交会角逼近 $90^\circ$。若光波电场平行于入射面（TM 偏振），斜交电场的矢量点积趋近于零（$\vec{E}_0 \cdot \vec{E}_1 \propto \cos 90^\circ = 0$），干涉对比度归零！因此 ArFi 偶极照明必须配套**方位角切向 TE 偏振（Azimuthal TE Polarization）**锁死干涉对比度。
- **版图设计代价（1D Gridded Layout）**：极限偶极照明（如 X-Dipole）虽能把垂直密线印到极致，却对水平方向线条近乎失明。这一光学硬限制直接倒逼芯片设计自 $20\,\text{nm}/14\,\text{nm}$ 节点起取消任意 2D 弯曲布线，全面实施 **单向栅格化设计规则（1D Gridded Design Rules）**。

### 2.2 PSM（Phase-Shift Mask，相移掩模）
由 Marc Levenson 等人于 1982 年提出，借助 $180^\circ$ 反相干涉相消榨干暗区底部余光、陡峭化边缘：
- **Alt-PSM（交替型相移掩模）**：
  - 将相邻两条透光缝隙中的一条石英玻璃精确刻深 $d = \frac{\lambda}{2(n_{\text{quartz}} - 1)}$，产生 $\pi$（$180^\circ$）相位翻转。
  - 两束反相光在遮光铬条下方交叠抵消至严格零光强。短板是在复杂二维转角与 T 型交叉处必然发生 $0^\circ$ 与 $180^\circ$ 相位冲突（Phase Conflict），需补做修剪掩模（Trim Mask）。
- **Att-PSM（衰减型相移掩模，如 $6\%$ MoSi 掩模）**：
  - 12 寸产线最普及的掩模方案！将不透光铬膜替换为半透明的**硅化钼（MoSi）薄膜**（透射率 $6\%$ 且反相 $180^\circ$）。
  - 透过的 $6\%$ 反相弱光恰好中和亮区衍射渗入暗区的余辉，拉高 NILS 且无相位冲突；**调机警示**：过高曝光剂量会使大暗区内的反相干涉次峰突破阈值，意外印出虚假的**旁瓣凹坑（Side-lobe Printing）**。

### 2.3 OPC、SRAF 与 SMO / ILT（计算光刻闭环）
- **邻近效应物理成因**：物镜低通滤波截断高频 + 光刻胶酸扩散模糊 + 刻蚀负载效应，导致晶圆实测图形出现**线端缩短（Line-end Shortening）、直角圆化、以及孤立线与密集线线宽差（Iso-Dense Bias）**。
- **OPC（光学邻近修正）工程流**：采样数千组校准测试图形（Calibrated Gauges）拟合光学+光刻胶+刻蚀物理紧凑模型（Compact Model），在掩模数据准备（MDP）中自动切片迭代形变——线端外扩成**锤头（Hammerhead）**、拐角加**衬线（Serif）**、孤立线两侧插入亚分辨极限（不曝光成型）的**辅助散射条（SRAF）**，把孤立线“伪装”成密集阵列以共享同一焦深窗口。
- **SMO 与 ILT 突破**：
  - **SMO（光源-掩模联合优化）**：利用自由曲面微反射镜阵列（如 ASML FlexRay 数千像素可编程光瞳）与掩模网格联合反演，榨干系统最后 $1\%$ 工艺窗口；
  - **ILT（逆向光刻技术）**：求解偏微分反问题产出酷似等高线的**曲线型掩模（Curvilinear Mask）**，显著降低 MEEF 并成倍拓宽工艺窗口。直到 **多波束掩模写版机（MBMW，如 $50\,\text{keV}$ 26 万+电子束并行写入）** 取代单束可变矩形电子束（VSB）后，ILT 才克服写版时间爆炸瓶颈，全面落地 $5\,\text{nm}/3\,\text{nm}$ 与 EUV 核心层。

---

## 3. 突破单次曝光极限：LELE vs SADP / SAQP 多重图形化

当目标半节距低于 $36\,\text{nm}$ 时，产线通过多次光刻或自对准薄膜沉积-回刻把密集节距物理劈分倍增：

```text
[SADP 自对准双重图形化核心工艺演进示意]
Step 1: 芯轴光刻 + 修剪刻蚀 (节距 2P)       [#####]         [#####]         [#####]
Step 2: ALD 保形沉积 Spacer (厚度 t = CD)   |#####|         |#####|         |#####|
Step 3: 顶/底 Spacer 各向异性回刻           | [#####] |     | [#####] |     | [#####] |
Step 4: 选择性掏空剥离芯轴 (Mandrel Pull)   |         |     |         |     |         |  --> 节距减半为 P !
Step 5: Cut Mask 光刻+刻蚀切断闭合环路端头   |         |     |               |         |
```

| 多重图形化技术 | 核心工艺流程 | 等效 $k_{1,\text{eff}}$ 与适用节点 | 核心量产痛点与控制要点 |
| :--- | :--- | :--- | :--- |
| **LELE / LELELE**<br>（光刻-刻蚀循环） | 按奇偶拆分 $2\sim 3$ 张掩模（Color A/B/C），分别独立“涂胶-曝光-刻蚀进硬掩模”，间距错位减半 | $k_{1,\text{eff}} \ge 0.13\sim 0.17$<br>$20\,\text{nm}/14\,\text{nm}$ 逻辑局部金属布线 | **套刻误差 1:1 恶化为线距不均（Pitch Walking）**：两次曝光错位 $\Delta$ 致使奇偶间距变为 $S+\Delta$ 与 $S-\Delta$，推高耦合电容并诱发 TDDB 击穿 |
| **SADP**<br>（自对准双重图形化） | 光刻节距 $2P$ 芯轴（a-Si 或 ACL）$\to$ ALD 保形沉积薄侧墙（Spacer，$\text{SiO}_2/\text{SiN}$）$\to$ 顶底回刻露芯轴 $\to$ 掏空芯轴，**只留两侧对称 Spacer 作硬掩模** | $k_{1,\text{eff}} \approx 0.125$<br>$14\,\text{nm}/10\,\text{nm}$ 鳍片与密集 M1/M2 主力 | **无光刻套刻误差！** 最终线宽由 ALD 膜厚决定；须控制芯轴 CD 防止内/外间距不对称，并配 **Cut/Block Mask** 切断闭合环路端头 |
| **SAQP**<br>（自对准四重图形化） | 连续嵌套两遍 SADP：第 1 轮 Spacer 掏空芯轴后充当第 2 轮芯轴，再长第 2 轮 Spacer 回刻掏空，**密度 $\times 4$ 倍增** | $k_{1,\text{eff}} \approx 0.065\sim 0.08$<br>用 $193\,\text{nm}$ ArFi 硬做出 $7\,\text{nm}/10\,\text{nm}$ FinFET 鳍片（Pitch $24\sim 30\,\text{nm}$） | 工序极端冗长（1 张芯轴掩模 + 2~3 张 Cut 掩模 + 2 轮 ALD + 4~5 步精密刻蚀），缺陷累加与 Cycle Time 暴涨 |

### 3.1 工程权衡：193i SAQP vs EUV 单次曝光的经济学拐点
- **SAQP 的复杂性瓶颈**：在 $7\,\text{nm}$ 初期，ArFi + SAQP 虽省去 EUV 购机折旧，但单一密金属层需 4~5 张掩模与 30 余道沉积刻蚀步骤，多张 Cut Mask 交叉带来的 EPE 良率风险极高。
- **EUV 单次曝光的经济反超**：随着 EUV $0.33\,\text{NA}$ 光源功率跨过量产门限，TSMC N7+/N5 及 Samsung 5nm 果断在关键密层用 **1 次 EUV 单次曝光替代复杂 SAQP**——省下 3 张掩模及数十步缺陷累加风险，依据综合良率模型 $Y \propto e^{-D_0 A \cdot N_{\text{steps}}}$ 与 Cycle Time 缩短在总经济效益上实现反超。

### 3.2 多重曝光典型异常与 Troubleshooting 速查

| 异常指纹 | 物理/工艺根因 | 工程排查与处置动作 |
| :--- | :--- | :--- |
| **周期性奇偶线距不等（Pitch Walking）** | LELE 套刻偏置 $\Delta_{\text{OVL}} \ne 0$；或 SADP/SAQP 芯轴 CD 刻偏挤压相邻空隙 | LELE 收紧 APC 套刻反馈；SADP/SAQP 监控芯轴 AEI CD 并前馈微调 ALD Spacer 膜厚补偿 |
| **Cut Mask 端头粘连或切伤邻线** | Cut 掩模套刻超标或边缘圆化严重，未切透侧墙或误侵占隔壁主线 | 采用双色高选择比 Cut 方案，并在 MES 中锁定 Cut 掩模对芯轴层的专机专用路线（Tool Dedication） |
| **侧墙掏空阶段倒塌（Spacer Collapse）** | 芯轴高宽比过高致使剥离甩干时毛细力拉倒薄 Spacer，或 ALD 侧壁覆盖不均 | 降低芯轴高度压低 AR；将掏空后干燥工艺切换为超临界 $\text{CO}_2$ 或马兰戈尼低表面张力干燥 |
