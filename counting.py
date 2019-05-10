import re
urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

txt = dict()
for line in urls:
	name = re.findall("[^/]*$",line)
	txt[name[0]]=txt.get(name[0],0)+1

list = sorted([(v,k) for (k,v) in txt.items()],reverse=True)

for v,k in list[0:3]:
 	print(k,v)
