import collections


class MazeSolver:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        self.end = end
        self.rows = len(maze)
        self.cols = len(maze[0])

    def solve_dfs(self):
        # 栈内存储: (当前坐标, 路径)
        stack = [(self.start, [self.start])]
        visited = set()
        open_list = [self.start]  # 初始点在 Open 中
        closed_list = []
        count = 0

        while stack:
            curr, path = stack.pop()
            # 模拟：从 Open 弹出，进入 Close
            if curr in open_list:
                open_list.remove(curr)

            if curr in visited:
                continue

            count += 1
            visited.add(curr)
            closed_list.append(curr)

            if curr == self.end:
                return path, open_list, closed_list, count

            # 探索邻居 (DFS通常倒序压栈以保持顺序，这里按正常逻辑)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = curr[0] + dr, curr[1] + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and \
                        self.maze[nr][nc] == '⬜️' and (nr, nc) not in visited:
                    stack.append(((nr, nc), path + [(nr, nc)]))
                    if (nr, nc) not in open_list:
                        open_list.append((nr, nc))
        return None, open_list, closed_list, count

    def solve_bfs(self):
        queue = collections.deque([(self.start, [self.start])])
        visited = {self.start}
        open_list = [self.start]
        closed_list = []
        count = 0

        while queue:
            curr, path = queue.popleft()
            # 模拟：从 Open 弹出，进入 Close
            if curr in open_list:
                open_list.remove(curr)

            count += 1
            closed_list.append(curr)

            if curr == self.end:
                return path, open_list, closed_list, count

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = curr[0] + dr, curr[1] + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and \
                        self.maze[nr][nc] == '⬜️' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    open_list.append((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))
        return None, open_list, closed_list, count


def print_maze_state(maze, path, opens, closes, title):
    print(f"\n--- {title} ---")
    path = path or []
    for r in range(len(maze)):
        line = ""
        for c in range(len(maze[0])):
            pos = (r, c)
            if pos in path:
                line += "🔴"
            elif pos in closes:
                line += "✔️"  # 已访问 (Close)
            elif pos in opens:
                line += "⭕️"  # 待访问 (Open)
            else:
                line += maze[r][c]
        print(line)


def main():
    print("请输入迷宫 (⬜️通路, ⬛️墙, 'e'结束):")
    raw_maze = []
    while True:
        line = input().strip()
        if line.lower() == 'e': break
        if line: raw_maze.append([line[i:i + 2] for i in range(0, len(line), 2)])

    start = (0, raw_maze[0].index('⬜️'))
    end = (len(raw_maze) - 1, raw_maze[-1].index('⬜️'))

    solver = MazeSolver(raw_maze, start, end)

    results = {
        "深度优先搜索 (DFS)": solver.solve_dfs(),
        "广度优先搜索 (BFS)": solver.solve_bfs()
    }

    for name, (path, opens, closes, count) in results.items():
        print(f"\n{'=' * 20} {name} {'=' * 20}")
        print(f"1. 最终结算时的 Open 数量: {len(opens)}")
        print(f"   内容: {opens}")
        print(f"2. 最终结算时的 Close 数量 (即计算次数): {len(closes)}")
        print(f"   内容: {closes}")
        print(f"3. 总计算步数: {count}")

        print_maze_state(raw_maze, None, opens, closes, "过程图 (⭕Open表示算法‘看中’但还没走的岔路)")
        print_maze_state(raw_maze, path, [], [], "路径图 (🔴最终答案)")


if __name__ == "__main__":
    main()