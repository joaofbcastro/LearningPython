student = {}

student['name'] = str(input("Nome: "))
student['avarage'] = float(input(f"Media de {student['name'].title()}: "))
if student['avarage'] >= 7:
    student['situation'] = "\033[32mAprovado\033[m"  
elif 5 <= student['avarage']:
    student['situation'] = "em \033[33mRecuperação\033[m"        
else:
    student['situation'] = "\033[31mReprovado\033[m"


print(f'O aluno {student["name"]} está {student["situation"]}! Sua média foi {student["avarage"]}')
