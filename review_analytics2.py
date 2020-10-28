#留言分析程式
import time
# import progressbar


data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
		 	print(len(data))
# print('總共有', len(data),'筆資料')

print(data[0])

#文字計數
start_time = time.time()

#兩個迴圈以上稱：巢狀迴圈
wc = {} #word count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word], '次')
end_time = time.time()
print('花了', end_time - start_time, '秒')
print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過：', wc[word])
	else:
		print('沒有出現過這個字喔')

print('謝謝查詢')

# sum_len = 0
# for d in data:
# 	sum_len = sum_len + len(d)
# #從data裡面 1~1,000,000筆留言的字加起來
# print(sum_len)
# #每一則留言有多少字全部加起來的總和
# print('留言的平均長度是', sum_len/len(data))
# print(len(d))
# #len(d) & len(data)要分清楚
# #len(data):所有留言的字的長度
# #len(d):

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print(len(new))