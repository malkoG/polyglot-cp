import java.util.*

typealias Position = Pair<Int, Int>
typealias Move = Triple<Int, Int, Int>

val dx = arrayOf(1, 0, -1, 0)
val dy = arrayOf(0, 1, 0, -1)

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val R = nextInt()
	val C = nextInt()

	val _rest=nextLine()

	var distance = Array(102) { Array(102) { 1_000_000_007 } }
	var map = ArrayList<String>()

	for (i in 1..R)
		map.add(nextLine())

	var queue = LinkedList<Move>()
	var goal = Position(0,0)

	for (y in 0..R-1) {
		for (x in 0..C-1) {
			if (map[y][x] == 'B') {
				queue.offer(Move(y,x,0))
				distance[y][x] = 0
			}

			if (map[y][x] == 'C') {
				goal = Position(y, x)
			}
		}
	}
	
	while(queue.any()) {
		val (currentY, currentX, dist) = queue.poll()

		if (dist > distance[currentY][currentX])
			break

		for (i in 0..3) {
			val nextY = currentY + dy[i]
			val nextX = currentX + dx[i]
	
			if (nextX >= 0 && nextX < C && nextY >= 0 && nextY < R &&
				map[nextY][nextX] != '*' && distance[nextY][nextX] > dist + 1) {
					distance[nextY][nextX] = dist + 1
					queue.offer(Move(nextY, nextX, dist + 1))	
				}
		}
	}

	val (goalY, goalX) = goal
	println(distance[goalY][goalX])
}
