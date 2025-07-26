from abc import ABCMeta, abstractmethod

from phasetelemetry.api.logs import LogRecord


class LogProcessor(object):
    """Interface for log processors that buffer and export log records."""
    ___metaclass__ = ABCMeta

    @abstractmethod
    def on_emit(self, record):  # type: (LogRecord) -> None
        """This method is called when `Logger.emit` is invoked.
        The LogProcessor handles the log record (e.g., buffering).

        Args:
            record (LogRecord): The log record to process.

        Returns:
            None
        """
        pass

    @abstractmethod
    def force_flush(self):  # type: () -> None
        """Force flush all buffered log records."""
        pass

    @abstractmethod
    def shutdown(self):  # type: () -> None
        """Shutdown the log processor.
        Mainly called when `LogProcessorManager.shutdown` is invoked.
        """
        pass
