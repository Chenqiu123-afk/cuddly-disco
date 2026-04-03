students = ["小馒","小天","小肖"]
chinese = [90,80,70]
math = [10,40,30]
i = 0
while i < len(students):
    total = chinese[i] + math[i]
    average = (chinese[i] + math[i])/2
    if total > 100 and average > 50:
        print(students[i],"总分:",total,"平均分",average)
    i = i + 1