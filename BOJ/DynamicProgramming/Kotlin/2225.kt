import java.util.*;

var dp = Array(202) {
	Array(202) { 0 }
}

fun solve(N: Int, K: Int) : Int {
	if (dp[N][K] > 0 || K == 0)
		return dp[N][K];

	if (dp[N][K] == 0) {
		for (i in N downTo 0) {
			dp[N][K] += solve(N-i, K-1)
			dp[N][K] %= 1_000_000_000
		}
	}
	return dp[N][K];
}


fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	for (i in 0..201) {
		dp[0][i] = 1
	}

	val N = nextInt();
	val K = nextInt();

	println(solve(N,K));
}
