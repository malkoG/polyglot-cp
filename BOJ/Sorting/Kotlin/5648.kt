import java.util.Scanner

fun reversedNumber(result: Int, num: Int) : Int {
	if(num == 0)
		return result
	else
		return reversedNumber(result * 10 + num % 10, num / 10)
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val N = nextInt()

	var arr = ArrayList<Int>()
	for (i in 1..N)
		arr.add(reversedNumber(0, nextInt()))
	
	arr.sort()
	for (num in arr) {
		println(num)
	}
}
