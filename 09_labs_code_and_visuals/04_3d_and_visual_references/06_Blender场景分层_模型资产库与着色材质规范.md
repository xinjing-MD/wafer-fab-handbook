# 《现代晶圆厂三维建模参考手册》
## 第六章：Blender 场景分层、模型资产库与着色材质规范

---

### 6.1 Blender 生产级工程文件组织（Collections 分层架构）

在 Blender 中构建拥有数十台复杂设备、海量动力管网和自动化物流的大型晶圆厂场景时，若不进行严格的资产集合（Collection）分层，极易导致视口卡顿、内存溢出和动画管理混乱。

建议在 Blender `Outliner` 中建立如下标准生产级层级树：

```
Master Scene [Scene Collection]
│
├── 00_WORLD_ORIGIN & DATUM (全球基准坐标系 / 地坪 0.000m 基准轴)
│
├── 01_ARCH_SHELL (建筑主体与土建结构)
│   ├── Arch_WaffleSlab (现浇钢筋混凝土 1.0m 华夫板与立柱群)
│   ├── Arch_Subfab_Floor (Subfab 地面防腐环氧地坪与排水明沟)
│   ├── Arch_RaisedFloor_Plates (600x600mm 铝合金实心板/穿孔板/支架阵列)
│   ├── Arch_Bulkhead_Walls (50mm 夹芯彩钢板隔墙系统与检修门)
│   └── Arch_Ceiling_FFU_Grid (T-Bar 铝合金龙骨天花板与 FFU 滤网阵列)
│
├── 02_AMHS_LOGISTICS (空中自动化物流网络)
│   ├── AMHS_Monorail_Tracks (天轨型材主干道、弯道与道岔机构)
│   ├── AMHS_Track_Hangers (天花吊架结构钢吊杆与防晃斜撑)
│   ├── AMHS_Vehicles_OHT (天车车体、导向轮、非接触供电集电靴)
│   ├── AMHS_Hoist_Armatures (天车卷扬钢带、升降四轴骨架与抓手夹爪)
│   ├── AMHS_FOUP_Pods (300mm 晶圆传送盒本体、前门板、提手)
│   ├── AMHS_Stockers (巨型自动化立体仓储立库与内部堆垛手臂)
│   └── AMHS_UTB_Buffers (悬吊式轨下/轨侧临时晶圆盒缓存托盘)
│
├── 03_EQUIPMENT_CLEAN_BAY (核心工艺机台前端与主体)
│   ├── EQ_Litho_ASML_EUV (ASML EUV/DUV 光刻机台本体、蔡司镜筒、载物台)
│   ├── EQ_Litho_TEL_Track (TEL LITHIUS 涂胶显影机、旋转杯、热烘板)
│   ├── EQ_Etch_Lam_SenseI (Lam 刻蚀平台、VTM 真空室、3口 EFEM 前端)
│   ├── EQ_Depo_AMAT_Endura (AMAT Endura PVD 多边形真空溅射机群)
│   ├── EQ_Depo_AMAT_Producer (AMAT Producer GT 双生腔 PECVD/ALD 机台)
│   ├── EQ_CMP_AMAT_Reflexion (AMAT CMP 研磨大盘、4组抛光头、修整器)
│   ├── EQ_Diff_Axcelis_Implanter (高能离子注入机、真空分析磁铁、电离腔)
│   ├── EQ_Diff_TEL_Furnace (立式高温扩散退火炉、升降碳化硅晶圆舟)
│   ├── EQ_Wet_TEL_Celesta (单片喷淋旋转清洗机台、耐腐蚀外罩)
│   └── EQ_Metro_KLA_Inspection (KLA 29xx/39xx 宽波段光学检测仪、CD-SEM)
│
├── 04_SUBFAB_UTILITIES (洁净下层动力机电设备与管道丛林)
│   ├── Utility_Vacuum_DryPumps (Edwards/Pfeiffer 干式机械真空泵立体机架)
│   ├── Utility_Scrubbers_POU (尾气电热/等离子裂解洗涤中和塔)
│   ├── Utility_Chillers_Loop (高精度水冷回路管线与恒温水箱机柜)
│   ├── Utility_Gas_Panels_VMB (特气二次分配阀门箱、Swagelok 不锈钢特气管)
│   ├── Utility_UPW_PVDF_Piping (高纯水透明 PVDF 循环管道回路)
│   └── Utility_CableTrays (重型金属网格强弱电电缆桥架与接地铜排)
│
├── 05_CHARACTERS_PROPS (洁净室人机工程与环境道具)
│   ├── Props_Engineers_BunnySuits (身穿连体无尘服、护目镜、口罩的工程技术人员)
│   ├── Props_Mobile_Carts (手动防静电不锈钢晶圆推车、维修工具车)
│   ├── Props_Console_Islands (机台外置悬臂触摸屏、人体工学键盘工作站)
│   └── Props_Cleanroom_Details (无尘室专用防静电吸尘器、粘尘垫、警示标贴)
│
├── 06_LIGHTING_RIGS (全厂专业灯光照明系统)
│   ├── Light_Litho_Yellow (589nm 琥珀色低压钠灯光谱防感光照明)
│   ├── Light_General_White (5000K 高显色无尘室专用泪珠状 LED 灯条)
│   ├── Light_Equipment_Towers (各机台红/黄/绿/蓝四色 LED 运行指示灯塔)
│   └── Light_Plasma_Emitters (刻蚀/沉积腔体内部等离子体放电彩色辉光照明)
│
└── 07_CAMERAS_CINEMATIC (导播机位与电影级运镜轨道)
    ├── Cam_Overview_Crane (全厂超大广角飞越俯瞰推拉机位)
    ├── Cam_OHT_POV_Chasing (紧随天车穿梭第一人称跟随追焦机位)
    ├── Cam_EFEM_Macro_Wafer (机械手抓取晶圆微距超精细浅景深微雕镜头)
    └── Cam_Plasma_SlowMo (反应腔内部等离子轰击高帧率特写机位)
```

---

### 6.2 关键资产轴心点（Pivot Point / Origin）设立规范

为确保后续机械手臂绑定（Rigging）、约束（Constraints）以及 OHT 路径跟随正常运作，所有核心模型在导出前必须统一轴心点：

1. **机台总体（Mainframe Blockout）：**
   - **Origin 放置规则：** 贴合在机台正前方地面（$Z=0.000\text{m}$），位于正中央 Load Port 的前沿水平投影中心。
   - **朝向规范：** 正向（+Y 或 -Y）严格平行于洁净走廊法线方向，确保拼装时与 Bulkhead 墙面对齐。

2. **FOUP 晶圆传送盒：**
   - **Origin 放置规则：** 放置于 FOUP 底盘三颗定位球销构成的等边三角形几何中心，且位于最底面接触面上（$Z=0.000$）。
   - **对齐意义：** 当 FOUP 坐标与 Load Port 上的对接虚拟体（Empty Object）重合时，3 颗 SEMI E57 定位销刚好完美嵌入底盘 V 型凹槽。

3. **300mm 硅晶圆片（Wafer）：**
   - **Origin 放置规则：** 严格位于 300mm 晶圆圆盘顶面正中心（$X=0, Y=0, Z=0$）。
   - **朝向：** “V”型定向缺口（Notch）默认指向正负 X 轴方向，便于 Pre-Aligner 旋转寻心动画的度数驱动。

4. **OHT 天车车体（Vehicle）：**
   - **Origin 放置规则：** 位于车体顶部中心与天车铝合金导轨横截面中心线的物理切点处。
   - **动画驱动：** 使得天车可直接添加 `Follow Path` 路径约束，直接贴合由 Bezier 曲线绘制的天轨中轴线运行。

---

### 6.3 模块化 Kitbash 资产库清单（快速搭建全厂必备预制件）

建议优先在 Blender 中制作并封装为资产库（Asset Browser）的 6 大工业预制套件：

| 资产预制件名称 | 标准工程尺寸规格 | 面数预算 (LOD0) | 材质着色属性 | 作用与装配方式 |
| :--- | :--- | :--- | :--- | :--- |
| **穿孔架高地板板件**<br>(Perforated Tile) | $600\text{mm} \times 600\text{mm} \times 55\text{mm}$<br>(带 64 或 100 个倒角圆形落风孔) | 1,200 三角面 | 浅灰哑光环氧粉末涂层<br>(防静电 PVC 贴面) | 通过 Blender Array 阵列修改器铺满全厂走廊与操作湾地面 |
| **FFU 风机过滤单元**<br>(Fan Filter Unit) | $1175\text{mm} \times 575\text{mm} \times 320\text{mm}$<br>(带密布百叶铝边框与白色超细微滤纸) | 800 三角面 | 阳极氧化铝合金拉丝<br>+ 白色致密褶皱滤纸 | 阵列在天花板 T-Bar 龙骨矩阵中，提供自发光背景与漫反射光 |
| **SEMI E15.1 Load Port**<br>(标准装载口模块) | $480\text{mm}(\text{W}) \times 520\text{mm}(\text{D}) \times 850\text{mm}(\text{H})$<br>(带 3 颗定位销、开门机构缝隙、LED 灯) | 4,500 三角面 | 304 砂光不锈钢板<br>+ 黑色防磨工程塑料台面 | 拼装在所有机台 EFEM 前端，统一机台装载交接标准化形态 |
| **OHT 天轨直线与弯道型材**<br>(Monorail Track Profile) | 截面 $100\text{mm} \times 160\text{mm}$<br>(带双侧导向凹槽与底部开缝) | 200 面/米 | 银白色电泳喷涂铝合金<br>+ 侧边贴有黄色刻度条码带 | 配合 Curve 曲线变形修改器生成全厂纵横交错的立体空中轨道网络 |
| **Swagelok 特气不锈钢双卡套接头**<br>(Tube Fitting & Manifold) | 管径 1/4" 与 1/2"<br>(微型 90° 弯头、三通、手动隔膜阀) | 1,500 三角面 | 316L VIM/VAR 高纯不锈钢<br>(高光镜面金属，略带车削微细纹) | 大量阵列并拼接在 Service Chase 维护后廊与机台背后气路板上 |
| **机台四色运行状态指示灯塔**<br>(Signal Light Tower) | 高度 $450\text{mm}$，直径 $\Phi 60\text{mm}$<br>(红、黄、绿、蓝 4 节圆柱菲涅尔透镜) | 1,800 三角面 | 柱体为乳白哑光工程塑料<br>各节内部带强发光体 (Emission) | 竖立安装在每台机器 EFEM 前脸正上方，标识设备状态 |

---

### 6.4 电影级工业材质着色器（Shaders & Materials）节点参数指南

在 Cycles / EEVEE Next 渲染管线中，使用 Blender 原生 `Principled BSDF` 配合程序化节点制作以下 6 大关键半导体材质：

#### 1. 洁净室 589nm 琥珀色防感光黄光照明 (Litho Safe Light)
- **物理机理：** 光刻胶（Photoresist）对低于 450nm 的蓝光和紫外线极度敏感，因此曝光区必须完全剔除紫外与蓝光波段，使用单色低压钠灯光谱（589nm）。
- **Blender 节点设置：**
  - 使用 `Emission`（自发光）材质或 `Area Light` 面积光。
  - **Color（RGB）：** 设为高纯度琥珀金黄色：`Hex: #FFA800`，RGB: `[1.000, 0.658, 0.000]`。
  - **Color Temperature（黑体色温）：** 约 2200K，但建议直接用 RGB 锁定纯度，严禁掺杂任何蓝色或冷白微光。
  - **Strength（强度）：** 泪珠灯管设为 12.0 - 20.0，赋予洁净走廊一种极具未来感与科技神圣感的金黄静谧氛围。

#### 2. 300mm 硅晶圆极薄干涉彩虹薄膜着色器 (Wafer Thin-Film Iridescence)
- **视觉特征：** 硅晶圆表面是一面反射率极高的黑色镜面，但当表面沉积了数十至数百纳米厚的 $\text{SiO}_2$ 或 $\text{Si}_3\text{N}_4$ 介质层时，白光反射会发生强烈的**薄膜干涉（Thin-Film Interference）**，随着观察视角的变化泛出灿烂的彩虹光晕（孔雀绿、深紫红、明黄相间）。
- **Blender 节点网络搭建方案：**
  ```
  [Texture Coordinate] -> [Fresnel / Layer Weight (Facing: 0.65)]
                                      |
                                      V
  [Mapping (Scale 1.0)] -> [Wave Texture (Rings / Spherical)] -> [ColorRamp (虹彩渐变色卡)]
                                                                         |
                                                                         V
                                                            [Principled BSDF]
                                                            - Base Color: 纯黑 (#050505)
                                                            - Metallic: 0.95
                                                            - Roughness: 0.025 (极光滑镜面)
                                                            - Coat Weight: 1.0 (清漆层)
                                                            - Coat Roughness: 0.01
                                                            - Coat IOR: 1.46 (对应 SiO2 折射率)
                                                            - Emission Color: 连入 ColorRamp (极微弱 0.08)
  ```
  - *ColorRamp 关键色标设置：* 0.00(墨黑) $\rightarrow$ 0.25(翠绿 `#00FF88`) $\rightarrow$ 0.50(紫红 `#D800FF`) $\rightarrow$ 0.75(橙金 `#FFAE00`) $\rightarrow$ 1.00(湖蓝 `#00D4FF`)。

#### 3. 半透明防静电茶色聚碳酸酯 (Smoked ESD Polycarbonate - FOUP 盒壳)
- **视觉特征：** 高折射率塑料，带有深灰色、茶褐色或琥珀色半透明质感，表面略带轻微漫散射磨砂感，能模模糊糊透视看到内部水平叠放的硅晶圆银白色边缘。
- **Blender 核心参数：**
  - **Base Color：** 浅茶褐灰色（`Hex: #4A4036`，RGB: `[0.29, 0.25, 0.21]`）。
  - **Metallic：** 0.00。
  - **Roughness：** 0.12 - 0.15（微漫反射哑光光泽，并非完全通透的高光玻璃）。
  - **IOR（折射率）：** 严格设为 **1.586**（聚碳酸酯 PC 的物理精确 IOR）。
  - **Transmission Weight（透光度）：** **0.82 - 0.88**。
  - **Volume Absorption（体积吸收节点，连入 Material Output 的 Volume 端口）：**
    - Color：浓茶黄色（`Hex: #7A5826`）。
    - Density（密度）：12.0（产生边缘厚处颜色深暗、薄壁处透光的真实体积厚度感）。

#### 4. 砂光不锈钢与阳极氧化铝合金 (Chamber Body & Machine Panels)
- **304/316 砂光不锈钢（EFEM 面板、Load Port）：**
  - Base Color：纯金属白灰（RGB: `[0.85, 0.85, 0.85]`）。
  - Metallic：1.00。
  - Roughness：0.28。
  - **Anisotropic（各向异性拉丝）：** 0.65，Anisotropic Rotation：0.25。配合一条细微的线性 Bump 贴图，模拟机械表面水平拉丝砂光痕迹。
- **阳极氧化白铝（真空腔体、机械手臂）：**
  - Base Color：略偏冷灰白（RGB: `[0.78, 0.80, 0.82]`）。
  - Metallic：1.00。
  - Roughness：0.35（柔和的高级哑光金属质感，不产生刺眼的高光小斑点）。

#### 5. 等离子体辉光自发光材质 (Plasma Glow Emitters)
- **Blender 节点设置：**
  - 将材质表面直接连接 `Emission` 节点，或者在反应腔正中央放置一个扁平椭球体（半长轴 150mm，扁平高度 20mm），赋予 `Principled Volume`（体积发光）或高强度面自发光。
  - **刻蚀氟碳等离子体（Fluorocarbon）：** 深蓝紫色（`Hex: #3800FF`，Strength: 35.0）。
  - **刻蚀含氯等离子体（Chlorine）：** 亮蓝绿色（`Hex: #00FFC4`，Strength: 45.0）。
  - **氧气灰化等离子体（Oxygen）：** 柔和紫粉色（`Hex: #FF26A8`，Strength: 25.0）。
  - **Cycles 渲染设置：** 开启渲染设置中的 `Compositor`，添加 `Glare`（辉光）节点（类型选 `Fog Glow`，阈值 1.5，大小 8），渲染出等离子体向周围金属内壁映照出的强烈的工业漫射霓虹感。

---

### 6.5 Blender 动画机构绑定（Rigging）与运动学约束推荐

为了实现自动化机械手和 OHT 天车的毫秒级联动，推荐在 Blender 中采用以下约束方案：

1. **OHT 天车沿轨道巡航：**
   - 提取天轨三维模型的中轴线边缘，按快捷键 `P` 分离并转化为一条 3D `Bezier Curve`（贝塞尔平滑曲线）。
   - 为 OHT 天车父级空物体（Empty）添加 **`Follow Path`（跟随路径）** 约束，勾选 `Curve Radius` 与 `Follow Curve`。
   - 通过在 Curve 属性的 `Path Animation` 中为 `Evaluation Time`（评估时间）打关键帧，可精准控制天车在不同区域的巡航速度、转弯减速以及停止位置。

2. **凯夫拉悬吊带伸缩与抓手下落：**
   - 抓手（Gripper）作为独立子级，添加 **`Limit Location`（限制位置）** 约束，锁定其 X 和 Y 轴平移，仅释放垂直 Z 轴平移。
   - 4 条悬吊黑带可采用一个简单的包含 2 节骨骼的骨架（Armature），骨骼头固定在天车机箱卷筒，尾部应用 **`Stretch To`（拉伸至）** 约束指向抓手的挂钩顶点。当抓手在 Z 轴下落时，4 条扁平带会自动以完美的物理对齐方式垂直拉长伸出。

3. **EFEM 双关节 SCARA 机械手逆向运动学（IK 绑定）：**
   - 建立 3 根骨骼链：`Bone_Base`（垂直升降轴） $\rightarrow$ `Bone_Arm1`（大臂水平旋转） $\rightarrow$ `Bone_Arm2`（小臂水平旋转） $\rightarrow$ `Bone_Fork`（承托晶圆的末端叶片）。
   - 在 `Bone_Arm2` 上添加 **`IK`（Inverse Kinematics / 逆向运动学）** 约束，目标（Target）指向一个独立晶圆控制柄空物体（`Ctrl_Wafer_Target`），极向目标（Pole Target）用于锁定肘部向外翻折。
   - 为晶圆自身添加 **`Child Of`（子级于）** 约束，将目标分别设为“FOUP槽位”、“机械臂叶片”、“机台反应台”。通过在动画时间轴上关键帧切换子级约束的 `Influence`（从 0.0 瞬变到 1.0），即可实现晶圆在不同设备间的无缝机械拾取与递交。
