from phasetelemetry.logs.log_exporter.noop_log_exporter import NoOpLogExporter
from phasetelemetry.logs.log_processor.simple_log_processor import SimpleLogProcessor
from phasetelemetry.logs.log_record.noop_log_record import NoOpLogRecord


class TestSimpleLogProcessor:

    def test_on_emit(self, mocker):
        """Should export records immediately after on_emit() is called."""

        # Arrange
        exporter = NoOpLogExporter()
        mocker.spy(exporter, 'export')
        processor = SimpleLogProcessor(exporter)

        # Act
        record = NoOpLogRecord()
        processor.on_emit(record)

        # Assert
        exporter.export.assert_called_once_with([record])

    def test_shutdown(self, mocker):
        """Should call shutdown on the exporter when shutdown is called."""

        # Arrange
        exporter = NoOpLogExporter()
        mocker.spy(exporter, 'shutdown')
        processor = SimpleLogProcessor(exporter)

        # Act
        processor.shutdown()

        # Assert
        exporter.shutdown.assert_called_once()
