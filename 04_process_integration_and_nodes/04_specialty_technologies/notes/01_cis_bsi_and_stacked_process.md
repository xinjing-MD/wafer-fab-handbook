# CMOS 图像传感器（CIS）：背照式（BSI）与三维堆叠键合工艺

- **所属模块**：`04_process_integration_and_nodes / 04_specialty_technologies`

---

## 1. CIS 结构演进：FSI → BSI → Stacked 堆叠架构

```text
[前照式 FSI (传统)]               [背照式 BSI (主流)]               [三层堆叠 CIS (高端)]
   入射光线                          入射光线                          入射光线
      ↓                                 ↓                                 ↓
[彩色滤光片 + 微透镜]              [彩色滤光片 + 微透镜]              [彩色滤光片 + 微透镜]
      ↓                                 ↓                                 ↓
[金属布线层 (M1~M4 挡光!)]         [减薄硅衬底光电二极管 (满格进光)]   [像素阵列晶圆 (Pixel Wafer)]
      ↓                                 ↓                          ============ Cu-Cu 混合键合
[底层光电二极管 (光损失大)]         [金属布线层 (移到了背面下层)]      [高速逻辑处理晶圆 (Logic Wafer)]
                                                                   ============ 硅通孔 / 键合
                                                                   [DRAM 缓存晶圆 (超慢动作捕捉)]
```

- **传统 FSI（Front-Side Illumination）痛点**：金属互连线挡在感光硅表面上方，光线经过多次反射与折射，在像素微缩到 1.4μm 以下时感光度（Sensitivity）急剧劣化，且斜射光线极易溢出到隔壁像素造成严重**串扰（Cross-talk / 偏色）**。
- **背照式 BSI（Back-Side Illumination）**：颠覆性地将晶圆背面朝上进光，金属走线全部藏在光电二极管（Photodiode）下方，进光开口率（Fill Factor）达到接近 100%。

---

## 2. 现代 BSI CIS 晶圆厂制造核心技术

1. **晶圆键合与背面极限减薄（Wafer Bonding & Backside Thinning）**：
   - 正面制造完光电二极管与多层金属走线后，将晶圆正面与一块平整支撑硅片（Carrier Wafer）进行永久氧化层键合；
   - 翻转晶圆，使用高精度磨削机（Grinding）与 CMP 将硅片从原本的 **$775\,\mu\text{m}$ 减薄至仅剩 $2\sim 4\,\mu\text{m}$**（比红细胞还薄！）；
   - 减薄后必须用化学腐蚀去除机械损伤层，防止界面缺陷引起暗电流（Dark Current）和白点噪点（White Spot）。
2. **深沟槽隔离（DTI, Deep Trench Isolation）**：
   - 为了防止相邻纳米级像素之间光子与电子横向穿透串扰，在每个感光像素周围用干法刻蚀挖出深达数微米的极细狭缝；
   - 填入高反射率金属氧化物介质，像砌“不透光的反光水泥墙”一样把每个像素完全独立隔开（分为 Front-DTI 与 Full-depth DTI）。
3. **彩色滤光片（CFA）与微透镜（On-chip Microlens）制作**：
   - 在减薄的背面涂布含红、绿、蓝（RGB / Bayer Array）感光颜料的负性光刻胶，三次低温光刻成型滤色阵列；
   - 表面旋涂透明聚合物透镜胶，光刻出正方形微岛，经热回流（Thermal Reflow）在表面张力作用下自发收缩变圆，形成数千万个聚集光线的微米级凸透镜。
4. **Cu-Cu 混合键合（Direct Bond Interconnect, DBI）**：
   - 顶级手机 CIS（如索尼 Exmor RS 系列）将感光像素晶圆与底部逻辑处理晶圆面对面直接键合；
   - 表面通过极限 CMP 抛光至表面粗糙度 $< 0.2\,\text{nm}$，两片晶圆在超净真空室内以亚微米精度对准贴合，在 250~350°C 退火下同时完成 $\text{SiO}_2-\text{SiO}_2$ 分子键合与 $\text{Cu}-\text{Cu}$ 原子互扩散导通，实现每平方毫米数万个互连点。
