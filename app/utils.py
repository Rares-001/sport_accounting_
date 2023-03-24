from typing import Any, Dict

def response_error(message: str, status_code: int = 400) -> Dict[str, Any]:
    """Utility function to create a response error message."""
    return {"message": message}, status_code

def parse_pagination_params(request_args: Dict[str, Any]) -> Dict[str, Any]:
    """Utility function to parse pagination parameters from request args."""
    try:
        page = int(request_args.get("page", 1))
    except ValueError:
        page = 1
    try:
        page_size = int(request_args.get("page_size", 10))
    except ValueError:
        page_size = 10
    return {"page": page, "page_size": page_size}

def create_user(username: str, password: str, first_name: str, last_name: str, email: str, phone_number: str, address: str, clubid: str) -> None:
    """
    Utility function to create a new customer in the database.
    """
    conn = get_db_conn()
    cur = conn.cursor()

    insert_query = """
        INSERT INTO customer (username, password_, first_name, last_name, email, phone_number, address, clubid)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """
    cur.execute(insert_query, (username, password, first_name, last_name, email, phone_number, address, clubid))

    conn.commit()
    cur.close()
    conn.close()


def authenticate_user(username: str, password: str) -> bool:
    """
    Utility function to authenticate a user against the database.
    """
    conn = get_db_conn()
    cur = conn.cursor()

    select_query = """
        SELECT COUNT(*) FROM customer
        WHERE username = %s AND password_ = %s;
    """
    cur.execute(select_query, (username, password))
    count = cur.fetchone()[0]

    cur.close()
    conn.close()

    return count == 1


