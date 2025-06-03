def best_career(input_file_name, output_file_name):
    with open(input_file_name) as file:
        L = int(file.readline())
        E = [list(map(int, file.readline().split())) for _ in range(L)]

    def dfs(i, j):
        if i == 0:
            return E[i][j], [(i, j)]

        paths = []
        if j > 0:
            left_sum, left_path = dfs(i - 1, j - 1)
            paths.append((left_sum, left_path))
        if j < len(E[i - 1]):
            right_sum, right_path = dfs(i - 1, j)
            paths.append((right_sum, right_path))

        if not paths:
            return E[i][j], [(i, j)]

        best_sum, best_path = max(paths, key=lambda x: x[0])
        return best_sum + E[i][j], [(i, j)] + best_path

    candidates = [dfs(L - 1, j) for j in range(len(E[L - 1]))]
    max_sum, best_path = max(candidates, key=lambda x: x[0])
    values = [E[i][j] for i, j in best_path]

    with open(output_file_name, 'w') as file:
        file.write(str(max_sum) + '\n')
        file.write(' '.join(map(str, values)) + '\n')


best_career("lab6/career.in", "lab6/career.out")
