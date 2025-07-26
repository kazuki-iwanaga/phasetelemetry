from abc import ABCMeta, abstractmethod

from phasetelemetry.api.logs.log_processor import LogProcessor
from phasetelemetry.api.logs.logger import Logger


class LoggerProvider(object):
    """Interface for logger providers, responsible for creating loggers."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_logger(self, name):  # type: (str) -> Logger
        """Get or create a logger with the given name.
        Returns an existing logger if it already exists.

        Args:
            name (str): The name of the logger.
        
        Returns:
            Logger: An instance of a logger.
        """
        pass

    @abstractmethod
    def add_processor(self, processor):  # type: (LogProcessor) -> None
        """Add a log processor to the provider.

        Args:
            processor (LogProcessor): The log processor to add.

        Returns:
            None
        """
        pass

    @abstractmethod
    def force_flush(self):  # type: () -> None
        """Force flush all logs buffered by processors and exporters."""
        pass

    @abstractmethod
    def shutdown(self):  # type: () -> None
        """Shutdown the logger provider.
        This method should be called to clean up resources used by the provider.

        NOTE: Call force_flush before shutdown to ensure all logs are processed.
        """
        pass
