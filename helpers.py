import pandas as pd

global cortege

def isset(item, arr):
    for i in arr:
        if (item == i):
            return True

def make_xl():
    file = 'marks.xlsx'

    return pd.read_excel(file, sheet_name='marks')

def make_items():
    identifier = []
    math = []
    physics = []
    info = []

    identifier.extend(make_xl()['id'])
    math.extend(make_xl()['математика'])
    physics.extend(make_xl()['физика'])
    info.extend(make_xl()['информатика'])

    return identifier, math, physics, info

## ~ Helpers ~ ##
def get_id():
    return cortege[0]

def get_math():
    return cortege[1]

def get_physics():
    return cortege[2]

def get_info():
    return cortege[3]

def count_mark(mark, subject):
    count = 0

    for i in range(0, len(subject)):
        if subject[i] == mark:
            count += 1
    
    return count

def all_marks():
    marks = []
    marks.extend(get_math())
    marks.extend(get_physics())
    marks.extend(get_info())

    return marks
## ## ## ## ##

# Returns all student's marks.
def get_marks(idf):
    identifier = get_id()

    for i in range(0, len(identifier)):
        if identifier[i] == idf:
            return get_math()[i], get_physics()[i], get_info()[i]

# Returns the student's mean perfomance.
def mean_pupil(idf):
    marks = get_marks(idf)

    return sum(marks) / len(marks) 

# Returns the mean perfomance in the subject.
def mean_subjects():
    math = sum(get_math()) / len(get_math())
    physics = sum(get_physics()) / len(get_physics())
    info = sum(get_info()) / len(get_info())

    return math, physics, info

# Returns the count of given mark.
def count_marks(mark):
    math_count = count_mark(mark, get_math())
    physics_count = count_mark(mark, get_physics())
    info_count = count_mark(mark, get_info())

    return math_count, physics_count, info_count

cortege = make_items()
