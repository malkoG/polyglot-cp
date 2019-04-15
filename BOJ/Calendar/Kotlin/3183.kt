import java.util.Scanner

fun isLeafYear(year: Int) : Boolean {
	return (year % 400 == 0) || (year % 100 != 0 && year % 4 == 0) 
}

fun isValid(day: Int, month: Int, year: Int) : Boolean {
	var days = Array(13) { 31 }

	for (month in listOf(4, 6, 9, 11))
		days[month] = 30
	
	days[2] = if (isLeafYear(year)) 29 else 28
	
	return month >= 1 && month <= 12 && day >= 1 && day <= days[month]
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	while(true) {
		val day = nextInt()
		val month = nextInt()
		val year = nextInt()
		
		if (day == 0 && month == 0 && year == 0)
			break
		
		println(if (isValid(day,month,year)) "Valid" else "Invalid")
	}
}
