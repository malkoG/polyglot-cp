import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val N = nextInt()
	val M = nextInt()

	var dp  = Array(M+1) { Array(N+1) { 10_000_000 } }
	var wok = ArrayList<Int>()

	for (i in 0..M) 
		dp[i][0] = 0 
	
	wok.add(0)
	for (i in 1..M) 
		wok.add(nextInt())
	
	wok.sort()

	for (i in 1..M) {
		for (j in 0..N) {
			if (j < wok[i])
				dp[i][j] = dp[i-1][j]
			else {
				val calculated = dp[i][j - wok[i]] + 1
				dp[i][j] = if (calculated < dp[i-1][j]) calculated else dp[i-1][j]
			}
		}
	}

	println(dp[M][N])
}
