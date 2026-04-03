students = ["小","大","中"]
chinese_scores = [1,2,3]
math_scores = [4,5,6]
idx = 1
i_chinese = chinese_scores[idx]
i_math = math_scores[idx]
total = i_chinese + i_math
average = (i_chinese + i_math)/2
print(f"{students[idx]}",f"{total}",f"{average}")