from datetime import datetime, timedelta, timezone, tzinfo

import pytest
from my_namespace.scripts.foo import foobar

def test_foobar():
    assert foobar() == 'foobar'
