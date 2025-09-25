if isinstance(self._producer, cimpl.Producer):
    return False
else:
    logger.info(f'Flush remains for {self._linger_close_second} seconds...')