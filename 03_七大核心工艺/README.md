# 03 · 晶圆制造七大核心单项工艺 (`03_七大核心工艺`)

> 本目录是整个仓库的**知识核心区**。真实晶圆厂虽然要跑 700~1500 道工序，但本质上都是以下 7 大类基础单项工艺的“排列组合与循环往复（Re-entrant Flow）”。

---

## 七大工艺全景对照表

| 编号 | 模块 | 英文统称 | 核心任务（一句话） | 核心 KPI 指标 | 代表设备商 |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **01** | [光刻](./01_光刻工艺/README.md) | Lithography | 将掩模版电路图形转移到光刻胶上 | CD、Overlay、DOF、WPH | ASML、Nikon、TEL (Track) |
| **02** | [刻蚀与清洗](./02_刻蚀与清洗/README.md) | Etch & Wet Clean | 按图形“挖走”暴露的材料，并彻底清除残渣颗粒 | Etch Rate、选择比、形貌 Profile、颗粒度 | Lam Research、TEL、AMAT、中微、北方华创、盛美 |
| **03** | [薄膜沉积](./03_薄膜沉积/README.md) | Thin Film Deposition | 在晶圆表面“长出”纳米级介质、金属或单晶硅层 | 膜厚均匀性、台阶覆盖率 (Step Coverage)、应力 | AMAT、Lam、TEL、ASM、北方华创、拓荆 |
| **04** | [热处理与注入](./04_热处理与离子注入/README.md) | Thermal & Implant | 生长栅氧/高温激活退火，以及精确掺杂改变导电类型 | $R_s$ 方阻、结深 $X_j$、热预算、剂量均匀性 | AMAT、Axcelis、TEL、凯世通、屹唐 |
| **05** | [平坦化](./05_CMP平坦化/README.md) | CMP | 把凹凸不平的表面“磨平”，保证下一层光刻不失焦 | MRR 去除率、WIWNU、Dishing/Erosion、Scratch | AMAT、Ebara、华海清科 |
| **06** | [金属化与电镀](./06_金属化与电镀/README.md) | Metallization / ECP | 填充铜互连线与钨/钴通孔，把亿万晶体管连成电路 | 空洞 Void、线电阻 $R$、电迁移 (EM) 寿命 | AMAT、Lam、盛美、新傲/拓荆(阻挡层) |
| **07** | [量测与检测](./07_量测与缺陷检测/README.md) | Metrology & Inspection | 测量尺寸膜厚对准精度，并抓出致命颗粒/结构缺陷 | Precision (TMU)、灵敏度、检出率 | KLA、AMAT、Hitachi、中科飞测、精测 |
