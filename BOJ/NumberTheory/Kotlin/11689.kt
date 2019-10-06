import java.util.Scanner
import java.util.ArrayList

fun solve(N: Long, P: Long) : Long {
	if (P == 0L)
		return 1L
	
	if (P % 2 == 0L) {
		val s = solve(N, P/2L)
		return (s * s)
	}

	return (N * solve(N, P-1))
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var N = nextLong()
    
	var target = 0L
	var QV = ArrayList<Pair<Long,Long>>()
	for (Q in 2L..100000L) {
		var count = 0L
		if (Q > N)
			break

		while(N % Q == 0L) {
			N /= Q
			count += 1
		}
		
		if (count > 0) {
			QV.add(Pair(Q, count))
		}
	}

	if (N > 1L) {
		QV.add(Pair(N, 1))
	}
	
	var answer = 1L
	for (p in QV) {
		val (NN, P) = p
		val result = solve(NN, P-1)*(NN-1L)
		answer *= result
	}

	println(answer)
}
