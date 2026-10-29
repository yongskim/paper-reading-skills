# Paper Reading Skills

**先粗读了解论文，感兴趣后入库并补充精读笔记。** 跨领域适用，默认中文，支持 Zotero 与思源 PDF 首页画廊。

Cross-domain paper reading for Codex: skim first, then save with detailed notes when requested.

## 日常只用两句话

### 1. 粗读这篇

上传 PDF、给论文链接，或指定 Zotero 中的论文：

```text
用 $paper-reading 粗读这篇论文。
```

得到约 2–3 分钟可读完的概览：一句话总结、叙事脉络、研究问题、核心认识、研究做法与主要结果。结构随论文类型调整，以事实和证据为主。此时只在聊天中呈现，不问归档目录、不创建思源记录。

### 2. 入库并精读

觉得值得保留，就在同一对话里继续说：

```text
这篇入库并精读，放到「我的文献库 / 某领域 / 某主题」。
```

代理沿用刚才的论文和有效提取结果，完成：

- 补读关键内容，写清机制或研究设计、条件、关键证据，并核对实质方法或研究设计的来源。
- 在你指定的目录创建或更新论文子文档，写入完整精读笔记，保留已有批注。
- 添加 PDF 首页画廊卡片，填写关键词、年份、研究类型等字段；代码等字段按领域适用性处理。
- 在分类页添加文字索引，画廊和索引都指向同一篇子文档；Zotero 已有对应条目时关联原文。

没说目录时，只需补充要放的位置。你不用再次指定模板或调用其他子技能，也不用重发仍可访问的原文。连接与目标已明确时直接执行；完成后给笔记入口，并说明实际完成情况。

可以跳过粗读，直接要求「用 $paper-reading 入库并精读这篇，放到……」。需要精读但暂不保存时，说「只精读，不入库」。仅说“感兴趣”不会自动写入。

## 安装一次

需要 Python 3.10 或以上，无第三方 Python 依赖：

```bash
git clone https://github.com/yongskim/paper-reading-skills.git
cd paper-reading-skills
python scripts/install.py --dry-run
python scripts/install.py
```

默认安装到 `$CODEX_HOME/skills`；未设置时使用 `~/.codex/skills`。其他技能目录可用 `--dest <skills-directory>` 指定。安装后开启新会话，或按客户端提供的方式刷新技能。

已有同名技能时，脚本在写入前停止。检查差异并备份自己的改动后，用 `python scripts/install.py --update` 更新；它覆盖同名文件并保留其他文件，不清理旧文件。

没有 Python 时，手动复制下方表中的六个技能文件夹到技能目录，保持为同级文件夹。不要只复制入口 `SKILL.md`。

## 按需连接应用

**只粗读：** 提供可读原文即可，不要求 Zotero 或思源。

**入库并精读：** 提供可用的思源 API 或连接器，并明确目标文献库。需要关联 Zotero 时提供对应连接。新用户可让代理“检查思源和 Zotero 连接，帮我配置本地论文库”，再选择自己的根目录。

个人配置保存在发布源码之外；可从 [空白示例](examples/siyuan.config.example.json) 复制。配置发现顺序与字段见 [运行配置说明](paper-reading/references/runtime-configuration.md)。密钥交给已连接工具或环境变量，不写进 skill 或示例。

PDF 遵从活动工作区的提取规则；不要求固定安装 MinerU，不假设软件路径或硬件。没有所需连接时可继续交付 Markdown，并说明尚未完成的归档步骤。

本仓库提供代理指令、模板和安装工具。应用操作依赖当前环境可用的工具，不会自行安装插件，也没有后台同步服务。输入只有外部 PDF 时，不自动导入 Zotero。现成工具与联动边界见 [Zotero / 思源联动](paper-reading/references/zotero-siyuan.md) 和 [画廊工作流](paper-reading/references/gallery-workflow.md)。

## 内容约定

论文按实际研究类型阅读：方法讲机制，实证讲测量，定性研究讲材料与分析过程，Benchmark 讲数据和评估协议，综述讲范围与分类，理论讲定义与证明。领域和论文类型不会替你决定存放目录。

区分作者主张、证据支持和阅读解释，保留 Section、Figure、Table、Equation 等定位。默认不生成研究方案、审稿式评分或替读者回答思考题。精读来源追查需要对照本文与前作，不能仅凭相似认定继承。

<details>
<summary>精读笔记结构与思源公式</summary>

完整笔记约 5–10 分钟可读完，复杂核心内容可展开：

1. 一句话总结。
2. 叙事脉络，紧接总结。
3. 问题与动机。
4. 核心认识与发现。
5. 问题定义与适用条件。
6. 研究设计与技术内容，包括相关来源。
7. 证据与主要发现。

这些是阅读功能，实际标题按论文类型调整。笔记采用思源兼容 Markdown：行内公式用 `$...$`，独立公式用各自占一行的 `$$`，多行公式使用 `aligned`。见 [笔记模板](paper-reading/assets/siyuan-note-template.md) 与 [思源格式](paper-reading/references/siyuan-format.md)。

</details>

<details>
<summary>内部技能与单独调用</summary>

日常只需使用 `$paper-reading`。以下模块由总入口按需调用，也支持单独处理局部任务：

| 技能 | 用途 |
| --- | --- |
| [paper-reading](paper-reading/SKILL.md) | 粗读 → 用户决定 → 入库并精读 |
| [paper-reading-skim](paper-reading-skim/SKILL.md) | 简短概览 |
| [paper-reading-deep](paper-reading-deep/SKILL.md) | 深入解释研究设计与证据 |
| [paper-reading-lineage](paper-reading-lineage/SKILL.md) | 方法、理论、设计或材料的来源追查 |
| [paper-reading-synthesis](paper-reading-synthesis/SKILL.md) | 整理已有事实、出处和用户批注 |
| [paper-reading-archive](paper-reading-archive/SKILL.md) | 思源画廊、索引与子文档归档 |

例如：“用 $paper-reading 只解释评估协议”或“用 $paper-reading-lineage 追查这个设计的前作”。无需依次运行所有模块。

</details>

## 验证与贡献

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
```

检查覆盖技能基础结构、相对链接、常见隐私泄露特征，以及临时目录中的安装与迁移。GitHub Actions 在 Windows 和 Linux 上运行同样的检查。事实准确性、PDF 提取和应用写入需在使用环境中核验；源码检查不代表端到端论文归档已验证。

请勿提交本机路径、个人配置、真实文档/数据库 ID、令牌、论文全文、私人笔记或生成内容。欢迎提供脱敏后的 Issue 和 PR，参见 [贡献说明](CONTRIBUTING.md)。

## 许可证

[MIT](LICENSE)。适用于本仓库的原创技能指令、模板和代码，不改变外部论文或第三方软件的权利。
