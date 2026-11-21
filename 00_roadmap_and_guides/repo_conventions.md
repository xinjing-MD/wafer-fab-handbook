# 仓库整理、命名与资料上传规范

## 1. 资料分级上传规则（防止 GitHub 仓库臃肿）

| 级别 | 文件类型 | 存放规则 | 体积控制 |
| :--- | :--- | :--- | :--- |
| **L1 纯文本与代码** | `.md` 笔记、`.py`、`.ipynb`、`.svg`、`.drawio` | 直接 `git push` 到对应模块目录 | 无严格限制（Notebook 提交前清理大输出） |
| **L2 轻量配图与精华论文** | `.png` / `.webp` 架构图、单篇关键 `.pdf` | 放对应模块 `diagrams/` 或 `papers_and_slides/` | 单图 `< 2MB`，单 PDF `< 10MB`，全库建议 `< 500MB` |
| **L3 超大教材与视频/模型** | 整本教材 PDF、培训视频 `.mp4`、3D 工程 `.blend/.step` | **禁止直接提交 Git**；上传网盘或 GitHub Releases，在 `external_links.md` 建索引 | 仓库内只留标题、摘要、页数/时长和链接 |

---

## 2. 标准子模块 5 件套结构

建议 `03_unit_processes/` 等重点模块统一保持如下目录组织：
```text
xx_module_name/
├── README.md                  # 本模块导读、核心概念 Checklist
├── notes/                     # 个人 Markdown 笔记（编号排序：01_xxx.md）
├── diagrams/                  # 自制或精简后的示意图
├── papers_and_slides/         # 轻量公开讲义或单篇论文
└── external_links.md          # 视频、教材、设备官网白皮书外链索引
```

---

## 3. 文件与 Commit 命名规范

- **目录/文件名**：全小写英文 + 下划线 `_`，顺序类文件加两位数字前缀（如 `01_lithography_fundamentals_and_rayleigh.md`）。
- **Commit Message**（Conventional Commits 风格）：
  - `docs(etch): add ICP vs CCP mechanism notes`
  - `feat(labs): add SPC Western Electric rule checker`
  - `index(fab): add ASML EUV technical links`
  - `chore(inbox): archive weekly unsorted articles`

---

## 4. 单篇笔记参考模板

```markdown
# [主题名称]

- **所属模块**：`03_unit_processes / 01_lithography`
- **掌握程度**：🟡 概念理解 / 🟢 原理可复述 / ⭐ 案例复盘

## 1. 一句话核心原理
> ...

## 2. 机理与流程结构
（插入 Mermaid 或 `./diagrams/xxx.png`）

## 3. 核心指标（KPI）与典型参数
| 指标 | 工程含义 | 关键影响因素 |
| :--- | :--- | :--- |

## 4. 常见缺陷与工程难点（Troubleshooting）
- 现象：
- 根因与改善方向：
```
