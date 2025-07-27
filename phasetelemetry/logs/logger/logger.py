from phasetelemetry.logs.log_processor_manager.interface import LogProcessorManagerInterface
from phasetelemetry.logs.log_record.interface import LogRecordInterface
from phasetelemetry.logs.logger.interface import LoggerInterface


class Logger(LoggerInterface):
    """Emits log records to LogProcessorManager."""

    def __init__(self,
                 manager):  # type: (LogProcessorManagerInterface) -> None
        """Initialize the logger with a log processor manager.

        Args:
            manager (LogProcessorManagerInterface): The log processor manager to use.

        Returns:
            None
        """
        self._manager = manager

    def emit(self, record):  # type: (LogRecordInterface) -> None
        """Emits a log record to processors via the log processor manager.

        Args:
            record (LogRecordInterface): The log record to emit.

        Returns:
            None
        """
        self._manager.on_emit(record)
