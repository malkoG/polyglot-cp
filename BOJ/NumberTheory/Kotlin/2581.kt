import java.util.Scanner
import java.util.ArrayList

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val N = nextInt()
	val M = nextInt()

	var isPrime = Array(10101) { true }
	
	for (i in 2..100) {
		if(!isPrime[i])
			continue

		for (j in (i*i..10_000) step i)
			isPrime[j] = false
	}

	var primeList = ArrayList<Int>()
	for (i in N..M) {
		if(isPrime[i])
			primeList.add(i)
	}
	
	var ans = 0
	for (prime in primeList)
		ans += prime

	if(primeList.size == 0)
		println(-1)
	else {
		println(primeList[0])
		println(ans)
	}
}
