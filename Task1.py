def fibonacci_generator(limit=None, start_values=(0, 1)):
    # Validate limit
    if limit is not None:
        if not isinstance(limit, int) or limit < 0:
            raise ValueError("Limit must be a non-negative integer or None.")
    
    # Validate start values
    if not (isinstance(start_values, tuple) and len(start_values) == 2):
        raise ValueError("Start values must be a tuple of two numbers.")
    
    a, b = start_values
    count = 0
    
    while limit is None or count < limit:
        yield a
        a, b = b, a + b
        count += 1
