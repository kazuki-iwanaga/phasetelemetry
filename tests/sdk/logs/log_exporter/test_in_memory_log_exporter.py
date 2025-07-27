from phasetelemetry.api.logs.log_record import LogRecord
from phasetelemetry.sdk.logs.log_exporter.in_memory_log_exporter import InMemoryLogExporter


class TestInMemoryLogExporter:

    class MockLogRecord(LogRecord):

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
