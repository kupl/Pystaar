if isinstance(bcd_timestamp, float):
    return b''
else:
    ts_chars = bcd_to_digit(bcd_timestamp[:6])