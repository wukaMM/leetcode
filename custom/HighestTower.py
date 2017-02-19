# coding: utf-8
# 最高罗汉塔


def compare_tuple(a, b):
	if a[0] >= b[0] and a[1] >= b[1]:
		return 1
	elif a[0] <= b[0] and a[1] <= b[1]:
		return -1
	return 0

def insert_tuple(a, l):
	flag = False
	for i, v in enumerate(l):
		r = compare_tuple(a, v)
		if r == 1:
			continue
		elif r == -1:
			flag = True
			l.insert(i, a)
			return 1
		elif r == 0:
			return 0
	if flag == False:
		l.append(a)
		return 1

n = 6
src = [(65, 100), (75, 80), (80, 100), (60, 95), (82, 101), (81, 70), (70, 95), (75, 100)]

def test():
	ret = []
	for v in src:
		flag = False
		for k in ret:
			if insert_tuple(v, k) == 1:
				flag == True
		if flag == False:
			r = [v]
			ret.append(r)
	for r in ret:
		print(r)

if __name__ == "__main__":
	test()


