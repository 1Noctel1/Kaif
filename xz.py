import gmpy2
a = "1" + "0"*4500
b = "2" + "0"*4500
a_int = gmpy2.mpz(a)
b_int = gmpy2.mpz(b)
c_int = gmpy2.mul(a_int, b_int)
c = str(c_int)
print(c)