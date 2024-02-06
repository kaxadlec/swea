T = int(input())
for tc in range(T):
    str1 = input()
    str2 = input()
    set_str1 = list(set(str1))
    count_dict = {}

    for idx in set_str1:
        count_dict.setdefault(idx, 0)

    item = count_dict.items()
    for k, v in item:
        for s in str2:
            if k == s:
                count_dict[k] += 1

    max_v = 0
    for v in count_dict.values():
        if v > max_v:
            max_v = v

    print(f'#{tc+1} {max_v}')