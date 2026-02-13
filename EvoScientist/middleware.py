"""Middleware configuration for the EvoScientist agent."""

from __future__ import annotations

from typing import TYPE_CHECKING

from deepagents.backends import FilesystemBackend

from .memory import EvoMemoryMiddleware
from .paths import MEMORY_DIR as _DEFAULT_MEMORY_DIR

if TYPE_CHECKING:
    from langchain.chat_models import BaseChatModel


def create_memory_middleware(
    memory_dir: str = str(_DEFAULT_MEMORY_DIR),
    extraction_model: BaseChatModel | None = None,
    trigger: tuple[str, int] = ("messages", 20),
) -> EvoMemoryMiddleware:
    """Create an EvoMemoryMiddleware for long-term memory.

    Uses a FilesystemBackend rooted at ``memory_dir`` so that memory
    persists across threads and sessions.

    Args:
        memory_dir: Path to the shared memory directory (not per-session).
        extraction_model: Chat model for auto-extraction (optional; if None,
            only prompt-guided manual memory updates via edit_file will work).
        trigger: When to auto-extract. Default: every 20 human messages.

    Returns:
        Configured EvoMemoryMiddleware instance.
    """
    memory_backend = FilesystemBackend(
        root_dir=memory_dir,
        virtual_mode=True,
    )
    return EvoMemoryMiddleware(
        backend=memory_backend,
        memory_path="/MEMORY.md",
        extraction_model=extraction_model,
        trigger=trigger,
    )
