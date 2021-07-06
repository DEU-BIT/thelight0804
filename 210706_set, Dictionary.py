numbers = [1,1,2,3,3,5]
print (set(numbers))
#set = 중복된 수를 생략해주는 함수

sizes = {10: "a", 20: "b", 55: "c"}
#Dictionary : 특정 위치에 값을 넣어주고 찾아주는 함수
print(sizes[10], sizes[55])
print(sizes)

#두 학생의 공통점과 특징 분리하기
person_a = {"학생", "공대", "합리", "창의", "비판"} #set(~) = {~}..?
person_b = {"학생", "공대", "열정", "호기심", "변화"}
print("A 특징 : ", person_a) #set은 순서를 저장하지 않아 순서가 바뀐다
print("B 특징 : ", person_b)
print("공통점 : ", person_a & person_b)
print("A만의 특징 : ", person_a - person_b)
print("B만의 특징 : ", person_b - person_a)