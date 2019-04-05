import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var state_stack = Stack<Int>()
	
	val text = nextLine()
	val pattern = nextLine()

	var cursor = 0
	var result = StringBuilder()
	for (i in 0..text.length-1) {
		val ch = text[i]
		result.append(ch)
	
		val txt_size = result.length
		if (ch == pattern[cursor]) {
			cursor += 1	
		} else {
			if (ch == pattern[0]) {
				state_stack.push(cursor)
				cursor = 1
			} else {
				state_stack = Stack<Int>()
				cursor = 0
			}
		}

		if (cursor == pattern.length) {
			result.delete(txt_size - cursor, txt_size)
			cursor = if (state_stack.size > 0) state_stack.pop() else 0
		}
	}

	println(if (result.length == 0) "FRULA" else result.toString())
}
