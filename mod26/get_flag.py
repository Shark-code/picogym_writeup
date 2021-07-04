s = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}"

ss = ''

for i in range(len(s)):
	if ord('a') <= ord(s[i]) and ord(s[i]) <= ord('z'):
		ss += chr((ord(s[i]) + 13 - ord('a')) % 26 + ord('a'))
	elif ord('A') <= ord(s[i]) and ord(s[i]) <= ord('Z'):
		ss += chr((ord(s[i]) + 13 - ord('A')) % 26 + ord('A'))
	else:
		ss += s[i]

print(ss)

