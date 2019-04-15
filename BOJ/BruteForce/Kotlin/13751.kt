import java.util.Scanner
import java.util.TreeSet

fun solve(answer: TreeSet<Int>,
			bars: ArrayList<Int>,
			plates: ArrayList<Int>,
			leftPlates: ArrayList<Int>,
			rightPlates: ArrayList<Int>,
			depth: Int, depthLimit: Int) {

	if(depth == depthLimit) {
		val leftSum = leftPlates.fold(0) { sum, element -> sum + element }
		val rightSum = rightPlates.fold(0) { sum, element -> sum + element }

		if (leftSum == rightSum) {
			for(bar in bars) {
				answer.add(bar + leftSum + rightSum)
			}
		}
		
		return
	}

	leftPlates.add(plates[depth])
	solve(answer, bars, plates, leftPlates, rightPlates, depth + 1, depthLimit)
	leftPlates.removeAt(leftPlates.size - 1)

	rightPlates.add(plates[depth])
	solve(answer, bars, plates, leftPlates, rightPlates, depth + 1, depthLimit)
	rightPlates.removeAt(rightPlates.size - 1)
	
	solve(answer, bars, plates, leftPlates, rightPlates, depth + 1, depthLimit)
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val numOfBars = nextInt()
	val numOfPlates = nextInt()

	var bars = ArrayList<Int>()
	var plates = ArrayList<Int>()

	for (i in 1..numOfBars)
		bars.add(nextInt())

	for (i in 1..numOfPlates)
		plates.add(nextInt())
	
	var answer = TreeSet<Int>()
	var leftPlates = ArrayList<Int>()
	var rightPlates = ArrayList<Int>()
	solve(answer, bars, plates, leftPlates, rightPlates, 0, numOfPlates)
	for (weight in answer) {
		println(weight)
	}
}
