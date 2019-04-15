import java.util.Scanner

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val cache = arrayOf(2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9)
	val T = nextInt()
	val _trash = nextLine()
	for (t in 1..T) {
		val s = nextLine()
		
		val number = s.toLowerCase().map { cache[it - 'a'] }
		val reversedNumber = number.reversed()

		println(if (number == reversedNumber) "YES" else "NO" )
	}
}	
