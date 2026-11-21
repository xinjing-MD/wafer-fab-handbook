# AMHS 自动物料搬运系统：OHT 天车、Stocker 与 FOUP 规范

- **所属模块**：`06_fab_automation_and_cim / 01_amhs_and_oht`

## 1. 为什么 12 寸晶圆厂必须全自动化搬运？
一个装满 25 片 300mm 硅片的 **FOUP** 重约 **8~9 kg**，内部承载着价值数十万甚至数百万人民币的在制品（WIP）。人工搬运极易磕碰产生微振动或错拿混片（Wrong Lot），因此 300mm Fab 全面采用 **AMHS（Automated Material Handling System，代表厂商：大福 Daifuku、村田 Murata）**。

---

## 2. AMHS 核心硬件组成

| 组件 | 英文全称 | 核心作用与工程细节 |
| :--- | :--- | :--- |
| **FOUP** | Front Opening Unified Pod | **前开式晶圆传送盒**（SEMI E47.1）：标准容量 **25 片**，槽距 **`10.0 mm`**；抗静电聚碳酸酯茶色半透明外壳，底部带充氮口（防止铜氧化或晶圆表面长自然氧化膜）与 RFID 标签 |
| **OHT** | Overhead Hoist Transport | **空中悬吊天车**：沿天花板下方（距地面约 3.2~3.8m）铝型材轨道高速运行；采用**非接触式感应供电（HID/CPS）**与红外光通信防撞；停靠机台上方后，释放 4 根凯夫拉同步带垂直降下机械抓手将 FOUP 精准放到 Load Port |
| **Stocker** | Automated Storage & Retrieval System | **自动立体存储库**：内部像多层立体货架，配有高速堆垛机与**充氮存储位（N2 Purge Stocker）**，用于暂存等待派工的 FOUP |
| **OHB / UTS** | Overhead Buffer / Under Track Storage | 悬挂在天车轨道正下方或旁边的单层暂存架，就近缓冲缩短下一次天车取放时间（Delivery Time） |
| **Lifter** | Inter-floor Lifter | 跨楼层垂直提升机，在多层洁净室之间跨楼层运送 FOUP |

---

## 3. OHT 调度与交通管制核心难题
- **单向环形轨道 + Shortcut 捷径道岔**：避免对向死锁（Deadlock）；
- **动态派工（MCS, Material Control System）**：依据机台即将完工前 2~3 分钟的预通知，提前调度最近的空载 OHT 赶往 Stocker 取下一批料，实现 **Just-In-Time (JIT) 无缝换料**，不让昂贵机台空等（Idle）。
