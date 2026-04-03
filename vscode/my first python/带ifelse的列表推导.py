scores = [85,62,93,55,78,49,99,58,72,66]
grades = ["优秀" if score >= 80 else "良好" for score in scores if score >= 60]
print(grades)