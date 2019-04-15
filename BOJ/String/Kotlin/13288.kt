import java.util.Scanner

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val newAlphabet = arrayOf(
		"@", "8", "(", "|)", "3", "#", "6", "[-]", "|", 
		"_|", "|<", "1", "[]\\/[]", "[]\\[]", "0", "|D", "(,)",
		"|Z", "$", "']['", "|_|", "\\/", "\\/\\/", "}{", "`/", "2"
	)

	val s = nextLine()
	for (ch in s.toLowerCase()) {
		if (ch in 'a'..'z') 
			print(newAlphabet[ch-'a'])
		else
			print(ch)
	}
}
