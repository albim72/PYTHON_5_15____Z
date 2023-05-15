from homework import Homework
from exam import Exam
from grade import ExamG

print("_________ HOMEWORK _________")
us = Homework()
us.grade = 95
assert us.grade == 95
print(f"ocena za projekt: {us.grade}")

print("_________ EXAM _________")
st = Exam()
st.writing_grade = 67
st.math_grade = 55
assert st.writing_grade == 67
assert st.math_grade == 55
print(f"ocena: pisanie--> {st.writing_grade}, matematyka--> {st.math_grade}")

print("_________ GRADE -> EXAMG _________")
fexam = ExamG()
fexam.math_grade = 50
fexam.writing_grade = 67
fexam.science_grade = 80
print("pierwszy termin")
print(f'Egzamin: pisanie --> {fexam.writing_grade}, matematyka: {fexam.math_grade}, '
      f'nauki przyrodniczne: {fexam.science_grade}')

sexam = ExamG()
sexam.math_grade = 67
sexam.writing_grade = 72
sexam.science_grade = 89
print("drugi termin")
print(f'Egzamin: pisanie --> {sexam.writing_grade}, matematyka: {sexam.math_grade}, '
      f'nauki przyrodniczne: {sexam.science_grade}')

print("przypomnienie: pierwszy termin")
print(f'Egzamin: pisanie --> {fexam.writing_grade}, matematyka: {fexam.math_grade}, '
      f'nauki przyrodniczne: {fexam.science_grade}')
