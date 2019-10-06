import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val N = nextInt()
	var M = nextLong()

	val A = Array(N) { nextLong() }
	val B = Array(N) { nextLong() }

	for (i in 0..N-1) {
		if (M >= A[i] && B[i]-A[i] >= 0)
			M += B[i]-A[i]
	}

	println(M)
}
