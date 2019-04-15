import java.util.Scanner

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	
	var dp = Array(101010) { Array(10) { 0 } }
	for (i in 0..9) {
		dp[1][i] = 1
	}	

	for (i in 2..100000) {
		for (j in 0..9) {
			for (k in j..9) {
				dp[i][j] = (dp[i][j] + dp[i-1][k]) % 1_000_000_007
			}
		}
	}

	val T = nextInt()
	for (t in 1..T) {
		var answer = 0
		val N = nextInt()
		for (i in 0..9)
			answer = (answer + dp[N][i]) % 1_000_000_007

		println(answer)
	}
}
