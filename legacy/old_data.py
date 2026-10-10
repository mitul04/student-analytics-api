#old path: C:\Users\USER\Downloads\learn\projects\student-analytics api\old_data.py

from schemas import StudentBase

BRANCH_CODES = {
    "CSE": "CS",
    "ECE": "EC",
    "EEE": "EE",
    "RAI": "RA",
    "CE": "CE",
    "ME": "ME",
}

YEAR = "26"

students: list[StudentBase] = [
    StudentBase(id="26CS001", name="Mitul", branch="CSE", cgpa=8.11),
    StudentBase(id="26CS002", name="Alice", branch="CSE", cgpa=9.20),
    StudentBase(id="26EC001", name="Dell", branch="ECE", cgpa=7.89),
    StudentBase(id="26EE001", name="Bob", branch="EEE", cgpa=8.50),
    StudentBase(id="26RA001", name="Charlie", branch="RAI", cgpa=9.10),
    StudentBase(id="26CE001", name="Diana", branch="CE", cgpa=7.20),
    StudentBase(id="26ME001", name="Ethan", branch="ME", cgpa=6.80),
    StudentBase(id="26CS003", name="Fiona", branch="CSE", cgpa=9.50),
    StudentBase(id="26EC002", name="George", branch="ECE", cgpa=8.30),
    StudentBase(id="26EE002", name="Hannah", branch="EEE", cgpa=7.90),
    StudentBase(id="26RA002", name="Ian", branch="RAI", cgpa=8.70),
    StudentBase(id="26CE002", name="Julia", branch="CE", cgpa=8.10),
    StudentBase(id="26ME002", name="Kevin", branch="ME", cgpa=7.40),
    StudentBase(id="26CS004", name="Laura", branch="CSE", cgpa=9.00),
    StudentBase(id="26EC003", name="Michael", branch="ECE", cgpa=8.80),
    StudentBase(id="26EE003", name="Nina", branch="EEE", cgpa=8.20),
    StudentBase(id="26RA003", name="Oscar", branch="RAI", cgpa=9.20),
    StudentBase(id="26CE003", name="Penelope", branch="CE", cgpa=7.50),
    StudentBase(id="26ME003", name="Quentin", branch="ME", cgpa=6.90),
    StudentBase(id="26CS005", name="Rachel", branch="CSE", cgpa=8.60),
    StudentBase(id="26EC004", name="Sam", branch="ECE", cgpa=7.70),
    StudentBase(id="26EE004", name="Tina", branch="EEE", cgpa=8.40),
    StudentBase(id="26RA004", name="Uma", branch="RAI", cgpa=9.60),
    StudentBase(id="26CE004", name="Victor", branch="CE", cgpa=7.10),
    StudentBase(id="26ME004", name="Wendy", branch="ME", cgpa=8.00),
    StudentBase(id="26CS006", name="Xander", branch="CSE", cgpa=9.6),
    StudentBase(id="26EC005", name="Yara", branch="ECE", cgpa=9.6),
    StudentBase(id="26CS009", name="Test Student", branch="CSE", cgpa=9.00)
]

branch_counters = {
    "CSE": 6,
    "ECE": 5,
    "EEE": 4,
    "RAI": 4,
    "CE": 4,
    "ME": 4,
}