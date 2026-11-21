# 产线量测（Metrology）与缺陷检测（Inspection）全景解析

- **所属模块**：`03_unit_processes / 07_metrology_and_inspection`

## 1. 区分两个经常混用的词：Metrology vs Inspection
晶圆厂不直接生产硅的价值，但它有 **20%~30% 的设备与工时都在做监控（Process Control）**：

- **Metrology（量测 — 测“准不准”）**：在晶圆特定靶标（Target/Pad）上测量具体物理数值，如线宽 `CD`、膜厚 `Thickness`、套刻偏差 `Overlay`、轮廓倾角。数据送给 **SPC** 和 **APC** 做实时反馈补偿。
- **Inspection（缺陷检测 — 抓“坏不坏”）**：高速全片或大区域扫描，找出随机/系统物理缺陷（颗粒 Particle、刮伤 Scratch、断线 Open、桥接 Short、残留 Residue），输出缺陷坐标图（KLARF 文件）供复检与良率溯源。

---

## 2. 核心量测（Metrology）工具箱

| 量测项目 | 主流技术 | 原理与特点 | 适用场景 |
| :--- | :--- | :--- | :--- |
| **线宽与形貌 (CD)** | **CD-SEM**（关键尺寸扫描电镜） | 高分辨率电子束扫描成像，精度达亚纳米；缺点是有一定电子束损伤与测量慢 | 显影后 ADI、刻蚀后 AEI 线宽抽检 |
| **三维结构 (3D Profile)** | **OCD / Scatterometry**（光学临界尺寸/光谱偏振） | 测量周期性光栅的反射偏振光谱，配合物理光学模型反演 Fin 高度、侧壁角、CD；**非破坏且极快** | FinFET / GAA / 3D NAND 3D 剖面监控 |
| **膜厚与折射率 (n,k)** | **Ellipsometry（椭偏仪）/ Reflectometry** | 利用偏振光反射振幅比与相位差变化反算纳米级透明/半透明薄膜厚度；金属膜厚常用 **四探针方阻** 或 **皮秒超声（Picosecond Acoustics）** | 氧化、氮化、ALD/CVD 薄膜、CMP 残余膜厚 |
| **套刻对准 (Overlay)** | **IBO（基于图像）/ DBO（基于衍射）** | 测量本层光刻胶图形与下层图形之间的 $\Delta X, \Delta Y$ 偏移，精度亚纳米；通常在专门套刻靶标（Box-in-Box 或 AIM/光栅靶）上测量 | 光刻机每次曝光后的补偿反馈（Feedback） |
| **剖面切片（破坏性）** | **Dual-Beam FIB + TEM** | 聚焦离子束切割出几十纳米薄片，送透射电镜查看原子晶格排布 | 研发调参、严重异常定性（会毁掉该晶圆） |

---

## 3. 核心缺陷检测（Inspection）与复检（Review）流水线

1. **无图形晶圆检测（Unpatterned Wafer Inspection，如 KLA Surfscan）**：
   - 利用激光斜入射散射检测光片表面纳米级颗粒（LPD），用于监控洁净室、清洗机台与薄膜腔室掉粉（Particle Monitor）。
2. **有图形晶圆光学检测（Patterned Inspection）**：
   - **明场（Brightfield，宽带等离子体光源 BBP）**：分辨率极高，擅长捕捉极其微小的光刻桥接/断线缺陷，是 14nm 以下先进逻辑线核心主力（但单台设备极为昂贵且扫描较慢）。
   - **暗场（Darkfield，激光散射）**：只收集缺陷产生的散射光，速度快（WPH 高），适合抓颗粒、划伤与台阶大异常。
3. **电子束检测与自动缺陷分类（E-Beam Inspection & DR-SEM Review）**：
   - 光学检测给出可疑缺陷坐标后，送至 **DR-SEM（Defect Review SEM）** 高倍率拍照并用 AI/ADC（自动缺陷分类）判定是致命颗粒还是无害干扰（Nuisance）。
   - **电压衬度（Voltage Contrast, EBI）**：利用电子束扫描时开路/短路部位充电亮暗不同，专门抓肉眼和光学完全看不见的**隐性电学断路/漏电（如深孔未刻穿）**。
