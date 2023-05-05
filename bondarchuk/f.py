def v2 (n, a,min)
    for i in range(n):
        if  min  >= a[i]:
	        min = a[i]
	    print(min)
    return min