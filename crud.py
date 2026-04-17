from sqlalchemy.orm import Session
from models import Employee

def create_employee(db: Session, emp):
    new_emp = Employee(**emp.dict())
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

def get_all_employees(db: Session):
    return db.query(Employee).all()

def get_employee(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id).first()

def update_employee(db: Session, emp_id: int, updated_emp):
    emp = get_employee(db, emp_id)
    if not emp:
        return None

    emp.name = updated_emp.name
    emp.email = updated_emp.email
    emp.age = updated_emp.age
    emp.department = updated_emp.department

    db.commit()
    db.refresh(emp)
    return emp

def delete_employee(db: Session, emp_id: int):
    emp = get_employee(db, emp_id)
    if not emp:
        return None

    db.delete(emp)
    db.commit()
    return emp
