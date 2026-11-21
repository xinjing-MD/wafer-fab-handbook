# 套刻精度（Overlay）数学建模、测量原理与高阶畸变修正

- **所属模块**：`03_七大核心工艺 / 01_光刻工艺`

---

## 1. 为什么 Overlay（套刻）往往比 CD（线宽）更难控？

光刻不仅要“印得细（CD）”，更要**“上下几十层电路严丝合缝对得准（Overlay）”**。
一般行业经验准则：
$$\text{Overlay Budget} \le \frac{1}{4}\sim\frac{1}{3} \text{ Minimum Half-Pitch}$$
在 5nm/3nm 节点（金属 Pitch ~21~24nm），上下层金属线与通孔的 Overlay 误差必须死守在 **$1.5\sim 2.0\,\text{nm}$（3σ）以内**——相当于在足球场大小的晶圆上以几毫米精度叠放几十层微米地图！一旦偏移超标，通孔就会扎偏短路或悬空开路（Edge Placement Error, EPE 失效）。

---

## 2. 两大套刻量测技术：IBO vs DBO

| 对比维度 | IBO（Image-Based Overlay，图像套刻） | DBO（Diffraction-Based Overlay，衍射套刻） |
| :--- | :--- | :--- |
| **代表系统** | KLA Archer 系列 | ASML YieldStar 系列 |
| **靶标图形** | **Box-in-Box** 或 **AIM（先进成像对准靶标）** | 成对上下叠置的微米级**周期光栅（Grating-over-Grating）**，附带人为预设微小偏移 $+d / -d$ |
| **测量原理** | 高倍光学显微镜直接拍照，通过算法计算外框（下层）与内框（上层）几何中心差值 $(\Delta X, \Delta Y)$ | 照射偏振光收集 +1 级与 -1 级衍射光强不对称度，光强差与套刻偏移量呈严格线性关系 |
| **核心优劣** | 直观、抗多层膜厚干涉畸变能力强；受光学像差与目标不对称影响 | **测量重复精度极高（< 0.15 nm）且速度极快**；但对下层光栅侧壁不对称形变较敏感 |

---

## 3. 套刻误差数学分解模型（Linear → High-Order）

测量出全片数百个位置点 $(\Delta x, \Delta y)$ 后，APC（先进过程控制）系统把复杂矢量场分解为两部分喂给光刻机进行实时逆向补偿：

### （1）片间网格参数（Inter-field / Grid Model）—— 控制工件台走位
- **平移（Translation $T_x, T_y$）**：整体 X/Y 偏置；
- **片内缩放（Wafer Scaling $S_x, S_y$）**：晶圆因为高温热处理或大应力薄膜沉积导致整体膨胀或收缩；
- **旋转与正交性（Rotation $R$ & Orthogonality $\theta$）**：X 轴与 Y 轴不成严格 90°。

### （2）曝光场内参数（Intra-field Model）—— 控制掩模台与投影透镜
- **曝光场放大倍率（Field Mag）与旋转（Field Rot）**：调节掩模台位置与扫描同步速度比；
- **梯形畸变（Trapezoid）与高阶多项式（CPE / High-Order CPE）**：由于双工件台动态扫描、透镜热像差（Lens Heating）以及 CMP 抛光引起的局部翘曲，现代先进节点使用 **每个曝光场独立的高阶 3 阶/5 阶多项式（CPE, Correction Per Exposure）**，由 ASML Scanner 内部压电变形镜实时微调波前进行点对点抵消。

> **工程警示**：注意区分 **Matched-Machine Overlay（MMO，不同光刻机混跑之间的套刻）** 与 **Single-Machine Overlay（SMO，同一台光刻机前后层对准）**。晶圆厂核心关键层往往在 MES 中锁定 **Tool Dedication（专机专用路线）**，减少跨机台镜头畸变指纹差异。
