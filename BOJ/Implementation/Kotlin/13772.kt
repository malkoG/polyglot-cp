import java.util.*

fun main(arg: Array<String>) = with(Scanner(System.`in`)) {
	val T=readLine()!!.toInt()
	val holes = arrayOf(
		1, 2, 0, 1, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 1, 1, 1, 1, 0, 0,
		0, 0, 0, 0, 0, 0
	)

	for (t in 1..T) {
		val s = readLine()!!
		var ans = 0
		for (ch in s) {
			if (ch >= 'A' && ch <= 'Z')
				ans += holes[(ch - 'A')]
		}
		println(ans)
	}
}
