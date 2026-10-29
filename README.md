# Paper Reading Skills

跨领域论文阅读技能：讲清叙事、研究问题、核心认识、研究设计、来源与证据，保留读者自己的研究思考。可仅生成 Markdown，也可选用 Zotero 与思源集成。

Cross-domain paper-reading skills for Codex, with evidence-grounded Chinese notes, research lineage checks, and optional Zotero / SiYuan archiving.

## 技能

| 技能 | 用途 |
| --- | --- |
| [paper-reading](paper-reading/SKILL.md) | 总入口，选择阅读深度、研究类型和交付方式 |
| [paper-reading-skim](paper-reading-skim/SKILL.md) | 速读与简短事实笔记 |
| [paper-reading-deep](paper-reading-deep/SKILL.md) | 按实际研究类型精读 |
| [paper-reading-lineage](paper-reading-lineage/SKILL.md) | 方法、理论、设计或材料的来源追查 |
| [paper-reading-synthesis](paper-reading-synthesis/SKILL.md) | 整理已有事实、出处和个人批注 |
| [paper-reading-archive](paper-reading-archive/SKILL.md) | 在用户指定目录关联思源画廊、索引与子文档 |

## 安装

下载仓库 ZIP 并解压，或克隆本仓库。在仓库根目录运行以下命令，需要 Python 3.10 或以上，无第三方依赖：

```bash
git clone https://github.com/yongskim/paper-reading-skills.git
cd paper-reading-skills
python scripts/install.py --dry-run
python scripts/install.py
```

默认安装到 `$CODEX_HOME/skills`；未设置 `CODEX_HOME` 时使用 `~/.codex/skills`。也可指定当前环境的技能目录：

```bash
python scripts/install.py --dest <skills-directory>
```

已有同名技能时，脚本会在写入前停止。检查差异并备份自己的改动后，可用 `--update` 更新六个技能；更新采用合并复制，会覆盖同名文件并保留其他文件，不会清理旧文件。

没有 Python 时，手动复制表中的六个技能文件夹到当前环境支持的技能目录，保持为同级文件夹。不要只复制入口 `SKILL.md`。其他目录及根目录文档是发布资料，不必安装。安装后开启新会话，或按客户端提供的方式刷新技能。

## 使用示例

> 用 $paper-reading 阅读这篇论文，只输出 Markdown，不入库。

> 用 $paper-reading-deep 精读这篇定性研究，解释材料选择、分析过程与证据。

> 用 $paper-reading-lineage 对照核心设计与前作，说明沿用和改动。

> 用 $paper-reading-archive 放入我指定的目录；没指定时先问我。

领域、研究类型和归档目录分别处理；新领域不必复制旧分类树。默认保留一句话总结与叙事脉络，其余研究内容按实际类型展开。

阅读深度和内容模块可以组合：L1 速读建立轮廓，L2 精读讲清机制或研究设计，L3 整理已有事实。也可单独要求“只讲叙事”“只核对实验结果”或“追查这个设计的前作”，无需逐层执行。

## 笔记包含什么

默认中文，保留关键英文术语，并尽可能标注 Section、Figure、Table、Equation 或页码。

1. **一句话总结**：研究问题、核心思想与主要结果。
2. **叙事脉络**：论文先提出什么、怎样验证、随后如何推进论证。
3. **问题与动机**：研究问题、已有处理方式与研究缺口。
4. **核心认识与发现**：区分观察、Insight、假设和具体方案。
5. **问题定义与适用条件**：输入输出、关键约束、研究范围及假设。
6. **研究设计与技术内容**：按类型解释机制、测量、协议、材料或证明。
7. **证据与主要发现**：保留关键数字、条件与来源，区分主张和已支持的结论。

这七项是阅读功能，实际标题随论文变化。方法论文讲机制与目标函数；实证研究讲变量、采样与测量；定性研究讲材料和分析过程；Benchmark 讲数据构建和评估协议；综述讲范围与分类；理论研究讲定义、命题和证明。不强行要求算法或消融。

来源追查对照本文与前作的原文，说明沿用、组合和修改，区分作者明确说明的继承与待核实的关系。默认不追加审稿式评分、研究方案或完整思考题答案。

笔记使用思源兼容 Markdown：行内公式用 `$...$`，独立公式用各自占一行的 `$$`，多行公式使用 `aligned`。见 [笔记模板](paper-reading/assets/siyuan-note-template.md) 与 [思源格式](paper-reading/references/siyuan-format.md)。

## 可选集成与本地配置

基础阅读只要求可用原文和相应提取工具，不要求 Zotero、思源或 MinerU。PDF 遵从当前工作区规则，配置了 wrapper 才调用该 wrapper；软件位置、后端与硬件由运行环境决定，不自动安装。

Zotero 和思源仅在请求集成时使用。缺少连接时仍可生成 Markdown，不能声称已完成入库或同步。具体工具及应用版本需要实际核对。

配置可以省略。需要时将 [空白示例](examples/siyuan.config.example.json) 复制到发布源码之外的本地文件，填入自己的连接和真实 ID。配置发现顺序与字段见 [运行配置说明](paper-reading/references/runtime-configuration.md)。密钥使用已连接工具或环境变量，不写进 skill 或示例。

思源归档由用户指定领域和父目录，目录未知时先问。每个选定分类页可使用 PDF 首页作为卡片封面，并关联同一篇子文档和文字索引。常用字段包括标题、年份、研究类型、关键词、阅读状态、论文链接、Zotero 链接、代码状态及代码地址；字段可按领域扩展。标题、数据库和关联 ID 从实际实例读取，不写死在技能里。

这些步骤由代理调用当前可用的 API、连接器或工具完成。仓库没有内置同步守护进程、PDF 提取器或思源插件，也不会自行安装它们。集成规则与可复用工具见 [Zotero / 思源联动](paper-reading/references/zotero-siyuan.md) 和 [画廊工作流](paper-reading/references/gallery-workflow.md)。

## 发布边界

这里只包含通用技能、模板、说明和空白示例。个人配置、文档/数据库 ID、路径、论文、笔记、缩略图与日志保留在仓库之外；.gitignore 是补充保护，发布前仍需检查文件。

这是代理指令集合，不是独立同步服务。源码检查不代表已在所有系统和应用版本完成端到端验证。

## 验证与贡献

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

检查覆盖技能基础结构、相对链接、常见隐私泄露特征，以及临时目录中的安装与迁移。GitHub Actions 在 Windows 和 Linux 上运行同样的检查。真实论文的事实准确性、PDF 提取质量、应用兼容性和画廊写入需在使用环境中核验。

欢迎通过 Issue 或 PR 提供脱敏后的复现信息。参见 [贡献说明](CONTRIBUTING.md)。

## 许可证

[MIT](LICENSE)。该许可证适用于本仓库的原创技能指令、模板和代码，不改变论文原文、第三方软件或其他外部材料的权利。
