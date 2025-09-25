if not isinstance(self._producer, cimpl.Producer):
    logger.info(f'Flush remains for {self._linger_close_second} seconds...')