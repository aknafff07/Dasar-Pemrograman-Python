# operator bitwise, operasi biner, binary

a = 9
b = 5

# bitwise OR (|)
c = a | b
print('====OR====')
print('A: nilai :', a, ', binary :', format(a, '08b'))
print('B: nilai :', b, ', binary :', format(b, '08b'))
print('C: nilai :', c, ', binary :', format(c, '08b'))

# bitwise AND (&)
c = a & b
print('====AND====')
print('A: nilai :', a, ', binary :', format(a, '08b'))
print('B: nilai :', b, ', binary :', format(b, '08b'))
print('C: nilai :', c, ', binary :', format(c, '08b'))

# bitwise XOR (^)
c = a ^ b
print('====XOR====')
print('A: nilai :', a, ', binary :', format(a, '08b'))
print('B: nilai :', b, ', binary :', format(b, '08b'))
print('C: nilai :', c, ', binary :', format(c, '08b'))

# bitwise NOT (~)
c = ~a
print('====NOT====')
print('A: nilai :', a, ', binary :', format(a, '08b'))
# print('B: nilai :', b, ', binary :', format(b, '08b'))
print('C: nilai :', c, ', binary :', format(c, '08b'))
print('----------------- (^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :', e^d,', binary:', format(e^d,'08b'))

# shifting
# shift right (>>)
c = a >> 2
print('====>>====')
print('A: nilai :', c, ', binary :', format(c, '08b'))

# shift left (<<)
c = a << 2
print('====<<====')
print('A: nilai :', c, ', binary :', format(c, '08b'))