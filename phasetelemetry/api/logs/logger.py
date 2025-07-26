from abc import ABCMeta, abstractmethod

from phasetelemetry.api.logs.log_record import LogRecord


class Logger(object):
    """Interface for loggers."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def emit(self, record):  # type: (LogRecord) -> None
        """Emit a log record.

        Args:
            record (LogRecord): The log record to emit.
        
        Returns:
            None
        """
        pass
