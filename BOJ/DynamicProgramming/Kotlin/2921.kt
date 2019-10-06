import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var dp  = Array(1001) { Array(1001) { 0L } }
	var dp2 = Array(1001) { Array(1001) { 0L } }

	dp[0][0] = 1L
	for (i in 0L..1000L)
		dp2[i.toInt()][1] = i

	for (H in 1..1000) {
		var current = 0L
		for (W in 0..1000) {
			current += dp[W][H-1]
			dp[W][H] = current
		}
	}

	for (H in 1..1000) {
		var current = 0L
		for (W in 0..1000) {
			current += dp2[W][H-1] + W*dp[W][H]
			dp2[W][H] = current
		}
	}

	for (H in 1..1000) {
		for (W in 0..1000) {
			print("(")
			print(dp[W][H])
			print(",")
			print(dp2[W][H])
			print(")")
			print(" ")
		}
		println("")
	}
	val N = nextInt()
	print(dp2[N][N])
}
