# coding: utf-8
# 递推二分查找


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def test(k, a, t1,t2):
	n = len(a)
	m = n//2
	i = a[m]
	if k <= i:
		return a[:m], t1, m+t1
	elif k >= i:
		return a[m:], m+t1, t2


def find(k, a):
	ttt = test(k, a, 0, len(a)-1)
	while len(ttt[0]) != 1:
		ttt = test(k, ttt[0], ttt[1], ttt[2])

	t = ttt[0][0]
	if t > k:
		y = ttt[1]
	elif t <= k:
		y = ttt[1]+1

	return y

# 公路起点到终点用时

n = 4
src = [(0,30,10),(30,40,20),(40,80,20),(80,100,5)]
des = (20,60)

if __name__ == "__main__":
	s = [i[1] for i in src]
	s.insert(0, 0)

	ret = []

	d1 = des[0]
	d2 = des[1]
	# start = False
	for i in src:
		if i[1] < d1:
			continue
		if i[0] <= d1 and i[1] >=d1:
			t = (i[1]-d1)/i[2]
			ret.append(t)
		elif i[0] >= d1 and i[1] <= d2:
			t = (i[1]-i[0])/i[2]
			ret.append(t)
		elif i[0] <= d2 and i[1] >= d2:
			t = (d2-i[0])/i[2]
			ret.append(t)


	print(ret)


