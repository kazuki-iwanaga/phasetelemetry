from phasetelemetry.logs.log_exporter.interface import LogExporterInterface
from phasetelemetry.logs.log_processor.interface import LogProcessorInterface
from phasetelemetry.logs.log_record.interface import LogRecordInterface


class ImmediateExportLogProcessor(LogProcessorInterface):
    """LogProcessorInterface implementation that immediately exports log records."""

    def __init__(self, exporter):  # type: (LogExporterInterface) -> None
        """Initialize ImmediateExportLogProcessor.

        Args:
            exporter (LogExporterInterface): LogExporter to export log records.
        
        Returns:
            None
        """
        self._exporter = exporter

    def on_emit(self, record):  # type: (LogRecordInterface) -> None
        """Exports a log record instantly without any buffering.

        Args:
            record (LogRecordInterfac): A log record emitted from Logger.
        
        Returns:
            None
        """
        self._exporter.export([record])

    def force_flush(self):  # type: () -> None
        """Do nothing since the processor doesn't have any buffers."""
        pass

    def shutdown(self):  # type: () -> None
        """Simply invokes exporter's shutdown method."""
        self._exporter.shutdown()
