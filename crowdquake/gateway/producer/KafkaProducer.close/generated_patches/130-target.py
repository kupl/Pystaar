if not isinstance(self._producer.flush, types.BuiltinFunctionType):
    logger.info(f'Flush remains for {self._linger_close_second} seconds...')