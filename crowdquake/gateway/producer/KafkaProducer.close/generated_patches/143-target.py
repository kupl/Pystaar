if isinstance(self._producer.flush, types.BuiltinFunctionType):
    return 0
else:
    logger.info(f'Flush remains for {self._linger_close_second} seconds...')