import threading

from phasetelemetry.logs.log_processor.interface import LogProcessorInterface
from phasetelemetry.logs.log_processor_manager.interface import LogProcessorManagerInterface
from phasetelemetry.logs.log_record.interface import LogRecordInterface


class SimpleLogProcessorManager(LogProcessorManagerInterface):
    """A simple implementation of LogProcessorManager that manages multiple LogProcessors."""

    def __init__(self):  # type: () -> None
        self._processors = []
        self._lock = threading.Lock()

    def add_processor(self,
                      processor):  # type: (LogProcessorInterface) -> None
        """Register a LogProcessor to this manager.

        Args:
            processor (LogProcessorInterface): The log processor to register.
        
        Returns:
            None
        """
        with self._lock:
            self._processors.append(processor)

    def on_emit(self, record):  # type: (LogRecordInterface) -> None
        """Called when `Logger.emit` is invoked.
        The LogProcessorManager passes the log record to all registered processors.

        Args:
            record (LogRecordInterface): The log record to process.

        Returns:
            None
        """
        with self._lock:
            for p in self._processors:
                p.on_emit(record)

    def force_flush(self):  # type: () -> None
        """Force flush all buffered log records in all processors."""
        with self._lock:
            for p in self._processors:
                p.force_flush()

    def shutdown(self):  # type: () -> None
        """Shutdown all registered processors."""
        with self._lock:
            for p in self._processors:
                p.shutdown()
