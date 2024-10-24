def longestIncreasingSubarray(l: list[int]) -> list[int]:
    local_dict = dict()
    max_len = 1

    for i in range(len(l) - 1):
        if l[i + 1] > l[i]:
            max_len += 1
            local_dict[i + 1] = max_len
        else:
            max_len = 1

    sorted_dict = sorted(local_dict.items(),
                         key=lambda item: item[1], reverse=True)

    first_val = sorted_dict[0][0] - (sorted_dict[0][1] - 1)
    last_val = first_val + sorted_dict[0][1]

    return l[first_val:last_val]


def main() -> None:

    print(longestIncreasingSubarray([1, 2, 1, 2, 3, 1, 2, 3, 4]))
    # OUTPUT:
    # [1, 2, 3, 4]

if __name__ == '__main__':
    main()

# longestIncreasingSubarray([1, 2, 1, 2, 3, 1, 2, 3, 4]) => [1, 2, 3, 4]
