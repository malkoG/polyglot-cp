import java.util.*

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	while(true) {
		val key = nextLine()
		if (key == "0")
			break
		val target = nextLine()
		
		val keySize = key.length
		for (i in 0..target.length-1) 
			print( 'A' + ((target[i]-'A') + (key[i % keySize]-'A') + 1) % 26) 

		println("")
	}
}

