import java.util.Scanner
import java.util.ArrayList

fun solve(N: Long, P: Long) : Long {
	if (P == 0L)
		return 1L
	
	if (P % 2 == 0L) {
		val s = solve(N, P/2L) % 1_000_000_007L
		return (s * s) % 1_000_000_007L
	}

	return (N * solve(N, P-1)) % 1_000_000_007L
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var N = nextLong()
	val M = nextLong()

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
			QV.add(Pair(Q, count*M+1))
		}
	}

	if (N > 1L) {
		QV.add(Pair(N, M+1))
	}
	
	var answer = 1L
	for (p in QV) {
		val (NN, P) = p
		val result = solve(NN, P)-1L
		answer *= (result * solve(NN-1L, 1_000_000_005L)) % 1_000_000_007
		answer %= 1_000_000_007L
	}

	println(answer)
}
