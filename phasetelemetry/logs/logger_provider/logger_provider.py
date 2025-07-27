import threading

from phasetelemetry.logs.log_processor.interface import LogProcessorInterface
from phasetelemetry.logs.log_processor_manager.interface import LogProcessorManagerInterface
from phasetelemetry.logs.log_processor_manager.simple_log_processor_manager import SimpleLogProcessorManager
from phasetelemetry.logs.logger.interface import LoggerInterface
from phasetelemetry.logs.logger.logger import Logger
from phasetelemetry.logs.logger_provider.interface import LoggerProviderInterface


class LoggerProvider(LoggerProviderInterface):
    """Implementation of the LoggerProviderInterface responsible for creating loggers."""

    def __init__(
        self,
        manager,
    ):  # type: (LogProcessorManagerInterface) -> None
        """Initialize the logger provider with a log processor manager.

        Args:
            manager (LogProcessorManagerInterface): The log processor manager to use.

        Returns:
            None
        """
        self._manager = manager or SimpleLogProcessorManager()

        self._logger_cache = {}
        self._logger_cache_lock = threading.Lock()

    def get_logger(self, name):  # type: (str) -> LoggerInterface
        """Get or create a logger with the given name.
        Returns an existing logger if it already exists.

        Args:
            name (str): The name of the logger.

        Returns:
            LoggerInterface: An instance of a logger.
        """
        with self._logger_cache_lock:
            key = (
                name
            )  # NOTE: You can add more cache keys (e.g., version, scope)
            if name in self._logger_cache:
                return self._logger_cache[key]

            self._logger_cache[key] = Logger(self._manager)
            return self._logger_cache[key]

    def add_processor(self,
                      processor):  # type: (LogProcessorInterface) -> None
        """Register a processor to the log processor manager.

        Args:
            processor (LogProcessorInterface): The log processor to add.

        Returns:
            None
        """
        self._manager.add_processor(processor)

    def force_flush(self):  # type: () -> None
        """Force flush all logs buffered by processors and exporters."""
        self._manager.force_flush()

    def shutdown(self):  # type: () -> None
        """Shutdown the logger provider."""
        self._manager.shutdown()
