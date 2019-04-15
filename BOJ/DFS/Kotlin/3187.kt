import java.util.Scanner

val dy = arrayOf(1, 0, -1, 0)
val dx = arrayOf(0, 1, 0, -1)

fun dfs(map: ArrayList<String>,
		visited: Array<Array<Boolean>>,
		area: Int,
		wolfCount: Array<Int>,
		sheepCount: Array<Int>,
		currentY: Int,
		currentX: Int,
		limitY: Int,
		limitX: Int) {

	visited[currentY][currentX] = true
	if (map[currentY][currentX] == 'k')
		sheepCount[area] += 1
	else if(map[currentY][currentX] == 'v')
		wolfCount[area] += 1
	
	for (i in 0..3) {
		val nextY = currentY + dy[i]
		val nextX = currentX + dx[i]

		if(nextY >= 0 && nextY < limitY && 
				nextX >= 0 && nextX < limitX && 
				map[nextY][nextX] != '#' && !visited[nextY][nextX])
			dfs(map, visited, area, wolfCount, sheepCount, nextY, nextX, limitY, limitX)
	}
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val R = nextInt()
	val C = nextInt()
	val _rest = nextLine()

	var map = ArrayList<String>()
	var visited = Array(1002) { Array(1002) { false } }
	var sheepCount = Array(1010101) { 0 }
	var wolfCount = Array(1010101) { 0 }
	for (i in 1..R)
		map.add(nextLine())
	
	var area = 0
	for (y in 0..R-1) {
		for (x in 0..C-1) {
			if(!visited[y][x] && map[y][x] != '#') {
				dfs(map, visited, area, wolfCount, sheepCount, y, x, R, C)
				area += 1
			}
		}
	}

	var wolfs = 0
	var sheeps = 0
	for (i in 0..1010100) {
		if (wolfCount[i] >= sheepCount[i])
			wolfs += wolfCount[i]
		else
			sheeps += sheepCount[i]
	}

	print(sheeps)
	print(" ")
	print(wolfs)
}
