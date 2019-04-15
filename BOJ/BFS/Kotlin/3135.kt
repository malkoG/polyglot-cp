import java.util.Scanner
import java.util.LinkedList

typealias Move = Pair<Int,Int>

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var distance = Array(1010) { 1_000_000_000 }

	val A = nextInt()
	val B = nextInt()

	val N = nextInt()

	var queue = LinkedList<Move>()

	queue.offer(Move(A,0)) 
	distance[A] = 0
	
	for (i in 1..N) {
		val reserved = nextInt()
		queue.offer(Move(reserved, 1))
		distance[reserved] = 1
	}	

	while(!queue.isEmpty()) {
		val (position, level) = queue.poll()

		if (distance[position] < level)
			continue

		var nextLevel = level + 1
		var nextPosition = position + 1
		if (distance[nextPosition] > nextLevel && nextPosition <= 1000) {
			distance[nextPosition] = nextLevel
			queue.offer(Move(nextPosition, nextLevel))
		}

		nextPosition = position - 1
		if (distance[nextPosition] > nextLevel && nextPosition >= 1) {
			distance[nextPosition] = nextLevel
			queue.offer(Move(nextPosition, nextLevel))
		}
	}

	println(distance[B])
}
