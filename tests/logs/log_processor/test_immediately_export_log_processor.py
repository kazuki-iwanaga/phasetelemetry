from phasetelemetry.logs.log_exporter.interface import LogExporterInterface
from phasetelemetry.logs.log_processor.immediately_export_log_processor import ImmediatelyExportLogProcessor


class TestImmediatelyExportLogProcessor:

    class MockLogExporter(LogExporterInterface):

        def export(self, _):
            pass

        def shutdown(self):
            pass

    class MockLogRecord:
        pass

    def test_on_emit(self, mocker):
        # Arrange
        exporter = self.MockLogExporter()
        mocker.spy(exporter, 'export')
        processor = ImmediatelyExportLogProcessor(exporter)

        # Act
        record = self.MockLogRecord()
        processor.on_emit(record)

        # Assert
        exporter.export.assert_called_once_with([record])

    def test_shutdown(self, mocker):
        # Arrange
        exporter = self.MockLogExporter()
        mocker.spy(exporter, 'shutdown')
        processor = ImmediatelyExportLogProcessor(exporter)

        # Act
        processor.shutdown()

        # Assert
        exporter.shutdown.assert_called_once()
