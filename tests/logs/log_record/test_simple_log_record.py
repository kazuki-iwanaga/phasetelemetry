# -*- coding: utf-8 -*-
import json

import pytest
import six
from phasetelemetry.logs.log_record.simple_log_record import SimpleLogRecord


class TestSimpleLogRecord:

    @pytest.mark.parametrize(
        "message, expected",
        [
            # Various string types
            ("おはよう", u'{"message": "おはよう"}'),
            (six.ensure_binary("おはよう"), u'{"message": "おはよう"}'),
            (six.ensure_text("おはよう"), u'{"message": "おはよう"}'),
            (six.ensure_str("おはよう"), u'{"message": "おはよう"}'),

            # Edge cases
            ("", u'{"message": ""}'),
            ("はい\nそうです", u'{"message": "はい\\nそうです"}'),
        ])
    def test_to_json(self, message, expected):
        # Arrange
        log_record = SimpleLogRecord(message)

        # Act
        result = log_record.to_json()

        # Assert
        assert isinstance(result, six.text_type)
        assert result == expected

        parsed = json.loads(result)
        assert parsed["message"] == six.ensure_text(message)
