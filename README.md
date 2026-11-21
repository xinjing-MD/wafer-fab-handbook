# Wafer Fab Handbook · 半导体晶圆厂系统学习与资料归档库

> 从**器件物理**、**洁净室厂务**、**七大核心单项工艺**、**工艺整合**、**制造设备与零部件**、**AMHS/CIM 自动化**到**良率工程与晶圆厂经济账**的 GitHub 开源学习路线与结构化知识库。

---

## 1. 学习全景图（Learning Architecture）

```mermaid
flowchart LR
    S0["00 学习路线与规范"] --> S1["01 基础物理与器件"]
    S1 --> S2["02 厂房结构与厂务"]
    S2 --> S3["03 七大单项工艺"]
    S3 --> S4["04 工艺整合 FEOL/MOL/BEOL"]
    S4 --> S5["05 设备与关键零部件"]
    S5 --> S6["06 AMHS天车与CIM/MES"]
    S6 --> S7["07 良率 SPC 与失效分析"]
    S7 --> S8["08 晶圆厂运营与产业链"]
    S3 -.-> S9["09 Python仿真与流程图"]
    S7 -.-> S9
```

---

## 2. 目录导航与学习进度看板

| 模块 | 主题方向 | 核心内容 | 建议学时 | 当前进度 |
| :--- | :--- | :--- | :---: | :---: |
| [00_roadmap_and_guides](./00_roadmap_and_guides/README.md) | 路线与规范 | 4 阶段规划、分岗位学习路线、笔记与上传规范 | 1h | 🟢 100% 完整 |
| [01_fundamentals_and_devices](./01_fundamentals_and_devices/README.md) | 器件与物理基础 | CZ 单晶、300mm 规范矢量图、能带/载流子、MOS C-V、短沟道 SCE、FinFET/GAA/3D NAND | 1~2 周 | 🟢 100% 完整 |
| [02_fab_architecture_and_facilities](./02_fab_architecture_and_facilities/README.md) | 厂房与厂务系统 | 三层建筑剖面、UPW 超纯水/特气/CDS、HVAC/MAU/PCW、真空干泵/Scrubber、SEMI F47/抗微振 | 1 周 | 🟢 100% 完整 |
| [03_unit_processes](./03_unit_processes/README.md) | **七大单项工艺** | 光刻 / 刻蚀清洗 / 薄膜沉积 / 热处理与注入 / CMP / 金属化 / 量测检测（全套配 7 张精制 SVG 矢量图 + 7 份经典论文精读指南） | 4~6 周 | 🟢 100% 完整 |
| [04_process_integration_and_nodes](./04_process_integration_and_nodes/README.md) | 工艺整合与节点 | CMOS 全流程串联、HKMG/GAA/BSPDN、1T1C DRAM、3D NAND 百层 HARC、CIS 背照堆叠、SiC/GaN 功率工艺、先进封装桥梁 | 2 周 | 🟢 100% 完整 |
| [05_equipment_and_subsystems](./05_equipment_and_subsystems/README.md) | 设备与核心部件 | Cluster Tool/EFEM、RF/ESC/MFC/干泵/分子泵、全球五大巨头与国产替代格局 | 1~2 周 | 🟢 100% 完整 |
| [06_fab_automation_and_cim](./06_fab_automation_and_cim/README.md) | 天车与 CIM/MES | OHT/FOUP/Stocker、SECS/GEM/E84/E87/E90、MES/EAP/RTD/APC 软件栈 | 1~2 周 | 🟢 100% 完整 |
| [07_yield_spc_and_failure_analysis](./07_yield_spc_and_failure_analysis/README.md) | 良率、SPC 与 FA | 良率四大模型($D_0$)、$C_p/C_{pk}$、西方电气判异规则、WAT/CP/Wafer Map 图谱、EFA/PFA 流程 | 2 周 | 🟢 100% 完整 |
| [08_fab_operations_and_industry](./08_fab_operations_and_industry/README.md) | 运营与产业链 | 晶圆单片成本模型、IE 运营指标、七大耗材供应链矩阵、全球代工厂与存储三巨头产能周期 | 1 周 | 🟢 100% 完整 |
| [09_labs_code_and_visuals](./09_labs_code_and_visuals/README.md) | 实战代码与图表 | Python 良率/SPC 脚本、E10/E84 状态机仿真、Mermaid 流程图、现代晶圆厂三维建模全套规范 | 穿插全程 | 🟢 100% 完整 |
| [10_glossary_books_and_interviews](./10_glossary_books_and_interviews/README.md) | 工具箱与资源 | 60+ 晶圆厂中英术语词典、经典教材与公开课书单、分岗位笔面试高频题库 | 随时查阅 | 🟢 100% 完整 |
| [99_inbox_staging](./99_inbox_staging/README.md) | 临时收件箱 | 暂存收件箱与标准化草稿模板，每周日集中归档 | 每周清理 | 🟢 规范就绪 |

---

## 3. 快速上手指南

1. **先读路线**：查看 [4 阶段学习路线](./00_roadmap_and_guides/learning_roadmap_4_stages.md) 和 [分岗位路径](./00_roadmap_and_guides/role_based_tracks.md)，确定自己的重点模块。
2. **遵守上传规则**：阅读 [仓库规范](./00_roadmap_and_guides/repo_conventions.md)——**笔记/代码/轻量图进 Git；教材 PDF、视频、3D 工程文件只写进 `external_links.md`**，不直接 push 大文件。
3. **跑通实战脚本**：进入 `09_labs_code_and_visuals/` 运行 Python 示例：
   ```bash
   python 09_labs_code_and_visuals/01_python_yield_and_spc/yield_and_dpw_calculator.py
   python 09_labs_code_and_visuals/01_python_yield_and_spc/spc_cpk_demo.py
   python 09_labs_code_and_visuals/02_secs_gem_simulators/e10_state_machine_sim.py
   ```
4. **每周打卡**：在 GitHub Issues 使用 `.github/ISSUE_TEMPLATE/` 里的打卡模板或精读模板记录进度。

---

## 4. 推送到自己的 GitHub 仓库

```bash
cd wafer-fab-handbook
git init
git add .
git commit -m "chore: initialize wafer fab learning repository"
git branch -M main
git remote add origin https://github.com/<your-username>/wafer-fab-handbook.git
git push -u origin main
```
