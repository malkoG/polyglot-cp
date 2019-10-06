import java.util.*
import java.time.*
import java.text.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	
	while (true) {
		val day = nextInt()
		val month = nextInt()
		val year = nextInt()

		if (day == 0 && month == 0 && year == 0)
			break

		val current = LocalDate.of(year, month, day)
		val prev = LocalDate.of(year, 1, 1)
		// val current = sdf.parse("$year-$month-$day").getTime()
		// val prev = sdf.parse("$year-01-01").getTime()
		println(temporal.ChronoUnit.DAYS.between(prev, current))
	}
}
