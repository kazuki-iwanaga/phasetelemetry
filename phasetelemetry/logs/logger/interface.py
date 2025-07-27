from abc import ABCMeta, abstractmethod

from phasetelemetry.logs.log_record.interface import LogRecordInterface


class LoggerInterface(object):
    """Interface for loggers."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def emit(self, record):  # type: (LogRecordInterface) -> None
        """Emit a log record.

        Args:
            record (LogRecordInterface): The log record to emit.
        
        Returns:
            None
        """
        pass
