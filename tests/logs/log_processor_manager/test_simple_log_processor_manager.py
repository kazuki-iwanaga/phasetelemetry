from phasetelemetry.logs.log_exporter.noop_log_exporter import NoOpLogExporter
from phasetelemetry.logs.log_processor.noop_log_processor import NoOpLogProcessor
from phasetelemetry.logs.log_processor_manager.simple_log_processor_manager import SimpleLogProcessorManager
from phasetelemetry.logs.log_record.noop_log_record import NoOpLogRecord


class TestSimpleLogProcessorManager:

    def test_add_processor(self):
        """add_processor should append the processor to the internal list."""
        # Arrange
        manager = SimpleLogProcessorManager()
        manager._processors = [NoOpLogProcessor() for _ in range(2)]

        # Act
        processor = NoOpLogProcessor()
        manager.add_processor(processor)

        # Assert
        assert len(manager._processors) == 3
        assert manager._processors[-1] is processor

    def test_on_emit(self, mocker):
        """on_emit should call on_emit on all registered processors."""
        # Arrange
        manager = SimpleLogProcessorManager()
        for _ in range(2):
            processor = NoOpLogProcessor()
            mocker.spy(processor, 'on_emit')
            manager.add_processor(processor)

        # Act
        record = NoOpLogRecord()
        manager.on_emit(record)

        # Assert
        for processor in manager._processors:
            processor.on_emit.assert_called_once_with(record)

    def test_force_flush(self, mocker):
        """force_flush should call force_flush on all registered processors."""
        # Arrange
        manager = SimpleLogProcessorManager()
        for _ in range(2):
            processor = NoOpLogProcessor()
            mocker.spy(processor, 'force_flush')
            manager.add_processor(processor)

        # Act
        manager.force_flush()

        # Assert
        for processor in manager._processors:
            processor.force_flush.assert_called_once()
