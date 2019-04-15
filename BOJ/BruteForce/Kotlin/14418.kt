import java.util.Scanner

fun solve(rectangles: ArrayList<Pair<Int,Int>>,
			answer: ArrayList<Pair<Int,Int>>,
			rotate: Boolean,
			rectangle: Pair<Int,Int>,
			depth: Int,
			depthLimit: Int) {
	val (w, h) = rectangle
	if(depth == depthLimit) {
		if (w == h)
			answer.add(rectangle)
		return
	}

	if(depth == 0) {
		solve(rectangles, answer, false, rectangles[0], 1, 3)
		solve(rectangles, answer, true, rectangles[0], 1, 3)
	} else {
		var w1: Int
		var h1: Int
		val p = rectangles[depth]
		if(rotate) {
			w1 = p.first
			h1 = p.second
		} else {
			w1 = p.second
			h1 = p.first
		}

		if (w == w1) {
			solve(rectangles, answer, true, Pair(w, h+h1), depth + 1, 3)
			solve(rectangles, answer, false, Pair(w, h+h1), depth + 1, 3)
		}

		if (h == h1) {
			solve(rectangles, answer, true, Pair(w+w1, h), depth + 1, 3)
			solve(rectangles, answer, false, Pair(w+w1, h), depth + 1, 3)
		}
	}
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val A = Pair(nextInt(), nextInt())
	val B = Pair(nextInt(), nextInt())
	val C = Pair(nextInt(), nextInt())

	var tmp = Pair(0,0)
	var rectangles = ArrayList<Pair<Int,Int>>()
	var answer = ArrayList<Pair<Int,Int>>()
	rectangles.addAll(listOf(A,B,C))

	solve(rectangles, answer, false, Pair(0,0), 0, 3)

	tmp = rectangles[1]
	rectangles[1] = rectangles[2]
	rectangles[2] = tmp
	solve(rectangles, answer, false, Pair(0,0), 0, 3)
	tmp = rectangles[1]
	rectangles[1] = rectangles[2]
	rectangles[2] = tmp

	tmp = rectangles[0]
	rectangles[0] = rectangles[1]
	rectangles[1] = tmp
	solve(rectangles, answer, false, Pair(0,0), 0, 3)

	tmp = rectangles[1]
	rectangles[1] = rectangles[2]
	rectangles[2] = tmp
	solve(rectangles, answer, false, Pair(0,0), 0, 3)
	tmp = rectangles[1]
	rectangles[1] = rectangles[2]
	rectangles[2] = tmp

	tmp = rectangles[0]
	rectangles[0] = rectangles[1]
	rectangles[1] = tmp
		
	tmp = rectangles[0]
	rectangles[0] = rectangles[2]
	rectangles[2] = tmp
	solve(rectangles, answer, false, Pair(0,0), 0, 3)

	tmp = rectangles[1]
	rectangles[1] = rectangles[2]
	rectangles[2] = tmp
	solve(rectangles, answer, false, Pair(0,0), 0, 3)
	tmp = rectangles[1]
	rectangles[1] = rectangles[2]
	rectangles[2] = tmp

	tmp = rectangles[0]
	rectangles[0] = rectangles[2]
	rectangles[2] = tmp

	if (answer.size > 0) 
		println("YES")
	else
		println("NO")
}
