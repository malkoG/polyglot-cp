import java.util.Scanner
import java.util.LinkedList

typealias Board = Array<Array<Int>>
typealias BooleanBoard = Array<Array<Boolean>>
typealias Position = Pair<Int,Int>

val dx = arrayOf(0, 1, 0, -1)
val dy = arrayOf(1, 0, -1, 0)

fun dfs(visited: BooleanBoard, 
		cheeseMap: Board,
		y: Int, x: Int, 
		limitY: Int, limitX: Int) {
	visited[y][x] = true

	for (i in 0..3) {
		val nextY = y + dy[i]
		val nextX = x + dx[i]

		if (nextX >= 0 && nextX <= limitX &&
				nextY >= 0 && nextY <= limitY &&
				!visited[nextY][nextX] && cheeseMap[nextY][nextX] == 0 ) {
			dfs(visited, cheeseMap, nextY, nextX, limitY, limitX)
		}
	}
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var year = 0
	var queue = LinkedList<Position>()
	var visited = Array(102) { Array(102) { false } }
	var cheeseMap = Array(102) { Array(102) { 0 } }

	val N = nextInt()
	val M = nextInt()

	for (i in 1..N) {
		for (j in 1..M) {
			cheeseMap[i][j] = nextInt()
		}
	}

	while(true) {
		for (i in 0..N) {
			for (j in 0..M) {
				visited[i][j] = false
			}
		}

		dfs(visited, cheeseMap, 0, 0, N, M) 

		for(y in 1..N) {
			for (x in 1..M) {
				if (cheeseMap[y][x] == 1) {
					var exposures = 0

					for (i in 0..3) {
						var nextY = y + dy[i]
						var nextX = x + dx[i]
						
						if(cheeseMap[nextY][nextX] == 0 && visited[nextY][nextX])
							exposures += 1
					}

					if (exposures >= 2)
						queue.offer(Position(y, x))
				}
			}
		}

		if(queue.isEmpty())
			break
	
		while(!queue.isEmpty()) {
			val (y, x) = queue.poll()

			cheeseMap[y][x] = 0
		}

		year += 1
	}

	println(year)
}
