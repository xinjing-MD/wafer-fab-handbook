# 12 寸逻辑晶圆厂 CMOS 电子流转卡（Run Sheet / Process Flow 实战范本）

> **教学意义**：教科书按单项工艺分章节讲“光刻、刻蚀、薄膜”，但新手进厂后最大的困惑是：**这七大工艺在真实 12 寸产线里究竟是如何按先后顺序交叉重入、在哪里插湿法清洗、在哪里插光学/电镜量测、哪里卡 Q-Time 死线的？**
> 本范本以现代 **28nm HKMG Gate-Last 逻辑制程（简化典型骨架）** 为蓝本，给出从裸硅片投片到 WAT 出厂的 **48 步核心工程流转表**（实际量产含多重图形与 10+ 层金属通常达 800~1,200+ 步）。

---

## 一、FEOL 前道晶体管制造流转表（Step 01 – Step 26）

| Step | 模块 | 工序名称 | 典型机台类别 | 核心工艺与参数目标（工程典型窗） | 在线监控 / 量测（Metrology）与 Q-Time 死线 |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **01** | Start | 300mm 来料与激光打码 | Sort / OCR | $p/p^-$ 或 $p/p^+$ 外延硅片（775μm），校验 T7 码 | Surfscan 抽检 LPD 颗粒 |
| **02** | Clean | 初始前清洗 | Wet Clean | RCA SC-1 + SC-2 + DHF（去自然氧化层） | **Q-Time ≤ 4h** 进炉管防自然氧化再生 |
| **03** | Thermal | 垫氧化层生长（Pad Ox） | 卧/立式炉管 | 干氧 $850\sim 900^\circ\text{C}$，厚 `5~8 nm`（缓冲 SiN 应力） | 椭偏仪（Ellipsometry）测膜厚 `±0.3 nm` |
| **04** | Dep | STI 硬掩模沉积 | LPCVD 炉管 | $\text{SiH}_2\text{Cl}_2 + \text{NH}_3$ @ $750^\circ\text{C}$，厚 `80~100 nm` | 椭偏仪测 SiN 膜厚与折射率 ($n \approx 2.0$) |
| **05** | Litho | 有源区（Active/OD）光刻 | Track + ArFi | 涂 BARC + ArF 光刻胶 + 曝光显影定义有源岛 | ADI：CD-SEM + Overlay + 宏观缺陷 |
| **06** | Etch | STI 浅沟槽干法刻蚀 | ICP 导体刻蚀 | 刻穿 SiN/Pad Ox → 刻硅深 `250~320 nm`，侧壁倾角 $84^\circ\sim 87^\circ$ | AEI：CD-SEM / OCD 查深宽与倾角；剥胶 + 湿洗 |
| **07** | Thermal | 衬垫热氧化（Liner Ox） | ISSG / 炉管 | **$1000\sim 1050^\circ\text{C}$** 圆化沟槽顶角，防止边角漏电双驼峰 | **Q-Time ≤ 2h**（STI 刻蚀清洗后立即衬垫氧化） |
| **08** | Dep | STI 绝缘填充（Gap Fill） | FCVD / HARP | 流动性填沟槽无空洞 + 蒸汽退火致密化（$500\sim 600\,\text{nm}$） | 薄膜应力 Bow 检测 + 无空洞截面抽检 |
| **09** | CMP | STI CMP 全局平坦化 | CMP（Ceria 浆料） | 磨除表面 $\text{SiO}_2$，高选择比精准停在 $\text{Si}_3\text{N}_4$ 上 | 残余 SiN 厚度片内均匀性监控 |
| **10** | Clean | 热磷酸剥离硬掩模 | 槽式湿法 | $160^\circ\text{C}\,\text{H}_3\text{PO}_4$ 剥除 $\text{Si}_3\text{N}_4$ + DHF 去 Pad Ox + 牺牲氧化 | 阶梯高度测量（Step Height）控制在 `< 2 nm` |
| **11** | Litho/Imp | **N-Well / P-Well 阱注入** | Track + 中高能注入 | 分别光刻掩模，多能量链式逆行阱注入（P/As 与 B） | 注入后灰化 + SPM 剥除碳化胶 + SC1 |
| **12** | Litho/Imp | 抗穿通与 $V_{th}$ 调整注入 | 光刻 + 注入 | 沟道区低能量精调表面浓度 | 四探针方阻监控测试片（Monitor Wafer） |
| **13** | Thermal | 阱区激活与缺陷修复 | RTP / Spike | $1000\sim 1050^\circ\text{C}$ 退火消除注入损伤 | 控片方阻与晶格缺陷检查 |
| **14** | Dep | 伪栅多晶硅沉积 | LPCVD | $620^\circ\text{C}$ 生长非晶/多晶硅（Poly `60~80 nm`）+ SiN 硬帽 | 膜厚与表面粗糙度检控 |
| **15** | Litho | **核心栅极（Gate）光刻** | Track + 193i | **全厂最高精度光刻层之一**（SADP/OPC 精印栅长 `25~30 nm`） | **ADI：CD-SEM + DBO Overlay**（超差直接 Rework！） |
| **16** | Etch | 栅极干法刻蚀 | ICP 刻蚀 | 精确停在底层极薄缓冲氧化硅上，垂直度 $\approx 89^\circ$ | **AEI：OCD + CD-SEM** 严格反馈给 APC |
| **17** | Dep | 偏置侧墙（Offset Spacer） | ALD | 极薄 $\text{SiN}/\text{SiOCN}$ `3~5 nm` | 椭偏测厚（控制后续 LDD 横向间距） |
| **18** | Litho/Imp | **LDD 轻掺杂 + 大倾角 Halo** | 低温/低能注入 | $0.5\sim 2\,\text{keV}$ LDD + $25^\circ\sim 35^\circ$ Quad 旋转 Halo | 注入束流校验 + 剥胶湿洗 |
| **19** | Dep/Etch | 主侧墙（Main Spacer） | ALD + RIE 回刻 | 沉积 `10~15 nm` 低 k SiOCN + 各向异性无 MASK 回刻 | OCD 侧墙宽度检查 |
| **20** | Epi | **PMOS e-SiGe 选择性外延** | Epi 外延腔 | 先刻凹槽 + Siconi 清洗 → 外延 $\text{Si}_{0.65}\text{Ge}_{0.35}\text{:B}$ 压应力源漏 | **Q-Time ≤ 1h**（清洗去自然氧化后进外延！）+ XRD 测 Ge% |
| **21** | Imp | NMOS 重掺 S/D 注入 | 大束流注入 | $\text{As}^+ / \text{P}^+$ $1\sim 5\times 10^{15}\,\text{cm}^{-2}$ | 剥胶清洗 |
| **22** | Thermal | **源漏毫秒级退火激活** | Spike + **LSA 激光** | Spike $1050^\circ\text{C}$ + LSA $1280^\circ\text{C}$（`< 1 ms`）高激活零扩散 | Monitor 控片四探针方阻 $R_s$ |
| **23** | Dep/CMP | ILD0 填充与伪栅露头 | FCVD + W/Ox CMP | 填满栅间间隙 + CMP 磨平露出多晶硅顶面 | CMP 残余高度光学监控 |
| **24** | Etch/Wet | **抽伪栅与 HKMG 替换（RMG）** | 湿法 + ALD + PVD | TMAH 掏空多晶硅 → 生长 `0.7 nm` IL + `1.8 nm` $\text{HfO}_2$ + PDA | **极严 Q-Time ≤ 1h**（界面层至 $\text{HfO}_2$ ALD 间不可暴露空气） |
| **25** | Dep/CMP | 功函数金属与金属栅填充 | ALD + CVD W + CMP | 分区填入 TiN（PMOS）/ TiAlC（NMOS）+ W 填满 + MG CMP | **FEOL 结束！** 测栅极高度与金属平整度 |
| **26** | Clean | FEOL 出区检查 | 明场光学检测 | 全面扫描前端缺陷，之后进入中段 MOL | KLA 明场 + DR-SEM |

---

## 二、MOL 中段接触与 BEOL 后道铜互连流转表（Step 27 – Step 48）

| Step | 模块 | 工序名称 | 典型机台类别 | 核心工艺与参数目标（工程典型窗） | 在线监控与跨区隔绝规范 |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **27** | Dep | 刻蚀阻挡层与 ILD0 沉积 | PECVD | 沉积 CESL SiN + 低 k 介质 `100~150 nm` | 膜厚与应力检查 |
| **28** | Litho | 接触孔（CA / TS）光刻 | Track + 193i | 定义源漏与栅极接触孔图形 | ADI：CD-SEM + Overlay |
| **29** | Etch | **SAC 自对准接触孔刻蚀** | CCP 介质刻蚀 | 高 $\text{SiO}_2/\text{Si}_3\text{N}_4$ 选择比刻穿暴露硅源漏与金属栅 | **EBI 电压衬度抽检**抓未刻通假孔 |
| **30** | Metal | **NiPt 金属硅化物（Salicide）** | PVD + 两步 RTP | 清洗去氧化层 → 溅射 NiPt → $280^\circ\text{C}\to$ 洗未反应金属 $\to 450^\circ\text{C}$ | **Q-Time ≤ 1h**（接触孔去氧化后立即进 PVD） |
| **31** | Metal | 接触孔栓塞填充与 CMP | ALD TiN + CVD W/Co + CMP | TiN 阻挡层 + CVD W 或 Co 填满接触孔 + W CMP 磨平 | 表面无 W 残余与划伤检查 |
| **32** | Dep | **M1 低 k（ULK）层间介质** | PECVD + UV Cure | 沉积掺碳多孔 SiCOH（$k \approx 2.5$）+ 紫外固化造孔 | **⚠️ 物理切换进入 BEOL Cu 隔离区**；测 $k$ 值与折射率 |
| **33** | Dep | TiN 金属硬掩模（TFMHM） | PVD | 沉积 `20~30 nm` TiN 阻挡 ULK 胺类毒化光刻胶 | 膜厚监控 |
| **34** | Litho | **M1 金属沟槽光刻** | Track + 193i/SADP | 精印第一层互连金属沟槽（最细金属节距层） | ADI：CD-SEM + Overlay |
| **35** | Etch | TiN 硬掩模开窗 + 剥胶 | 刻蚀 + 灰化 | 将 M1 线图刻入 TiN 金属硬掩模，洗净光刻胶 | AEI CD 检查 |
| **36** | Litho | **V0 / M1 通孔光刻（Via）** | Track + 193i | 涂 SOC/BARC 填平再对齐 M1 金属硬掩模开孔 | ADI 套刻检验 |
| **37** | Etch | 双大马士革介质共刻蚀 | CCP 刻蚀 + 湿洗 | 同步下切刻出 Via 通孔与 M1 Trench 沟槽（低温低损伤清洗） | AEI + 无残渣检控 |
| **38** | Dep | **PVD 阻挡层 + Cu 种子层** | Cluster Tool | 真空不断气连续沉积 `2 nm` TaN/Ta + `25~40 nm` Cu Seed | **Q-Time ≤ 2h**（Cu 极易氧化，立即送去电镀！） |
| **39** | Plating | **ECP 电化学镀铜 + Bevel Clean** | ECP 电镀机 | 三添加剂超填至过载 + **强制晶圆边缘 $2\,\text{mm}$ 湿法去铜与背面清洗** | 膜厚扫描 + 边缘金属污染监控 |
| **40** | Thermal | 铜晶粒粗化退火 | 低温炉管 / 退火腔 | $200\sim 300^\circ\text{C}$ 促使 Cu 晶粒长大降阻并释放应力 | 四探针薄层电阻监控 |
| **41** | CMP | **Cu CMP + Post-CMP 刷洗** | CMP + PVA Scrubber | Platen 1 去铜 → Platen 2 停在 TaN → Platen 3 精抛去阻挡层 + PVA 洗 | **Dishing/Erosion 台阶仪 + 明暗场缺陷全检** |
| **42** | Dep | 铜面还原与 SiCN 阻挡盖层 | PECVD | $\text{NH}_3/\text{H}_2$ 等离子体还原氧化铜 → 生长 SiCN 封帽（防铜向上扩散） | **Q-Time ≤ 1h**（CMP 暴露铜面后严防氧化降 EM 寿命） |
| **43** | Loop | **BEOL 重入循环（M2 ~ M10+）** | 重复 Step 32~42 | 逐层放大线宽与介质厚度（底层细连晶体管，中层走信号，顶层走厚铜电源） | 每层均经历 **光刻→刻蚀→镀铜→CMP→量测** 重入闭环 |
| **44** | Dep | 顶层钝化与 Al-Cu 焊盘 | PVD + PECVD | 铺设铝铜焊盘 Pad（防探针与引线键合氧化）+ USG/SiN 保护层 | 膜厚、焊盘尺寸检测 |
| **45** | Litho/Etch | Pad 开窗与背面减薄/清理 | 光刻 + 刻蚀 | 暴露焊盘窗口供扎针测试 | 外观显微全检 |
| **46** | Thermal | **FGA 合成气终极退火** | 炉管 | $400\sim 430^\circ\text{C}$ 通 $\text{H}_2/\text{N}_2$ 钝化前道界面悬挂键 | 严控上限防金属熔塌 |
| **47** | Test | **WAT 晶圆允收电学测试** | 半自动探针台 | 扎针切割道 TEG 测 $V_{th}/I_{dsat}/R_c/R_v/$TDDB | **全部参数落窗方可放行出厂** |
| **48** | Out | **CP 中测与 Wafer Map 分类** | 探针卡测试机 | 100% 扎针每颗产品 Die 输出 Bin 图，交封装厂切磨封装 | YMS 系统关联前端 FDC/SPC 闭环 |
