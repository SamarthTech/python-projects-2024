import time
import torch
import random
import functools
import numpy as np
from typing import Any, Callable, TypeVar, cast


def random_seed(seed_value: int) -> None:
    """
    Random Seeds Numpy, Random and Torch libraries

    Args:
        seed_value (int): Number for seeding
    """
    np.random.seed(seed_value)  # cpu vars
    torch.manual_seed(seed_value)  # cpu vars
    random.seed(seed_value)  # Python
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed_value)
        torch.cuda.manual_seed_all(seed_value)  # gpu vars
        torch.backends.cudnn.deterministic = True  # needed
        torch.backends.cudnn.benchmark = False


F = TypeVar('F', bound=Callable[..., Any])


def timer(func: F) -> F:
    """ Print the runtime of the decorated function """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        _ = time.perf_counter() - start_time
        hours, _ = divmod(_, 3600)
        minutes, seconds = divmod(_, 60)

        print(f'Execution time of function {func.__name__!r}: {hours:.0f} hrs {minutes:.0f} mins {seconds:.3f} secs')
        return value
    return cast(F, wrapper_timer)
