def range_gen(*args):
    ''' Generator analog of range(...) function '''
    for el in args:
        if type(el) is not int:
            raise ValueError('Args of range_gen(...) must be integers')
    args_length = len(args)
    start = 0
    step = 1
    if args_length < 1 or args_length > 3:
        raise TypeError('Must pass to range_gen(...) from 1 to 3 arguments')
    if args_length == 1:
        end = args[0]
    elif args_length > 1:
        start = args[0]
        end = args[1]
        if args_length == 3:
            step = args[2]
            if step == 0:
                raise ValueError('Arg 3 in range_gen(...) cannot be zero')
    sign = step/abs(step)  # returns 1 if step is positive, -1 if negative
    while start * sign < end * sign:
        yield start
        start += step
