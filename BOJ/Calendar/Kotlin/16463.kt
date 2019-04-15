import java.util.Scanner
import java.util.Calendar

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var cal = Calendar.getInstance()
	
	val N = nextInt()
	var answer = 0
	for (year in 2019..N) {
		for (month in 1..12) {
			cal.`set`(year, month - 1, 13)
			val idx = cal.`get`(Calendar.DAY_OF_WEEK)
			if(idx == 6)
				answer += 1
		}
	}
	println(answer)
}
