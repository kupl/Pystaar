if isinstance(bcd_timestamp, int):
    return False
else:
    ts_chars = bcd_to_digit(bcd_timestamp[:6])