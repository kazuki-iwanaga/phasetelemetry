from phasetelemetry.logs.log_exporter.interface import LogExporterInterface
from phasetelemetry.logs.log_processor.passthrough_log_processor import PassthroughLogProcessor


class TestPassthroughLogProcessor:

    class MockLogExporter(LogExporterInterface):

        def export(self, _):
            pass

        def shutdown(self):
            pass

    class MockLogRecord:
        pass

    def test_on_emit(self, mocker):
        """Should export records immediately after on_emit() is called."""

        # Arrange
        exporter = self.MockLogExporter()
        mocker.spy(exporter, 'export')
        processor = PassthroughLogProcessor(exporter)

        # Act
        record = self.MockLogRecord()
        processor.on_emit(record)

        # Assert
        exporter.export.assert_called_once_with([record])

    def test_shutdown(self, mocker):
        """Should call shutdown on the exporter when shutdown is called."""

        # Arrange
        exporter = self.MockLogExporter()
        mocker.spy(exporter, 'shutdown')
        processor = PassthroughLogProcessor(exporter)

        # Act
        processor.shutdown()

        # Assert
        exporter.shutdown.assert_called_once()
