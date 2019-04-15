import java.util.Scanner
import java.util.ArrayList

val dy = arrayOf(-1, -1, -1, 0, 1, 1, 1, 0)
val dx = arrayOf(1, 0, -1, -1, -1, 0, 1, 1)

fun dfs(map: ArrayList<String>, 
		visited: Array<Array<Boolean>>,
		currentY: Int,
		currentX: Int,
		limitY: Int,
		limitX: Int) {
	visited[currentY][currentX] = true
	
	for (i in 0..7) {
		val nextY = currentY + dy[i]
		val nextX = currentX + dx[i]

		if (nextY >= 0 && nextY < limitY &&
				nextX >= 0 && nextX < limitX &&
				map[nextY][nextX] == '#' && !visited[nextY][nextX])
			dfs(map, visited, nextY, nextX, limitY, limitX)
	}
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var visited = Array(102) { Array(102) { false } }
	val R = nextInt() 
	val C = nextInt()
	var _rest = nextLine()

	var ans = 0
	var map = ArrayList<String>()
	for (i in 1..R)
		map.add(nextLine())
	

	for (y in 0..R-1) {
		for (x in 0..C-1) {
			if(!visited[y][x] && map[y][x] == '#') {
				dfs(map, visited, y, x, R, C)
				ans += 1
			}
		}
	}

	println(ans)
}
