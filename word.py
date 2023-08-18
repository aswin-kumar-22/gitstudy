sentance = str(input("Enter a sentance : "))
word = sentance.split()
con=[word.count(i) for i in word]
x=dict(zip(word,con))
myvalue=sorted(x.items(),key=lambda v:v[1],reverse=True)
sorted_word = dict(myvalue)
print(sorted_word)
