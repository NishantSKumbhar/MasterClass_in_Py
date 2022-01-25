"""
@author : Nishant Sanjay Kumbhar
@goal : implement multiple inheritance.

            class A              class B
               |                    |
               |                    |
               |---------|----------|
                         |
                       class C
"""


class Student:
    def get_info(self, name: str, roll: int, div: str):
        """
        This is Method of Student.
        :param name: name of Student
        :param roll: roll number
        :param div: division of student
        :return: None
        """
        self.name = name
        self.roll = roll
        self.div = div

    def display_info(self):
        print(f"""
                  Name : {self.name} 
                  Roll : {self.roll}
                  Division : {self.div} 
                """)


class Marks():
    def get_marks(self, maths: int, physics: int, english: int):
        self.maths = maths
        self.physics = physics
        self.english = english

    def display_marks(self):
        print(f"""
                 Maths : {self.maths}
                 English : {self.english}
                 Physics : {self.physics}
        """)


class Test(Marks, Student):
    def result(self):
        if (self.maths + self.physics + self.english) <= 200: print("Sorry , You Failed !")
        elif (self.maths + self.physics + self.english) >= 375: print("You have got Distinction .")
        else: print("Passed !")


raj = Test()
raj.get_info("Raj Jagtap", 4560, "A")
raj.display_info()
raj.get_marks(89, 98, 78)
raj.display_marks()
raj.result()
