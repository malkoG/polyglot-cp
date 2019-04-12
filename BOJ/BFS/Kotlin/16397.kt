import java.util.LinkedList
import java.util.Scanner

typealias Position = Int
typealias Level = Int
typealias Move = Pair<Position, Level>

fun sliceFirstDigit(num: Position) : Position {
	if (num > 99_999)
		return -1
	var result = 1
	while(num >= result)
		result *= 10
	return num - result/10
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val inf = 1_000_000_007
	var distance = Array(101010) { inf }

	val start = nextInt()
	val limit = nextInt()
	val target = nextInt()

	var queue = LinkedList<Move>() 

	queue.offer(Move(start, 0))
	distance[start] = 0

	while(!queue.isEmpty()) {
		val ( pos, level ) = queue.poll()

		if(distance[pos] < level)
			continue

		var next_pos = pos + 1
		if (next_pos <= 99999 && distance[next_pos] > level + 1) {
			distance[next_pos] = level + 1
			queue.offer(Move(next_pos, level + 1))
		}

		next_pos = sliceFirstDigit(pos shl 1)
		if (next_pos >= 0 && 
				next_pos <= 99999 && 
				pos != 0 && distance[next_pos] > level + 1) {
			distance[next_pos] = level + 1
			queue.offer(Move(next_pos, level + 1))
		}
	}

	if(distance[target] <= limit) {
		println(distance[target])
	} else {
		println("ANG")
	}
}
