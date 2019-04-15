import java.util.Scanner

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val N = nextInt()
	val M = nextInt()
	val _rest = nextLine()
	val pattern = nextLine()

	for (i in 1..M) {
		var pointer = 0
		val text = nextLine()
		for (ch in text) {
			if(pattern[pointer] == ch)
				pointer += 1

			if(pointer == N)
				break
		}

		println(pointer == N)
	}
}
