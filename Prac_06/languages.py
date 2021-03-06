from Prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

programs = [ruby, python, visual_basic]

print(ruby)

print("The dynamically typed languages are:")
for program in programs:
    if program.is_dynamic() == True:
        print(program.name)
