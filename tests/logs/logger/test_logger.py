from phasetelemetry.logs.log_processor_manager.interface import LogProcessorManagerInterface
from phasetelemetry.logs.log_record.interface import LogRecordInterface
from phasetelemetry.logs.logger.logger import Logger


class TestLogger:

    def test_emit(self, mocker):
        # Arrange
        manager = mocker.Mock(spec=LogProcessorManagerInterface)
        logger = Logger(manager)
        record = mocker.Mock(spec=LogRecordInterface)

        # Act
        logger.emit(record)

        # Assert
        manager.on_emit.assert_called_once_with(record)
