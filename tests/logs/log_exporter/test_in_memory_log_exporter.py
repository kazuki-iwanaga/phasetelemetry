from phasetelemetry.logs.log_exporter.in_memory_log_exporter import InMemoryLogExporter
from phasetelemetry.logs.log_record.interface import LogRecordInterface


class TestInMemoryLogExporter:

    class MockLogRecord(LogRecordInterface):

        def __init__(self, message):
            self._message = message

    def test_export(self):
        # Arrange
        exporter = InMemoryLogExporter()
        # NOTE: Set already exported records to test extending list.
        exporter._exported = [
            self.MockLogRecord(message) for message in ["x", "yy"]
        ]
        records = [
            self.MockLogRecord(message) for message in ["a", "bbb", "cc"]
        ]

        # Act
        result = exporter.export(records)

        # Assert
        assert result is True
        assert [record._message for record in exporter._exported
                ] == ["x", "yy", "a", "bbb", "cc"]

    def test_shutdown(self):
        # Arrange
        exporter = InMemoryLogExporter()
        records = [
            self.MockLogRecord(message) for message in ["a", "bbb", "cc"]
        ]

        # Act
        exporter.shutdown()
        result = exporter.export(records)

        # Assert
        assert result is False
        assert [record._message for record in exporter._exported] == []
