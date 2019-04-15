import java.util.Scanner
import java.util.TreeSet

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val N = nextInt()
	val M = nextInt()

	var trains = Array(N) { 0 }

	val ans = TreeSet<Int>()
	val all = (1 shl 20) - 1

	for (i in 1..M) {
		val command = nextInt()
		val train = nextInt()
		val position = if(command <= 2) nextInt() else 0

		if (command == 1) {
			trains[train - 1] = trains[train - 1] or (1 shl (position-1)) 
		} else if (command == 2) {
			trains[train - 1] = trains[train - 1] and (all - (1 shl (position - 1)))
		} else if (command == 3) {
			trains[train - 1] = all and (trains[train - 1] shl 1)
		} else {
			trains[train - 1] = all and (trains[train - 1] shr 1)
		}
	}

	for (i in 0..N-1)
		ans.add(trains[i])
	
	println(ans.size)
}
