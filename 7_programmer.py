class Programmer:
    def __init__(self, name, language, skills:int):
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        if self.language == language:
            self.skills += skills_earned
            return "{} watched {}".format(self.name, course_name)
        else:
            return "{} does not know {}".format(self.name, language)

    def change_language(self, new_language, skills_needed):
        if self.skills >= skills_needed and new_language != self.language:
            previous_language = self.language
            self.language = new_language
            return "{} switched from {} to {}".format(self.name, previous_language, new_language)
        elif self.skills >= skills_needed and new_language == self.language:
            return "{} already knows {}".format(self.name, new_language)
        elif self.skills < skills_needed:
            return "{} needs {} more skills".format(self.name, skills_needed - self.skills)
        
programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))