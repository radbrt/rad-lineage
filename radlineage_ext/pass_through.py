"""Passthrough shim for RadLineage extension."""
import sys

import structlog
from meltano.edk.logging import pass_through_logging_config
from radlineage_ext.extension import RadLineage


def pass_through_cli() -> None:
    """Pass through CLI entry point."""
    pass_through_logging_config()
    ext = RadLineage()
    ext.pass_through_invoker(
        structlog.getLogger("radlineage_invoker"),
        *sys.argv[1:] if len(sys.argv) > 1 else []
    )
