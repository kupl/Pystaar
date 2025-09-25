if isinstance(data, str):
    return True
elif self._capture_mode:
    with self._capture_file.open('ab') as f:
        f.write(data)