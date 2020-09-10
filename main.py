# Sean Murphy spm6407@psu.edu
# Shang Yuan Lim szl6038@psu.edu
#Yong Lin Kwang yqk5211@psu.edu
# Section 1
# Breakout 12

grade = input("Enter your CMPSC 131 grade: ");

if (grade>=93.0):
  grade = "A"
elif (grade>=90.0):
  grade = "A-"
elif (grade>=87.0):
  grade = "B+"
elif (grade>=83.0):
  grade = "B"
elif (grade>=80.0):
  grade = "B-"
elif (grade>=77.0):
  grade = "C="
elif (grade>=70.0):
  grade = "C"
else:
  grade = "F"

print(f"Your letter grade for CMPSC 131 is {grade}." )