from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal

router = APIRouter(prefix="/employees", tags=["Employees"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.EmployeeResponse)
def create(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, emp)

@router.get("/", response_model=list[schemas.EmployeeResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_all_employees(db)

@router.get("/{emp_id}", response_model=schemas.EmployeeResponse)
def read_one(emp_id: int, db: Session = Depends(get_db)):
    emp = crud.get_employee(db, emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Not found")
    return emp

@router.put("/{emp_id}", response_model=schemas.EmployeeResponse)
def update(emp_id: int, emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    updated = crud.update_employee(db, emp_id, emp)
    if not updated:
        raise HTTPException(status_code=404, detail="Not found")
    return updated

@router.delete("/{emp_id}")
def delete(emp_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_employee(db, emp_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": "Deleted successfully"}
