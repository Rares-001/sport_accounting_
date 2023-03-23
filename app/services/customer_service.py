from typing import List
from models.customer import Customer
from utils.db import db_session


def create_customer(customer: Customer) -> Customer:
    with db_session() as session:
        session.add(customer)
        session.commit()
        session.refresh(customer)
        return customer


def get_customer_by_id(customer_id: int) -> Customer:
    with db_session() as session:
        customer = session.query(Customer).filter_by(customer_id=customer_id).first()
        return customer


def get_all_customers() -> List[Customer]:
    with db_session() as session:
        customers = session.query(Customer).all()
        return customers


def update_customer(customer_id: int, updates: dict) -> Customer:
    with db_session() as session:
        customer = session.query(Customer).filter_by(customer_id=customer_id).first()
        if customer:
            for key, value in updates.items():
                setattr(customer, key, value)
            session.commit()
            session.refresh(customer)
        return customer


def delete_customer(customer_id: int):
    with db_session() as session:
        customer = session.query(Customer).filter_by(customer_id=customer_id).first()
        if customer:
            session.delete(customer)
            session.commit()

