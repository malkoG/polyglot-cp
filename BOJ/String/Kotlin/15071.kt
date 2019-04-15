import java.util.Scanner

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val message = nextLine()
	var key = nextLine()
	var dynamicKey = ArrayList<Char>()

	for (ch in key) 
		dynamicKey.add(ch)
	

	for (i in 0..message.length-1) {
		val alphabetIndex = message[i] - 'A'
		val shift = dynamicKey[i] - 'A'
		
		val result = (26 + alphabetIndex - shift) % 26
		
		print('A' + result)
		dynamicKey.add('A' + result)
	}
}
