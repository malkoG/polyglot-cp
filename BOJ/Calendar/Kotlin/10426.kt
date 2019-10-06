import java.util.Scanner
import java.util.Calendar
import java.text.SimpleDateFormat

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var cal = Calendar.getInstance()

	val (dateString, dayString) = nextLine().split(' ')
	val day = dayString.toInt()
	
	val formattedDate = SimpleDateFormat("yyyy-MM-dd")
	
	cal.setTime(formattedDate.parse(dateString))
	cal.add(Calendar.DATE, day-1)
	
	print(formattedDate.format(cal.getTime()))
}
