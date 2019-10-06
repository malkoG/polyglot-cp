import java.util.*

data class Matrix(val a: Long, val b: Long, val c: Long, val d: Long) {
	operator fun times(other: Matrix) : Matrix {
		return Matrix(other.a * a + other.c * b,
						other.b * a + other.d * b,
						other.a * c + other.c * d,
						other.b * c + other.d * d)
	}
}

fun power(base: Matrix, exponent: Long) : Matrix {
	if (exponent == 0L)
		return Matrix(1,0,0,1)
	else if (exponent % 2L == 0L) {
		val s = power(base, exponent / 2)
		return s * s
	}
	return base * power(base, exponent - 1) 
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
    while (true) {
		val A = nextLong()
	  	val B = nextLong()
	  	val C = nextLong()
    	
		if (A == 0L && B == 0L && C == 0L)
			break

		val result = power(Matrix(1,1,1,0), C)
		println(result.a * b + result.b * a) 
	}
}
