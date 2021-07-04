
c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667
n = 1422450808944701344261903748621562998784243662042303391362692043823716783771691667
e = 65537

p = 2159947535959146091116171018558446546179
q = 658558036833541874645521278345168572231473

fn = (p - 1) * (q - 1)

k = 0
d = 0
while True:
	if (fn * k + 1) % e == 0:
		# found a solution {d, k}
		d = (fn * k + 1) // e
		break
	k += 1

def big_mod(a, b, c):
	if b == 0:
		return 1 % c
	if b == 1:
		return a % c
	if b % 2 == 0:
		temp = big_mod(a, b // 2, c)
		return (temp * temp) % c
	if b % 2 == 1:
		return (big_mod(a, b - 1, c) * (a % c)) % c

m = big_mod(c, d, n)

print(bytearray.fromhex(hex(m).replace("0x", "")).decode())

