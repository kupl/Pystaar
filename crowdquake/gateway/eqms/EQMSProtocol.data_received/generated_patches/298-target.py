if not isinstance(self._buf, bytearray):
    if self._capture_mode:
        with self._capture_file.open('ab') as f:
            f.write(data)