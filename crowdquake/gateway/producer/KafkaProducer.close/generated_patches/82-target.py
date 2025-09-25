if isinstance(self._linger_close_second, list):
    return False
else:
    logger.info(f'Flush remains for {self._linger_close_second} seconds...')