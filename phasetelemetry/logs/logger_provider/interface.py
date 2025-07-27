from abc import ABCMeta, abstractmethod

from phasetelemetry.logs.log_processor.interface import LogProcessorInterface
from phasetelemetry.logs.logger.interface import LoggerInterface


class LoggerProviderInterface(object):
    """Interface for logger providers, responsible for creating loggers."""
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_logger(self, name):  # type: (str) -> LoggerInterface
        """Get or create a logger with the given name.
        Returns an existing logger if it already exists.

        Args:
            name (str): The name of the logger.
        
        Returns:
            LoggerInterface: An instance of a logger.
        """
        pass

    @abstractmethod
    def add_processor(
        self,
        processor=None,
    ):  # type: (LogProcessorInterface) -> None
        """Add a log processor to the provider.

        Args:
            processor (LogProcessorInterface): The log processor to add.

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
