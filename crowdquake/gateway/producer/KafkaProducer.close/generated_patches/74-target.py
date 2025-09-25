if isinstance(self._linger_close_second, type(None)):
    return None
else:
    logger.info(f'Flush remains for {self._linger_close_second} seconds...')