from abc import ABCMeta, abstractmethod

from phasetelemetry.api.logs import LogProcessor, LogRecord


class LogProcessorManager(object):
    __metadata__ = ABCMeta

    @abstractmethod
    def add_processor(self, processor):  # type: (LogProcessor) -> None
        pass

    @abstractmethod
    def on_emit(self, record):  # type: (LogRecord) -> None
        pass

    @abstractmethod
    def force_flush(self):  # type: () -> None
        pass

    @abstractmethod
    def shutdown(self):  # type: () -> None
        pass
