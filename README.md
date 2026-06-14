# task-management-template

这是一个对于一位精通敏捷开发与项目管理的效率专家，旨在为用户设计一套结构严谨、实操性强的 Markdown 任务管理模版。
我们需要一个标准化的任务管理工具，在接到新任务时能够快速梳理全流程并预估工时，确保项目不漏掉调研、实施、评审等关键节点。
这是一个包含“任务基本信息”、“标准工作流（调研/实施/评审/交付）工时预估表”、“风险与依赖”以及“每日进度追踪”的 Markdown
模版，并提供简要的使用指南。

---

## 📋 任务管理 Markdown 模版

你可以直接复制以下 Markdown 代码保存为 `.md` 文件（如 [task-template.md](template-cn/task-template.md)），作为你的任务管理元模版。

---

## 📚 模板文档索引

本项目提供多个针对不同场景优化的任务管理模板，你可以根据实际需求选择合适的模板：

### 📋 可用模板列表

| 模板名称 | 适用场景 | 文件链接 |
|:--------|:--------|:---------|
| **通用任务模板** | 适合多种任务类型（功能开发、Bug修复、技术优化、调研分析、文档编写等），包含优先级管理、目标交付物、变更记录等增强功能 | [universal-task-template.md](template-cn/universal-task-template.md) |
| **Java 开发模板** | 专为 Java 开发任务设计，包含技术架构、Code Review 清单、部署运维、测试清单等 Java 专属内容 | [java-development-template.md](template-cn/java-development-template.md) |
| **调查/文档整理模板** | 适用于市场调研、竞品分析、技术调研、用户研究、文档整理等研究型任务，包含信息来源管理、关键发现记录、结论建议等 | [research-documentation-template.md](template-cn/research-documentation-template.md) |
| **Java 任务示例** | Java 开发任务的实际使用示例（用户认证模块重构），展示如何填写和使用模板 | [java-auth-task-example.md](example/java-auth-task-example.md) |

### 🎯 如何选择模板
[universal-task-template.md](template-cn/universal-task-template.md)
* **日常通用任务** → 使用 [通用任务模板](template-cn/universal-task-template.md)
* **Java 项目开发** → 使用 [Java 开发模板](template-cn/java-development-template.md)
* **调研分析/文档整理** → 使用 [调查/文档整理模板](template-cn/research-documentation-template.md)
* **想看看实际效果** → 参考 [Java 任务示例](example/java-auth-task-example.md)

### 💡 使用建议

1. **复制模板**：选择合适的模板，复制一份作为新任务的看板
2. **重命名文件**：建议命名为 `[任务名称]-task-board.md` 便于识别
3. **填充内容**：根据实际情况填写各个章节，不必拘泥于所有字段
4. **持续更新**：每日更新进度和笔记，保持模板的实时性
5. **任务复盘**：任务完成后回顾工时偏差，持续优化预估能力

---

## 💡 效率专家的小贴士 (Tips)

1. **工时预估的"颗粒度"**：建议单个细分任务的预估工时**不要超过 4 小时 (0.5天)**。如果一个任务需要 8
   小时以上，说明它还可以继续拆解。拆得越细，预估越准。
2. **偏差率计算**：任务结束后，可以通过公式 $\frac{\text{实际} - \text{预估}}{\text{预估}} \times 100\%$
   来计算你的工时偏差。这能帮你复盘自己是"乐观主义者"还是"悲观主义者"，从而让下一次的预估更精准。
3. **不要漏掉交付物**：在"评审与修正"阶段，Code Review 往往最容易被忽略。把它单独列出来，能有效减少"代码写完了，但卡在合并分支"的情况。