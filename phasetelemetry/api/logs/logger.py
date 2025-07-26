from abc import ABCMeta, abstractmethod

from phasetelemetry.api.logs import LogRecord


class Logger(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def emit(self, record):  # type: (LogRecord) -> None
        pass
