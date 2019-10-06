import java.util.Scanner

val dy = arrayOf(1, 0, -1, 0)
val dx = arrayOf(0, 1, 0, -1)

fun dfs(map: ArrayList<String>,
		visited: Array<Array<Boolean>>,
		golds: ArrayList<Int>,
		currentY: Int,
		currentX: Int,
		limitY: Int,
		limitX: Int) {

	visited[currentY][currentX] = true
	if (map[currentY][currentX] == 'G')
		golds.add(1)

	for (i in 0..3) {
		val nextY = currentY + dy[i]
		val nextX = currentX + dx[i]

		if(nextY >= 0 && nextY < limitY && 
				nextX >= 0 && nextX < limitX && 
				map[nextY][nextX] != '#' && map[nextY][nextX] != 'T' &&
				!visited[nextY][nextX])
			dfs(map, visited, golds, nextY, nextX, limitY, limitX)
	}
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {

	val C = nextInt()
	val R = nextInt()
	val _rest = nextLine()

	var map = ArrayList<String>()
	var visited = Array(102) { Array(102) { false } }
	var golds = ArrayList<Int>()

	for (j in 1..R)
		map.add(nextLine())

	for (y in 0..R-1) {
		for (x in 0..C-1) {
			if(!visited[y][x] && map[y][x] == 'P') {
				dfs(map, visited, golds, y, x, R, C)
			}
		}
	}
	println(golds.size)
}
