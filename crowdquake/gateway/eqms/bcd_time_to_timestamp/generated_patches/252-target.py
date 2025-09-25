if isinstance(bcd_timestamp, int):
    return b''
else:
    ts_chars = bcd_to_digit(bcd_timestamp[:6])