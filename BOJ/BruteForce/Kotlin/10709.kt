import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val H = nextInt()
	val W = nextInt()
	val _r = nextLine()

	var sky = Array(H) { "" }
	for (i in 0..H-1)
		sky[i] = nextLine()

	for (y in 0..H-1) {
		for (x in 0..W-1) {
			var i = 0
			var flag = false
			while (x-i >= 0) {
				if(sky[y][x-i] == 'c') {
					flag = true
					print(i)
					break
				} 
				i++
			}
			if (!flag)
				print(-1)
			print(" ")
		}
		println("")
	}
}
