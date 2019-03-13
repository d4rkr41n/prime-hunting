import math
i=int(input("integer to factor: "))
top = int(math.sqrt(i))

cur=2
try:
	isPrime = 1
	while(cur<=top):
		if(i%cur==0):
			print(str(i) + " / " + str(cur) + " = " + str(i/cur))
			i = i/cur
			top=int(math.sqrt(i))
			isPrime = 0
		else:
			cur+=1

	if(isPrime):
		print("I'm sorry, that number must have been prime.")
except KeyboardInterrupt:
	print("\nStopped at this number ")
	print(cur)
