import java.util.Scanner

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var dp = Array(1002) {
		Array(1003) {
			0
		}
	}

	var dp2 = Array(1002) {
		Array(1003) {
			0
		}
	}

	var silvers = Array(1002) {
		Array(1003) {
			0
		}
	}

	val max = { x: Int, y: Int -> if(x > y) x else y }
	val R = nextInt()
	val C = nextInt()

	for (i in 1..R) {
		for (j in 1..C) {
			silvers[i][j] = nextInt()
		}
	}

	for (x in 1..C+1) {
		for (y in 1..R) {
			dp[y][x] = max(dp[y][x], dp[y+1][x-1] + silvers[y][x])
			dp[y][x] = max(dp[y][x], dp[y-1][x-1] + silvers[y][x])
			if (x > 1)
				dp[y][x] = max(dp[y][x], dp[y][x-2] + silvers[y][x-1] + silvers[y][x])
		}
	}

	for (x in 1..C+1) {
		for (y in 1..R) {
			dp2[y][x] = max(dp2[y][x], dp2[y+1][x-1] + silvers[y][x])
			dp2[y][x] = max(dp2[y][x], dp2[y-1][x-1] + silvers[y][x])
			dp2[y][x] = max(dp2[y][x], dp2[y][x-1] + silvers[y][x])
		}
	}

	var ans = 0
	for (y in 1..R) {
		ans = max(ans, dp[y][C+1])
		ans = max(ans, dp2[y][C+1])
	}

	println(ans)
}
