import java.util.Scanner
import java.util.ArrayList
import java.util.Collections

typealias Index = Int

fun lower_bound(subsets: ArrayList<Int>,
				low: Index,
				high: Index,
				value: Int) : Index {
	var lo = low
	var hi = high
	var mid: Index = high
	while(lo < hi) {
		mid = (lo + hi) shr 1
		if (mid == high)
			return high

		if(subsets[mid] < value) { // value보다 작은 값을 만난 경우
			lo = mid + 1           // 탐색 범위가 뒤쪽에 있다고 가정
		} else {                   // value보다 크거나 같은 값을 만난 경우
			hi = mid               // 탐색 범위 안쪽에 있다고 가정
		}
	}

	return lo
}

fun upper_bound(subsets: ArrayList<Int>,
				low: Index,
				high: Index,
				value: Int) : Index {
	var lo = low
	var hi = high
	var mid: Index = high
	while (lo < hi) {
		mid = (lo + hi) shr 1
		if (mid == high)
			return high

		if(subsets[mid] <= value) {  // value보다 작거나 같은 값을 만난 경우
			lo = mid + 1             // 탐색 범위가 뒤쪽에 있다고 가정
		} else {                     // value보다 큰 값을 만난 경우
			hi = mid                 // 탐색 범위 안쪽에 있다고 가정
		}
	}

	return lo                        // 맨 왼쪽 범위가 처음 나타나는 위치를 의미
}

fun equal_range(subsets: ArrayList<Int>,
				low: Index, 
				high: Index,
				value: Int) : Pair<Index,Index> {
	return Pair(lower_bound(subsets, low, high, value), upper_bound(subsets, low, high, value))
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {

	val N = nextInt()
	val arr = Array(N) { nextInt() }
	
	var sums = ArrayList<Int>()

	for (x in 0..N-1) {
		for (y in 0..N-1) {
			sums.add(arr[x]+arr[y])
		}
	}

	sums.sort()

	var ans = 0
	for (k in 0..N-1) {
		for (z in 0..N-1) {
			val (lower, upper) = equal_range(sums, 0, sums.size, arr[k]-arr[z])
			if (lower != upper) {
				if(ans < arr[k])
					ans = arr[k]
			}
		}
	}

	println(ans)
}
