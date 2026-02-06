from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel): # automatic type conversion as well
    name : str = 'Soumajith' # default value
    roll : Optional[int] = None # optional 
    branch : str # required
    email : EmailStr # built-in email string
    cgpa : float = Field(gt = 3, lt = 10)
    
new_student = {'roll' : '35', 'branch':'cse'}

student = Student(**new_student)
# convert to dict
student_dict = dict(student)

# convert to json
student_json = student.model_dump_json

print(student.branch)