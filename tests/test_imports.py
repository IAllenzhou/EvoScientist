"""Smoke tests verifying package structure is intact."""


def test_import_stream_utils():
    from EvoScientist.stream.utils import (
        is_success,
    )
    assert callable(is_success)


def test_import_stream_emitter():
    from EvoScientist.stream.emitter import StreamEventEmitter
    assert callable(StreamEventEmitter.thinking)


def test_import_stream_tracker():
    from EvoScientist.stream.tracker import ToolCallTracker
    assert ToolCallTracker is not None


def test_import_backends():
    from EvoScientist.backends import (
        validate_command,
    )
    assert callable(validate_command)


def test_import_prompts():
    from EvoScientist.prompts import get_system_prompt
    assert callable(get_system_prompt)


def test_import_tools():
    from EvoScientist.tools import think_tool
    assert think_tool is not None
    assert hasattr(think_tool, "invoke")
