# 迷宫寻路算法展示 | Maze Pathfinding Visualizer

> 在终端里并排对比 DFS 与 BFS 两种寻路算法的搜索过程与结果差异；附赠一个网页版迷宫绘制器，画出迷宫即可复制成程序标准输入。
> Compare DFS and BFS pathfinding side by side in the terminal, with a companion web-based maze editor that turns your drawing into the program's standard input format.

## 功能特性 | Features

- **算法对比（迷宫-对比.py）**：对同一个迷宫分别运行 DFS（深度优先）与 BFS（广度优先），输出两种算法的 Open/Closed 集合规模、总计算步数，并可视化搜索过程（⭕ 待访问岔路）与最终路径（🔴 答案）。
  **Algorithm comparison (迷宫-对比.py)**：runs DFS and BFS on the same maze, reports Open/Closed set sizes and total computation steps, and visualizes the search process (⭕ pending branches) and final path (🔴 answer).
- **迷宫绘制器（迷宫绘制器.html）**：25×25 网格画笔/橡皮编辑，"智能检验"自动标出孤立点（🔶）与断头路（⭕），"一键复制"将迷宫转为 `⬜️/⬛️` 文本，粘贴进终端即可直接使用。
  **Maze editor (迷宫绘制器.html)**：paint/erase on a 25×25 grid, "smart check" highlights isolated cells (🔶) and dead ends (⭕), and "copy" converts the maze to `⬜️/⬛️` text ready to paste into the terminal.
- 两个工具**完全独立运行**：网页工具双击即开，无后端、无任何外部引用；但设计上与命令行程序配套使用。
  The two tools run **fully independently** — the web page opens directly in a browser with no backend; it is designed to pair with the CLI program.

## 快速开始 | Quick Start

```bash
python 迷宫-对比.py
```

然后逐行粘贴迷宫（`⬜️` 通路、`⬛️` 墙），输入 `e` 结束。起点/终点自动取第一行与最后一行的通路格。
Then paste your maze line by line (`⬜️` open, `⬛️` wall) and finish with `e`. The start/end are taken automatically from the open cells in the first and last rows.

推荐流程：打开 `迷宫绘制器.html` 画迷宫 → 一键复制 → 粘贴进终端。
Recommended flow: draw in `迷宫绘制器.html` → copy → paste into the terminal.

## 依赖 | Dependencies

**无。** 纯 Python 标准库（collections）+ 纯前端 HTML，无需 pip 安装任何东西。
**None.** Pure standard library (collections) plus plain HTML — nothing to install.

## 说明 | Notes

- 终端需支持 emoji 显示（Windows Terminal / 现代终端均可）。
  Your terminal needs emoji support (Windows Terminal or any modern terminal works).
- 本项目适合算法入门教学与直观理解"为什么 BFS 保证最短路径而 DFS 不保证"。
  Great for teaching beginners why BFS guarantees the shortest path while DFS does not.
