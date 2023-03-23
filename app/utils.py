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

