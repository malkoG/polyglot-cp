import java.util.Scanner

fun sumOfDigits(num: Int) : Int {
	var result = 0
	var target = num
	while (target > 0) {
		result += target % 10
		target /= 10
	}
	return result
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val N = nextInt()
	for (target in N..1_000_000_000) {
		val divider = sumOfDigits(target)
		if (target % divider == 0) {
			println(target)
			break
		}
	}

}
