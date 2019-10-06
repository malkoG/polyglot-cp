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

		if(subsets[mid] < value) {
			lo = mid + 1
		} else {
			hi = mid
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

		if(subsets[mid] <= value) {
			lo = mid + 1
		} else {
			hi = mid
		}
	}

	return lo
}

fun equal_range(subsets: ArrayList<Int>,
				low: Index, 
				high: Index,
				value: Int) : Pair<Index,Index> {
	return Pair(lower_bound(subsets, low, high, value), upper_bound(subsets, low, high, value))
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
    val T = nextInt()
    for (t in 1..T) {
		val N = nextInt()
		val S = nextInt()

		val h = N shr 1
	
		var leftHalf = ArrayList<Int>()
		var rightHalf = ArrayList<Int>()

		var sequence = Array(N) { nextInt() }
	
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

		var ans = 0L
		for (leftSum in leftHalf) {
			val (lower,upper) = equal_range(rightHalf, 0, 1 shl (N-h), S-leftSum)
    		ans += upper
		}

		if (S == 0) {
			println(ans - 1)
		} else {
			println(ans)
		}
    }
}
