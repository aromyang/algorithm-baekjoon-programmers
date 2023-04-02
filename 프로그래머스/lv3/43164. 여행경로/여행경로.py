def solution(tickets):
    tickets.sort(key=lambda x: (0 if x[0] == 'ICN' else 1, x[0], x[1]))
    visited = [False] * len(tickets)
    stack = []

    def dfs(cur_v, ans):
        visited[cur_v] = True
        ans.append((tickets[cur_v][0], cur_v))
        stack.pop()

        if all(visited):
            ans.append((tickets[cur_v][1], cur_v))

        for v, ticket in enumerate(tickets):
            if ticket[0] == tickets[cur_v][1] and not visited[v]:
                stack.append(v)
                dfs(v, ans)

        if not all(visited) and not stack:
            while not all(visited):
                start, idx = ans.pop()
                visited[idx] = False
                for prev_v, prev_ticket in enumerate(tickets):
                    if prev_ticket[0] == start and not visited[prev_v] and idx != prev_v:
                        stack.append(prev_v)
                        visited[idx] = False
                        dfs(prev_v, ans)

    stack.append(0)
    ans = []
    dfs(0, ans)
    return [ans[0] for ans in ans]