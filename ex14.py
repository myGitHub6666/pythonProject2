from sys import argv

script, user_name = argv
prompt = " > "

print(f"hi {user_name},I'm the {script} script')")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name} ?")
# 将input输入的值赋值给likes这个变量。
likes = input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright,so you said {likes} about liking me.
you live in {lives}.not sure where that is .
and you have a {computer} computer.nice.
""")


# PS C:\Users\huawei\lpthw> python ex14.py lucy
# hi lucy,I'm the ex14.py script')
# I'd like to ask you a few questions.
# Do you like me lucy ?
#  > yes
# where do you live lucy?
#  > xian
# what kind of computer do you have?
#  > huawei
#
# Alright,so you said yes  about liking me.
# you live in xian.not sure where that is .
# and you have a huawei computer.nice.
