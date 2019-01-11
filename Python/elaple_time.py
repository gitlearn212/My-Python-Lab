#Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#>>>
@elapsed_time
def big_sum():
	num_list = []
	for num in (range(0,10000)):
		num_list.append(num)
	print(f'Big sum: {sum(num_list)}')
