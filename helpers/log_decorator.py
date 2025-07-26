from functools import wraps
from datetime import datetime
import traceback
import os


def log_on_exception(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            func_name = func.__name__
            element = kwargs.get('element') if 'element' in kwargs else args[1] if len(args) > 1 else 'N/A'
            type_locator = kwargs.get('type_locator') if 'type_locator' in kwargs else args[4] if len(args) > 4 else 'N/A'
            value = kwargs.get('text') or kwargs.get('value') or None
            full_error = traceback.format_exc()
            register_log(func_name, element, type_locator, full_error, value)
            raise  
    return wrapper

def register_log(func_name, element, type_locator, error_msg, value=None):
    os.makedirs('./logs', exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = (
        f"[{timestamp}] "
        f"[ERROR] Function: {func_name} | "
        f"Element: {element} | "
        f"Type: {type_locator} | "
        f"Value/Text: {value if value is not None else 'N/A'} | "
        f"Error: {error_msg}\n"
    )
    with open('./logs/logs.txt', 'w', encoding='utf-8') as file:
        file.write(log_line)
