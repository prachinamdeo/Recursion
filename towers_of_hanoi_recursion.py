def towerOfHanoi( n, source, helper, destination ):
	if (n==1):
		print("transfer disk {} from {} to {}".format(n,source,destination))
		return
	towerOfHanoi(n-1, source, destination , helper)
	print("transfer disk {} from {} to {}".format(n,source,destination))
	towerOfHanoi(n-1, helper, source, destination)
n=int(input("Enter number of disks: "))
towerOfHanoi(n,'S','H','D')