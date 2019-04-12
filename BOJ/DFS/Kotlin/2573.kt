import java.util.Scanner

typealias Board = Array<Array<Int>>
typealias BooleanBoard = Array<Array<Boolean>>
typealias Position = Pair<Int,Int>

val dx = arrayOf(0, 1, 0, -1)
val dy = arrayOf(1, 0, -1, 0)

fun dfs(visited: BooleanBoard, 
		iceberg: Board,
		y: Int, x: Int, 
		limitY: Int, limitX: Int) {
	visited[y][x] = true

	for (i in 0..3) {
		val nextY = y + dy[i]
		val nextX = x + dx[i]

		if (nextX >= 0 && nextX <= limitX &&
				nextY >= 0 && nextY <= limitY &&
				!visited[nextY][nextX] && iceberg[nextY][nextX] != 0) {
			dfs(visited, iceberg, nextY, nextX, limitY, limitX)
		}
	}
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var year = 0
	var waterVisited = Array(302) { Array(302) { false } }
	var icebergVisited = Array(302) { Array(302) { false } }
	var iceberg = Array(302) { Array(302) { 0 } }

	val N = nextInt()
	val M = nextInt()

	for (i in 1..N) {
		for (j in 1..M) {
			iceberg[i][j] = nextInt()
		}
	}

	var flag = false
	while(true) {
		var components = 0

		for (i in 0..N) {
			for (j in 0..M) {
				waterVisited[i][j] = false
				icebergVisited[i][j] = false
			}
		}

		for (i in 1..N) {
			for (j in 1..M) {
				if(iceberg[i][j] != 0 && !icebergVisited[i][j]) {
					dfs(icebergVisited, iceberg, i, j, N, M)
					components += 1
				}
			}
		}

		if(components > 1)
			flag = true

		if(components != 1)
			break

		for (i in 0..N) {
			for (j in 0..M) {
				if(iceberg[i][j] == 0)
					waterVisited[i][j] = true
			}
		}

		for(y in 1..N) {
			for (x in 1..M) {
				if (iceberg[y][x] != 0) {
					var exposures = 0

					for (i in 0..3) {
						var nextY = y + dy[i]
						var nextX = x + dx[i]
						
						if(iceberg[nextY][nextX] == 0 && waterVisited[nextY][nextX])
							exposures += 1
					}

					iceberg[y][x] = if (iceberg[y][x] - exposures > 0) iceberg[y][x] - exposures else 0
				}
			}
		}
		
		year += 1
	}

	println(if (flag) year else 0)
}
