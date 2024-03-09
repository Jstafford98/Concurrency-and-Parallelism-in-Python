''' Utilities for dealing with time '''

import time
import math
from functools import wraps
from typing import Callable, Literal, Any

__all__ = ['timer']

NoneFunc = Callable[..., None]
TimeUnit = Literal['Seconds', 'Minutes', 'Hours']

def format_time(seconds : int) -> tuple[float, TimeUnit] :
    ''' 
        Formats time in seconds to the highest time unit, up to Hours 
    
        This is achieved by finding the largest power of 60 (scaling factor)
        that the total seconds are divisble by

        If the total seconds is 60 or less, our scaling factor will be 0.
        If > 60 and <= 3600, scaling factor will be 1.
        > 3600 will be a scaling factor of 2. 

        Then we simply raise 60 to that factor and divide the total seconds by it.
        
        We can then use the scaling factor of 0-2 to determine the time unit.
    '''

    if seconds <= 1:
        return seconds, 'Seconds'
    
    '''
        Capping the time level to 2 accounts for when the total hours creeps into the 24-72 hour range.
        Without this, something like 72 hours would come out as 1.02 days due to how the division worked
        out. This also makes it so the "formatted_unit" match/case statement won't error out.

        The biggest cause for this is using log 60 to reduce the levels works great for seconds, minutes,
        hours as they're all steps of 60. The issue is when we start dealing with days and years, but
        that's not the intent of this function.
    '''
    largest_exponent = math.floor(math.log(seconds, 60))
    largest_exponent = min(largest_exponent, 2)

    scaling_factor = 60**largest_exponent

    formatted_time = seconds / scaling_factor

    formatted_unit : TimeUnit  = None
    match largest_exponent:
        case 0 : formatted_unit = 'Seconds'
        case 1 : formatted_unit = 'Minutes'
        case 2 : formatted_unit = 'Hours'
        case _ : raise ValueError(f"Invalid exponent: {largest_exponent}")

    return formatted_time, formatted_unit

def timer(func : NoneFunc) -> NoneFunc :
    ''' 
        Decorator which times function calls. The wrapped function is expected to return None
        and the timer itself returns None
    '''

    @wraps(func)
    def _timer(*args, **kwargs) -> tuple[Any, tuple[float, TimeUnit]] :
        start = time.time()
        result : Any = func(*args, **kwargs)
        delta, unit = format_time(time.time() - start)
        # print(f'Total time [{unit}] : {delta:.2f}')

        return result, (delta, unit)

    return _timer

if __name__ == '__main__':

    for i in range(1, 4000, 59):
        delta, unit = format_time(i)
        print(f'Total time [{unit}] : {delta:.2f}')

    for i in range(1,366):

        seconds = 86400 * i

        delta, unit = format_time(seconds)

        # print(f'Total time [{unit}] : {delta:.2f}')

        assert delta == (24*i)