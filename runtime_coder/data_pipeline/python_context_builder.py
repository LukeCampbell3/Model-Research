"""Python context builder for RuntimeCoder training examples.

Builds ContextPacket instances from Python source snippets with proper
paths, symbols, and language="python" metadata.
"""

import hashlib
from typing import Dict, List, Any, Optional


def build_context_packet(
    file_path: str,
    content: str,
    symbols: List[str] = None,
    dependencies: List[str] = None,
    source_type: str = "file",
) -> Dict[str, Any]:
    """Build a ContextPacket dict from Python source.

    Args:
        file_path: Path to the Python source file.
        content: Python source code content.
        symbols: List of symbol names (functions, classes) in scope.
        dependencies: List of dependency module names.
        source_type: Type of context source (file, symbol, snippet).

    Returns:
        ContextPacket dictionary ready for training examples.
    """
    ctx_id = f"ctx_{hashlib.md5(file_path.encode()).hexdigest()[:8]}"
    return {
        "context_id": ctx_id,
        "source_type": source_type,
        "content": content,
        "file_path": file_path,
        "language": "python",
        "symbols": symbols or [],
        "dependencies": dependencies or [],
    }


def build_multi_file_context(
    files: List[Dict[str, str]],
) -> List[Dict[str, Any]]:
    """Build multiple ContextPackets from a list of file dicts.

    Args:
        files: List of dicts with 'path' and 'content' keys,
               optionally 'symbols' and 'dependencies'.

    Returns:
        List of ContextPacket dictionaries.
    """
    packets = []
    for f in files:
        packet = build_context_packet(
            file_path=f["path"],
            content=f["content"],
            symbols=f.get("symbols", []),
            dependencies=f.get("dependencies", []),
        )
        packets.append(packet)
    return packets


def extract_symbols_from_source(source: str) -> List[str]:
    """Extract function and class names from Python source.

    Simple regex-free parser that looks for 'def' and 'class' statements.

    Args:
        source: Python source code string.

    Returns:
        List of symbol names found.
    """
    symbols = []
    for line in source.split("\n"):
        stripped = line.lstrip()
        if stripped.startswith("def "):
            name = stripped[4:].split("(")[0].strip()
            if name:
                symbols.append(name)
        elif stripped.startswith("class "):
            name = stripped[6:].split("(")[0].split(":")[0].strip()
            if name:
                symbols.append(name)
    return symbols


def build_context_with_imports(
    file_path: str,
    content: str,
    import_context: Optional[str] = None,
) -> Dict[str, Any]:
    """Build context packet that includes import resolution info.

    Args:
        file_path: Path to the source file.
        content: Source code content.
        import_context: Optional string of resolved import info.

    Returns:
        ContextPacket with import metadata.
    """
    symbols = extract_symbols_from_source(content)
    deps = _extract_imports(content)

    packet = build_context_packet(
        file_path=file_path,
        content=content,
        symbols=symbols,
        dependencies=deps,
    )

    if import_context:
        packet["metadata"] = {"import_context": import_context}

    return packet


def _extract_imports(source: str) -> List[str]:
    """Extract imported module names from Python source."""
    imports = []
    for line in source.split("\n"):
        stripped = line.strip()
        if stripped.startswith("import "):
            mod = stripped[7:].split(" as ")[0].split(",")[0].strip()
            imports.append(mod)
        elif stripped.startswith("from "):
            mod = stripped[5:].split(" import")[0].strip()
            imports.append(mod)
    return imports
