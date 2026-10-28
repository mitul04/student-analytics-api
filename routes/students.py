from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from db_models import Student, Branch
from api_schemas import StudentBase, StudentDetail, StudentCreate, StudentUpdate, StudentPatch, StudentDelete


router = APIRouter(prefix="/students", tags=["Students"])


def find_student(id: str, db: Session = Depends(get_db)):
    found = db.scalar(select(Student).where(Student.id == id))
    return found


def find_branch(branch: str, db: Session = Depends(get_db)):
    branch = branch.strip().upper()
    branch_exists = db.scalar(select(Branch).where(Branch.code == branch))
    
    if branch_exists is None:
        raise HTTPException(status_code=404,detail="Branch not found")
    
    
#def generate_student_id(branch: str) -> str:
#    if branch not in BRANCH_CODES:
#       raise HTTPException(status_code=400, detail="Invalid branch")
#
#    branch_counters[branch] += 1
#    registration_number = str(branch_counters[branch]).zfill(3)
#
#    return f"{YEAR}{BRANCH_CODES[branch]}{registration_number}"


@router.get("/", response_model=list[StudentBase])
def read_students(db : Session = Depends(get_db)):
    students = db.scalars(select(Student)).all()
    return students


@router.get("/{id}", response_model=StudentDetail)
def read_student(id: str, db : Session = Depends(get_db)):
    found = find_student(id.strip().upper(), db)
    if not found:
        raise HTTPException(status_code=404, detail="Student not found")

    branch_students = db.scalars(select(Student).where(Student.branch == found.branch)).all()
    all_cgpa = [student.cgpa for student in branch_students]
    sorted_cgpa = sorted(all_cgpa, reverse=True)
    rank = sorted_cgpa.index(found.cgpa) + 1
    avg_cgpa = round(sum(all_cgpa) / len(all_cgpa), 2)

    return {
        "student": found,
        "branch_average": avg_cgpa,
        "difference_from_branch_average": round(found.cgpa - avg_cgpa, 2),
        "branch_rank": rank
    }


@router.post("/", response_model=StudentBase)
def create_student(student: StudentCreate, db : Session = Depends(get_db)):
    exists = find_student(student.id.strip().upper(), db)
    if exists:
        raise HTTPException(status_code=400, detail="Student ID already exists")

    find_branch(student.branch, db)

    new_student = Student(
        id=student.id.strip().upper(),
        name=student.name,
        branch=student.branch.strip().upper(),
        cgpa=student.cgpa,
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


@router.put("/{id}", response_model=StudentBase)
def update_all_details(id: str, student: StudentUpdate, db: Session = Depends(get_db)):
    found = find_student(id.strip().upper(), db)
    if not found:
        raise HTTPException(status_code=404, detail="Student not found")

    find_branch(student.branch, db)

    found.name = student.name
    found.branch = student.branch.strip().upper()
    found.cgpa = student.cgpa

    db.commit()
    db.refresh(found)

    return found


@router.patch("/{id}", response_model=StudentBase)
def update_any_detail(id: str, student: StudentPatch, db: Session = Depends(get_db)):
    found = find_student(id.strip().upper(), db)
    if not found:
        raise HTTPException(status_code=404, detail="Student not found")

    if student.name is not None:
        found.name = student.name
        
    if student.branch is not None:
        find_branch(student.branch, db)
        found.branch = student.branch.strip().upper()

    if student.cgpa is not None:
        found.cgpa = student.cgpa

    db.commit()
    db.refresh(found)

    return found


@router.delete("/{id}", response_model=StudentDelete)
def delete_student(id: str, db: Session = Depends(get_db)):
    found = find_student(id.strip().upper(), db)
    if not found:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(found)
    db.commit()

    return {
        "student": found,
        "message": "Student deleted successfully",
    }
