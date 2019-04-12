import java.util.Scanner
import java.util.ArrayList
import java.util.Collections

typealias Index = Int

/*
 * value 이상인 값들이 나타나는 처음 위치를 반환
 * 
 */
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

/*
 * value를 넘는 값들이 나타나는 처음 위치를 반환
 * 
 */
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
	val S = nextInt()

	val h = N shr 1
	
	var leftHalf = ArrayList<Int>()
	var rightHalf = ArrayList<Int>()

	var sequence = Array(N) { 0 }
	for (i in 0..N-1)
		sequence[i] = nextInt()
	
	for (i in 0L..((1 shl (N-h))- 1)) {
		var subset = i
		var result = 0
		for (j in 0..N-h-1) {
			if((subset % 2L) == 1L)
				result += sequence[h + j]
			subset = subset shr 1
		}

		rightHalf.add(result)
	}

	for (i in 0..((1 shl h) - 1)) {
		var subset = i
		var result = 0
		for (j in 0..h-1) {
			if((subset % 2L) == 1L)
				result += sequence[j]
			subset = subset shr 1
		}

		leftHalf.add(result)
	}

	Collections.sort(rightHalf)
/*
	println("left Sum")
	for (leftSum in leftHalf) {
		print(leftSum)
		print(" ")
	}
	
	println("")
	println("right Sum")
	for (rightSum in rightHalf) {
		print(rightSum)
		print(" ")
	}

	println(" ")
*/
	var ans = 0L
	for (leftSum in leftHalf) {
		val (lower,upper) = equal_range(rightHalf, 0, 1 shl (N-h), S-leftSum)
/*		print(lower)
		print(" ")
		print(upper)
		println("")
*/		ans += upper-lower	
	}

	if (S == 0) {
		println(ans - 1)
	} else {
		println(ans)
	}
}
