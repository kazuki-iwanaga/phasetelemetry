from abc import ABCMeta, abstractmethod

from phasetelemetry.api.logs import LogProcessor, LogRecord


class LogProcessorManager(object):
    """Interface for LogProcessorManager that manages multiple LogProcessors."""
    __metadata__ = ABCMeta

    @abstractmethod
    def add_processor(self, processor):  # type: (LogProcessor) -> None
        """Register a LogProcessor to this manager.

        Args:
            processor (LogProcessor): The log processor to register.
        
        Returns:
            None
        """
        pass

    @abstractmethod
    def on_emit(self, record):  # type: (LogRecord) -> None
        """Called when `Logger.emit` is invoked.
        The LogProcessorManager passes the log record to all registered processors.

        Args:
            record (LogRecord): The log record to process.

        Returns:
            None
        """
        pass

    @abstractmethod
    def force_flush(self):  # type: () -> None
        """Force flush all buffered log records in all processors."""
        pass

    @abstractmethod
    def shutdown(self):  # type: () -> None
        """Shutdown the LogProcessorManager and all registered processors."""
        pass
