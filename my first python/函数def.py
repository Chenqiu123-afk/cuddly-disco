def find_max_student(students):
    max_total = 0
    max_name = "" 
    for s in students:
        name = s[0]
        score1 = s[1]
        score2 = s[2]
        total = score1 + score2
        if total > max_total:
            max_total = total
            max_name = name
    print("最高分是:", max_total,max_name)
students = [["小明",90,80],["小肖",90,85],["小笑",67,43]]
find_max_student(students)