# 09 · 实战代码、仿真脚本与三维可视化资产 (`09_实战脚本与3D`)

> “光背公式不够，亲手跑一遍数据、Wafer Map 图谱与 SECS/E84 状态机才能真正建立产线工程直觉。”

## 目录与内容
- `01_Python良率与SPC仿真/`
  - [yield_and_dpw_calculator.py](./01_Python良率与SPC仿真/yield_and_dpw_calculator.py) —— 300mm 晶圆 Gross Die 几何排布计算 + 四大良率模型对比（Poisson / Murphy / Seeds / 负二项）
  - [spc_cpk_demo.py](./01_Python良率与SPC仿真/spc_cpk_demo.py) —— SPC $C_p / C_{pk}$ 计算 + Western Electric Rule 1~4 判异检查器
  - [wafer_map_pattern_simulator.py](./01_Python良率与SPC仿真/wafer_map_pattern_simulator.py) —— CP Wafer Map 四大典型失效图谱模拟（边缘环 / 中心靶心 / 划痕 / 光罩周期重复点）与根因提示
- `02_SECS_GEM状态机仿真/`
  - [e10_state_machine_sim.py](./02_SECS_GEM状态机仿真/e10_state_machine_sim.py) —— SEMI E10 设备六态机与 SEMI E84 OHT-LoadPort 交接握手模拟
- `03_工艺流程Mermaid图/`
  - [01_CMOS工艺与CIM数据闭环Mermaid图.md](./03_工艺流程Mermaid图/01_CMOS工艺与CIM数据闭环Mermaid图.md) —— 可直接嵌入文档与汇报的晶圆厂 Mermaid 流程图库
- `04_三维建模与视觉参考/`
  - [README.md](./04_三维建模与视觉参考/README.md) —— 现代晶圆厂三维建模与科普可视化全套参考专著（含厂房布局、9 大设备毫米级特征、工艺流转、运动学、Blender 着色规范）
