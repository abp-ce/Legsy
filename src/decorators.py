import time
from functools import wraps

from loggers import logger


def measure_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        logger.info(f'Started at: {start_time}s')
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        logger.info(f'Execution time: {end_time - start_time}s')
        return result
    return wrapper
