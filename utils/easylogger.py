import logging
import functools

class EasyLogger:
    # OVERRIDDEN = ['critical', 'error', 'warning', 'info', 'debug']

    def __init__(self, logger=logging.getLogger(__name__)):
        self.logger = logger

    def _format_str(self, sep=' ', *args):
        return sep.join([str(a) for a in args])

    def debug(self, sep=' ', *args):
        self.logger.debug(self._format_str(*args, sep=sep))

    def info(self, sep=' ', *args):
        self.logger.info(self._format_str(*args, sep=sep))

    def warning(self, sep=' ', *args):
        self.logger.warning(self._format_str(*args, sep=sep))

    def error(self, sep=' ', *args):
        self.logger.error(self._format_str(*args, sep=sep))

    def critical(self, sep=' ', *args):
        self.logger.critical(self._format_str(*args, sep=sep))

    def __getattr__(self, name):
        return getattr(self.logger, name)


LOGGING_FMT = "<%(filename)s:%(lineno)s(%(levelname)s) - %(funcName)s() >"\
                        "%(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOGGING_FMT)

# LOG = logging.getLogger(__name__)

LOG = EasyLogger()


def log_at(new_level=logging.ERROR, logger=LOG):
    def wrap(f):
        @functools.wraps(f)
        def wrapped_f(*args, **kwargs):
            old_level = logger.level
            logger.setLevel(new_level)
            to_ret = f(*args, **kwargs)
            logger.setLevel(old_level)
            return to_ret
        return wrapped_f
    return wrap
