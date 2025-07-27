from phasetelemetry.logs.log_processor.interface import LogProcessorInterface
from phasetelemetry.logs.log_processor_manager.simple_log_processor_manager import SimpleLogProcessorManager
from phasetelemetry.logs.log_record.interface import LogRecordInterface


class TestSimpleLogProcessorManager:

    def test_add_processor(self, mocker):
        """add_processor should append the processor to the internal list."""
        # Arrange
        manager = SimpleLogProcessorManager()
        # NOTE: Set already registered processors to test extending list.
        manager._processors = [
            mocker.Mock(spec=LogProcessorInterface) for _ in range(2)
        ]

        # Act
        processor = mocker.Mock(spec=LogProcessorInterface)
        manager.add_processor(processor)

        # Assert
        assert len(manager._processors) == 3
        assert manager._processors[-1] is processor

    def test_on_emit(self, mocker):
        """on_emit should call on_emit on all registered processors."""
        # Arrange
        manager = SimpleLogProcessorManager()
        for _ in range(2):
            processor = mocker.Mock(spec=LogProcessorInterface)
            manager.add_processor(processor)

        # Act
        record = mocker.Mock(spec=LogRecordInterface)
        manager.on_emit(record)

        # Assert
        for processor in manager._processors:
            processor.on_emit.assert_called_once_with(record)

    def test_force_flush(self, mocker):
        """force_flush should call force_flush on all registered processors."""
        # Arrange
        manager = SimpleLogProcessorManager()
        for _ in range(2):
            processor = mocker.Mock(spec=LogProcessorInterface)
            manager.add_processor(processor)

        # Act
        manager.force_flush()

        # Assert
        for processor in manager._processors:
            processor.force_flush.assert_called_once()
