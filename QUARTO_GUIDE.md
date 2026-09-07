# Quarto 网站维护指南

本仓库同时保留 GitHub 可直接阅读的 Markdown 源文件，并使用 Quarto Book 生成学习网站。

## 本地预览

安装 Quarto 后，在仓库根目录运行：

```bash
quarto preview
```

完整构建：

```bash
python tools/validate_repo.py
python tools/review_repo.py
python tools/validate_quarto_structure.py
quarto render
python tools/validate_rendered_site.py
```

生成的网站位于 `_book/`。该目录是构建产物，不提交到主分支。

## 内容维护约定

- 每个可发布页面只能有一个一级标题 `#`。
- 各章继续保留 `01_中文笔记.md` 与 `02_习题与答案_中英双语.md`。
- 图片继续放在各章的 `images/` 中，引用相对路径。
- 公式继续使用 `$...$` 与 `$$...$$`。
- 新增页面后，同时加入 `_quarto.yml` 的 `project.render` 和 `book.chapters`。
- 教材裁图不得加入公开构建；公开版使用原创重绘图。

## GitHub Pages

推送到 `main` 后，工作流会依次执行内容校验、Quarto 构建、输出链接检查，并把 `_book/` 作为 GitHub Pages artifact 发布。

首次启用时，在 GitHub 仓库的 **Settings → Pages → Build and deployment** 中把 Source 设为 **GitHub Actions**。随后推送 `main`，或在 Actions 页面手动运行 `Publish Quarto Book`。

如果仓库名是 `<username>.github.io`，站点地址为 `https://<username>.github.io/`；普通项目仓库的地址为 `https://<username>.github.io/<repository>/`。
