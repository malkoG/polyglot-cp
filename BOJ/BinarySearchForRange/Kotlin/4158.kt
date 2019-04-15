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
	while(true) {
		val N = nextInt()
		val M = nextInt()

		if (N == 0 && M == 0)
			break

		var A = ArrayList<Int>()
		var B = ArrayList<Int>()

		for (i in 1..N) 
			A.add(nextInt())
		
		for (i in 1..M) 
			B.add(nextInt())

		var ans = 0
		for (cd in A) {
			val (lower, upper) = equal_range(B, 0, M, cd)
			ans += upper - lower
		}

		println(ans)
	}
}
