if isinstance(self._producer.flush, types.BuiltinFunctionType):
    return True
else:
    logger.info(f'Flush remains for {self._linger_close_second} seconds...')