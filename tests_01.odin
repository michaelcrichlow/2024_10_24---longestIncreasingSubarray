package test

import "core:fmt"
print :: fmt.println

main :: proc() {

	print(longestIncreasingSubarray([]int{1, 2, 1, 2, 3, 1, 2, 3, 4}))
	// OUTPUT:
	// [1, 2, 3, 4]
}


longestIncreasingSubarray :: proc(l: []int) -> []int {
	local_dict := make(map[int]int)
	defer delete(local_dict)

	max_len := 1

	for i in 0 ..< (len(l) - 1) {
		if l[i + 1] > l[i] {
			max_len += 1
			local_dict[i + 1] = max_len
		} else {
			max_len = 1
		}
	}

	key := dict_find_highest_value_and_return_key(local_dict)
	value := local_dict[key]

	first_val := key - (value - 1)
	last_val := first_val + value

	return l[first_val:last_val]
}
