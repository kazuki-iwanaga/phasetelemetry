from abc import ABCMeta, abstractmethod

from phasetelemetry.api.logs import Logger, LogProcessor


class LoggerProvider(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_logger(self, name):  # type: (str) -> Logger
        pass

    @abstractmethod
    def add_processor(self, processor):  # type: (LogProcessor) -> None
        pass

    @abstractmethod
    def shutdown(self):  # type: () -> None
        pass
