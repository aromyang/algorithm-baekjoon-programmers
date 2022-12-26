def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    from_dict = dict.fromkeys(id_list)
    to_dict = dict.fromkeys(id_list)

    for r in report:
        f = r.split()[0]
        t = r.split()[1]

        if from_dict[f]:
            from_dict[f].add(t)
        else:
            from_dict[f] = {t}
        if to_dict[t]:
            to_dict[t].add(f)
        else:
            to_dict[t] = {f}

    for i, id in enumerate(id_list):
        if from_dict[id]:
            for j in from_dict[id]:
                if len(to_dict[j]) >= k:
                    answer[i] += 1
    return answer