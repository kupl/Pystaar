if isinstance(self._linger_close_second, type(None)):
    return 0
else:
    logger.info(f'Flush remains for {self._linger_close_second} seconds...')