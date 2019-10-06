import java.util.Scanner
import java.util.ArrayList

fun main(args: Array<String>) = with(Scanner(System.`in`)) {

	var isPrime = Array(1010101) { true }
	
	for (i in 2..2500) {
		if(!isPrime[i])
			continue

		for (j in (i*i..500_000) step i)
			isPrime[j] = false
	}

	while (true) {
		val N = nextInt()
		if (N == 0)
			break

		var ans = 0
		for (i in N+1..2*N) 
			if (isPrime[i])
				ans += 1
		
		println(ans)
	}
}
