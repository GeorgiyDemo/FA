def is_digital(number):
    try:
        float(number)
        return True
    except:
        return False