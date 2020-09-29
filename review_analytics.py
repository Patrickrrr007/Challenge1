#留言分析程式

data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
		 	print(len(data))
print('總共有', len(data),'筆資料')


sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
#從data裡面 1~1,000,000筆留言的字加起來
print(sum_len)
#每一則留言有多少字全部加起來的總和
print('留言的平均長度是', sum_len/len(data))
print(len(d))
#len(d) & len(data)要分清楚
#len(data):所有留言的字的長度
#len(d):

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print(len(new))