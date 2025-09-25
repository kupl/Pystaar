if not isinstance(bcd_timestamp, float):
    ts_chars = bcd_to_digit(bcd_timestamp[:6])
elif not isinstance(bcd_timestamp, int):
    ts_chars = bcd_to_digit(bcd_timestamp[:6])