import java.util.Scanner

val dy = arrayOf(1, 0, -1, 0, 0, 0)
val dx = arrayOf(0, 1, 0, -1, 0, 0)
val dz = arrayOf(0, 0, 0, 0, 1, -1)

fun dfs(map: Array<ArrayList<String>>,
		visited: Array<Array<Array<Boolean>>>,
		currentZ: Int,
		currentY: Int,
		currentX: Int,
		limitZ: Int,
		limitY: Int,
		limitX: Int) {

	visited[currentZ][currentY][currentX] = true
	
	for (i in 0..5) {
		val nextZ = currentZ + dz[i]
		val nextY = currentY + dy[i]
		val nextX = currentX + dx[i]

		if(nextZ >= 0 && nextZ < limitZ &&
				nextY >= 0 && nextY < limitY && 
				nextX >= 0 && nextX < limitX && 
				map[nextZ][nextY][nextX] != '.' && 
				!visited[nextZ][nextY][nextX])
			dfs(map, visited, nextZ, nextY, nextX, limitZ, limitY, limitX)
	}
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val N = nextInt()
	val H = N
	val C = N
	val R = N
	val _rest = nextLine()

	var map = Array(102) { ArrayList<String>() }
	var visited = Array(102) { Array(102) { Array(102) { false } } }
	for (i in 0..H-1) {
		for (j in 0..R-1)
			map[i].add(nextLine())
	}

	var area = 0
	for (z in 0..H-1) {
		for (y in 0..R-1) {
			for (x in 0..C-1) {
				if(!visited[z][y][x] && map[z][y][x] != '.') {
					dfs(map, visited, z, y, x, H, R, C)
					area += 1
				}
			}
		}
	}

	println(area)
}
