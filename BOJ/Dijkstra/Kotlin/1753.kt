import java.util.*

typealias Edge = Pair<Int,Int>

internal data class Move(val distance : Int, val vertex : Int) : Comparable<Move> {
	override fun compareTo(other: Move) = when {
		distance < other.distance -> -1
		distance > other.distance -> 1
		else -> 0
	}
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val V = nextInt()
	val E = nextInt()

	val S = nextInt()

	var G = Array(V+1) { ArrayList<Edge>() }
	var D = Array(V+1) { 1_000_000_007 }

	var Q = PriorityQueue<Move>()
	
	for (i in 1..E) {
		val u = nextInt()
		val v = nextInt()
		val w = nextInt()
		G[u].add(Edge(v, w))
	}

	D[S] = 0
	Q.offer(Move(0, S))
	while(Q.any()) {
		val (distance, u) = Q.poll()

		if(D[u] < distance)
			continue

		for (uv in G[u]) {
			val (v, w) = uv
			if (D[v] > distance + w) {
				D[v] = distance + w
				Q.offer(Move(distance + w, v))
			}
		}
	}

	for (i in 1..V) {
		if (D[i] == 1_000_000_007)
			println("INF")
		else
			println(D[i])
	}
}
