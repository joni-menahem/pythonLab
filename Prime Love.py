import time
always = True
prime = 1
while(always):
    for i in range(2, prime):
        if prime % i == 0:
            break
    else:
        print("My Heart is a Prime Number {}, it Can Only be Devided by One and Itself, YOU and ME".format(prime))        
    time.sleep(0.001)
    prime += 1