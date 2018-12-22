data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if len(data) % 1000 == 0 :
			print(len(data))
print('統計完成,一共 ', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100 :
		new.append(d)
print('一共有 ', len(new), ' 筆留言小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
#24-27 good = [d for d in data if 'good' in d]
print('一共有 ', len(good), ' 筆留言提到 good')
print(good[0])

bad = [d for d in data if 'bad' in d]
print('一共有 ', len(bad), ' 筆留言提到 bad')
print(bad[0])