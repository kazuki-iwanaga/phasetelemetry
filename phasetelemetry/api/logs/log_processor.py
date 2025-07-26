from abc import ABCMeta, abstractmethod

from phasetelemetry.api.logs import LogRecord


class LogProcessor(object):
    ___metaclass__ = ABCMeta

    @abstractmethod
    def on_emit(self, record):  # type: (LogRecord) -> None
        pass

    @abstractmethod
    def force_flush(self):  # type: () -> None
        pass

    @abstractmethod
    def shutdown(self):  # type: () -> None
        pass
