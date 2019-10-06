import java.util.Scanner
import java.util.ArrayList
import java.util.Collections

typealias Index = Int
typealias Data  = Long

fun lower_bound(subsets: ArrayList<Data>,
				low: Index,
				high: Index,
				value: Data) : Index {
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

fun upper_bound(subsets: ArrayList<Data>,
				low: Index,
				high: Index,
				value: Data) : Index {
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

fun equal_range(subsets: ArrayList<Data>,
				low: Index, 
				high: Index,
				value: Data) : Pair<Index,Index> {
	return Pair(lower_bound(subsets, low, high, value), upper_bound(subsets, low, high, value))
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {

	val N = nextInt()
	val M = nextInt()
	
	var arr = ArrayList<Data>()

	for (i in 1..N)
		arr.add(nextInt())

	arr.sort()

	val ans = 10000000007L
	for (num in arr) {
		val lo = lower_bound(arr, 0, N, num + M)
		if (lo != N && ans > (arr[lo] - num))
			ans = arr[lo] - num
	}

	println(ans)
}
