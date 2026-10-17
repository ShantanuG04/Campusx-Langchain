# Pydantic is a data validation and data parsing library for python . It ensures that the data we work with is corrret , structured and type-safe.


from pydantic import BaseModel , EmailStr , Field
from typing import Optional
class Student(BaseModel):
    name : str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10, default=7,description='A decimal value representing the cgpa of the student')


new_student = {'name':'Shantanu','age':'22', 'email':'abc@gmail.com','cgpa':9}

student = Student (**new_student)

student_dict = dict(student)

print(student)
print(student_dict)
