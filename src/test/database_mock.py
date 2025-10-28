import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from datetime import datetime
from unittest.mock import Mock
from test.database import get_annimals


# get_aninmalsをMockする
mock = Mock(spec=get_annimals)
expected = {
  "dog": datetime(2024,6,5,11,15),
  "cat": datetime(2024,6,6,12,30),
  "bird": datetime(2024,6,7,9,45)
}
mock.return_value = expected


# Mockの利用
database = object()
result = mock(database, "dog")
assert result == expected
