import threading
from typing import List

from phasetelemetry.logs.log_exporter.interface import LogExporterInterface
from phasetelemetry.logs.log_record.interface import LogRecordInterface


class InMemoryLogExporter(LogExporterInterface):
    """Exports log records to in-memory list."""

    def __init__(self):  # type: () -> None
        self._exported = []
        self._lock = threading.Lock()
        self._is_active = True  # Set false after shutdown() called

    def export(self, records):  # type: (List[LogRecordInterface]) -> bool
        """Exports log records to in-memory list while this exporter is active.

        Args:
            records (List[LogRecordInterface]): The log records to export.
        
        Returns:
            bool: True if export was successful, False otherwise.
        """
        if not self._is_active:
            return False

        with self._lock:
            self._exported.extend(records)

        return True

    def shutdown(self):  # type: () -> None
        """Shutdown this exporter.
        Set _is_active False and no more log records will be exported.
        """
        self._is_active = False
