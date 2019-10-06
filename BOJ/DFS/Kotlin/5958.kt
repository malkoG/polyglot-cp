import java.util.Scanner

val dy = arrayOf(1, 0, -1, 0)
val dx = arrayOf(0, 1, 0, -1)

fun dfs(map: ArrayList<String>,
		visited: Array<Array<Boolean>>,
		currentY: Int,
		currentX: Int,
		limitY: Int,
		limitX: Int) {

	visited[currentY][currentX] = true
	
	for (i in 0..3) {
		val nextY = currentY + dy[i]
		val nextX = currentX + dx[i]

		if(nextY >= 0 && nextY < limitY && 
				nextX >= 0 && nextX < limitX && 
				map[nextY][nextX] != '.' && !visited[nextY][nextX])
			dfs(map, visited, nextY, nextX, limitY, limitX)
	}
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val N = nextInt()
	val C = N
	val R = N
	val _rest = nextLine()

	var map = ArrayList<String>()
	var visited = Array(1002) { Array(1002) { false } }

	for (i in 1..R)
		map.add(nextLine())
	
	var area = 0
	for (y in 0..R-1) {
		for (x in 0..C-1) {
			if(!visited[y][x] && map[y][x] != '.') {
				dfs(map, visited, y, x, R, C)
				area += 1
			}
		}
	}

	println(area)
}
