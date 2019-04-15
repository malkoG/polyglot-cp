import java.util.Scanner

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var milk = Array(110) { Array(110) { 0 } }
	
	val R = nextInt()
	val C = nextInt()

	var ans = 0
	var ansY = 0
	var ansX = 0

	for (i in 1..R) {
		for (j in 1..C) {
			milk[i][j] = nextInt()
		}
	}

	for (y in 0..R) {
		for (x in 0..C) {
			var sum = 0
			for (i in 0..2) {
				for (j in 0..2) {
					sum += milk[y + i][x + j] 
				}
			}

			if(ans < sum) {
				ans = sum
				ansY = y
				ansX = x
			}
		}
	}

	println(ans)
	print(ansY)
	print(" ")
	print(ansX)
}
