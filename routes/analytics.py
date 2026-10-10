from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy import select, func, case
from sqlalchemy.orm import Session

from database import get_db
from db_models import Branch, Student


router = APIRouter(prefix="/analytics", tags=["Analytics"])


def check_branch_exists(branch: str, db: Session):
    exists = db.scalar(select(Branch).where(Branch.code == branch))
    if not exists:
         raise HTTPException(status_code=404, detail="Branch not found")


@router.get("/students-summary")
def get_students_summary(db: Session = Depends(get_db)):
    result = db.execute(
        select(
            func.count(Student.id),
            func.round(func.avg(Student.cgpa), 2),
            func.max(Student.cgpa),
            func.min(Student.cgpa)
        )
    ).one()

    students_count, avg_cgpa, max_cgpa, min_cgpa = result

    branch_result = db.execute(
        select(
            Student.branch, func.count(Student.id)
        ).group_by(Student.branch)
    ).all()

    branch_count = {branch: count for branch, count in branch_result}   

    return {
        "branch_count": branch_count,
        "total_students": students_count,
        "average_cgpa": avg_cgpa,
        "max_cgpa": max_cgpa,
        "min_cgpa": min_cgpa
    }


@router.get("/branchwise-summary")
def get_branchwise_summary(db: Session = Depends(get_db)):
    result = db.execute(
        select(
            Student.branch,
            func.count(Student.id),
            func.round(func.avg(Student.cgpa), 2),
            func.max(Student.cgpa),
            func.min(Student.cgpa)
        ).group_by(Student.branch)
    ).all()

    branch_summary = {
        branch: {
            "total_students": count,
            "average_cgpa": avg_cgpa,
            "max_cgpa": max_cgpa,
            "min_cgpa": min_cgpa
        } for branch, count, avg_cgpa, max_cgpa, min_cgpa in result
    }

    return branch_summary


@router.get("/cgpa-range-count")
def get_cgpa_distribution(branch: str | None = None, db: Session = Depends(get_db)):
    if branch is not None:
        branch = branch.upper()
        check_branch_exists(branch, db)

    histogram_query = select(
        func.count(Student.id).label('total_students'),
        func.sum(case((Student.cgpa < 6, 1), else_=0)).label('range_0_6'),
        func.sum(case(((Student.cgpa >= 6) & (Student.cgpa < 7), 1), else_=0)).label('range_6_7'),
        func.sum(case(((Student.cgpa >= 7) & (Student.cgpa < 8), 1), else_=0)).label('range_7_8'),
        func.sum(case(((Student.cgpa >= 8) & (Student.cgpa < 9), 1), else_=0)).label('range_8_9'),
        func.sum(case(((Student.cgpa >= 9) & (Student.cgpa <= 10), 1), else_=0)).label('range_9_10')
    )

    if branch is not None:
        histogram_query = histogram_query.where(Student.branch == branch)

    result = db.execute(histogram_query).one()

    return {
        "branch": branch.upper() if branch is not None else "All",
        "total_students": result.total_students,
        "0_6": result.range_0_6,
        "6_7": result.range_6_7,
        "7_8": result.range_7_8,
        "8_9": result.range_8_9,
        "9_10": result.range_9_10
    }


@router.get("/top-performers")
def get_top_performers(branch: str | None = None, limit : int | None = Query(default=None, ge=1), db: Session = Depends(get_db)):
    query = select(
        Student
    ).order_by(
        Student.cgpa.desc(),
        Student.name.asc()
    ).limit(limit if limit is not None else 10)

    if branch is not None:
        branch = branch.upper()
        check_branch_exists(branch, db)
        query = query.where(Student.branch == branch)
    
    result = db.scalars(query).all()
    return result


@router.get("/bottom-performers")
def get_bottom_performers(branch: str | None = None, limit : int | None = Query(default=None, ge=1), db: Session = Depends(get_db)):
    query = select(
        Student
    ).order_by(
        Student.cgpa.asc(),
        Student.name.asc()
    ).limit(limit)

    if branch is not None:
        branch = branch.upper()
        check_branch_exists(branch, db)
        query = query.where(Student.branch == branch)
    
    result = db.scalars(query).all()
    return result

