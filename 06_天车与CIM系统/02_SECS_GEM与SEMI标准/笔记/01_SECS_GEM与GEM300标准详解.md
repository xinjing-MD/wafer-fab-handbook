# SEMI 工业通信标准：SECS/GEM 与 GEM300 核心协议栈

- **所属模块**：`06_天车与CIM系统 / 02_SECS_GEM与SEMI标准`

## 1. 为什么所有设备商必须遵循 SEMI 标准？
一座晶圆厂里同时运行着 ASML、AMAT、Lam、TEL、KLA 等几十家厂商的上千台设备。如果没有统一的语言规范，工厂里的 **EAP / MES 系统** 根本无法统一派发配方（Recipe）、采集传感器数据或控制天车上下料。

---

## 2. 协议栈分层（从物理层到 300mm 业务标准）

| 标准编号 | 名称 | 一句话理解它管什么 |
| :--- | :--- | :--- |
| **SEMI E4 / E37** | SECS-I (串口) / **HSMS (TCP/IP 以太网)** | **底层传输层**：规定 Host（主机 EAP）和 Equipment（机台）如何建立网络连接、发送字节流数据包 |
| **SEMI E5** | **SECS-II**（Message 格式） | **报文语法层**：规定一条指令怎么编码。核心格式为 **`SxFy`**（Stream 流号 + Function 功能号，奇数请求，偶数应答，如 `S1F1` Are You There? → `S1F2` On Line Data；`S6F11` 事件上报） |
| **SEMI E30** | **GEM** (Generic Equipment Model) | **通用设备行为模型**：规定机台联网状态（Offline/Local/Remote）、工艺状态、报警处理（ALID）、数据采集（VID/CEID/RPTID）、远程指令（PP-SELECT 选配方、START 启动） |
| **SEMI E84** | Enhanced Carrier Handoff Parallel I/O | **天车与 Load Port 硬件交接握手**：通过 8 路光耦传感器信号（`VALID`, `CS_0`, `TR_REQ`, `L_REQ`, `U_REQ`, `READY`, `BUSY`, `COMPT`）完成毫秒级防碰撞交接（可在 `09_实战脚本与3D` 运行 Python 状态机体验！） |
| **SEMI E87** | Carrier Management | **载具（FOUP）管理**：跟踪载具到达、Read ID、Slot Map（扫描 25 层哪几槽有晶圆、是否插斜片 Cross-slot）、Access Mode |
| **SEMI E90** | Substrate Tracking | **单片晶圆跟踪**：精细到每 1 片硅片正在 EFEM 机械手、Pre-aligner 还是 PM2 腔室里 |
| **SEMI E40 / E94** | Process Job / Control Job | **作业编排**：允许将多片甚至不同配方的晶圆打包成一个作业序列，支持机台连续自动加工 |
| **SEMI E10** | Equipment Reliability, Availability, Maintainability | **机台六大标准时间状态**：Productive (生产)、Standby (待机)、Engineering (工程试验)、Scheduled Downtime (计划保养)、Unscheduled Downtime (故障宕机)、Non-Scheduled (未排产) |
