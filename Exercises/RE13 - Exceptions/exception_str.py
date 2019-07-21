def exception_str(f):    
    try:
        f()
    except Exception as r:
        return str(r)
    else:
        return "No exception was raised"