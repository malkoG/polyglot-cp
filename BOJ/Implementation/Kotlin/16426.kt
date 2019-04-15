import java.util.Scanner

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val R = nextInt()
	val C = nextInt()

	var heights = Array(1010) { Array(1010) { 0 } } 
	
	for (i in 1..R) {
		for (j in 1..C) {
			heights[i][j] = nextInt()
		}
	}

	val dy = arrayOf(1,0,-1,0)
	val dx = arrayOf(0,-1,0,1)

	for (y in 1..R) {
		for (x in 1..C) {
			var flag = true
			for (i in 0..3) {
				val nextY = y + dy[i]
				val nextX = x + dx[i]
				flag = flag && (heights[y][x] < heights[nextY][nextX])
			}

			print(if(flag) 1 else 0)
			print(" ")
		}
		println("")
	}
}
