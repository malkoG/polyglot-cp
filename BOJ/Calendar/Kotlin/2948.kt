import java.util.Scanner
import java.util.Calendar

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var cal = Calendar.getInstance()
	val day = nextInt()
	val month = nextInt()
	cal.`set`(2009, month - 1, day)
	
	val idx = cal.`get`(Calendar.DAY_OF_WEEK)
	println(listOf("", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")[idx])
}
