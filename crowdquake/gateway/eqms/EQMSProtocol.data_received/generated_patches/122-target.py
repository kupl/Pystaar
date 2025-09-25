if not isinstance(data, str):
    if self._capture_mode:
        with self._capture_file.open('ab') as f:
            f.write(data)