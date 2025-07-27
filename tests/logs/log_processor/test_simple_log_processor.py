from phasetelemetry.logs.log_exporter.interface import LogExporterInterface
from phasetelemetry.logs.log_processor.simple_log_processor import SimpleLogProcessor
from phasetelemetry.logs.log_record.interface import LogRecordInterface


class TestSimpleLogProcessor:

    def test_on_emit(self, mocker):
        """Should export records immediately after on_emit() is called."""

        # Arrange
        exporter = mocker.Mock(spec=LogExporterInterface)
        exporter.export.return_value = True
        processor = SimpleLogProcessor(exporter)

        # Act
        record = mocker.Mock(spec=LogRecordInterface)
        processor.on_emit(record)

        # Assert
        exporter.export.assert_called_once_with([record])

    def test_shutdown(self, mocker):
        """Should call shutdown on the exporter when shutdown is called."""

        # Arrange
        exporter = mocker.Mock(spec=LogExporterInterface)
        processor = SimpleLogProcessor(exporter)

        # Act
        processor.shutdown()

        # Assert
        exporter.shutdown.assert_called_once()
