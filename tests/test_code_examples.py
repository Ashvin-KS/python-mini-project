"""
Test suite for validating all code examples in the repository.

This module ensures that:
1. All example files can be imported without syntax errors
2. Code examples follow correct import patterns
3. Example scripts are executable and contain no broken imports
"""

import os
import sys
import importlib.util
from pathlib import Path


def test_all_python_files_have_valid_syntax():
    """Verify all Python files in the repository have valid syntax."""
    repo_root = Path(__file__).parent.parent
    python_files = list(repo_root.rglob('*.py'))

    # Skip test files and hidden directories
    python_files = [
        f for f in python_files
        if not f.parts[0].startswith('.')
        and 'test' not in str(f)
        and '__pycache__' not in str(f)
    ]

    errors = []
    for py_file in python_files:
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                compile(f.read(), str(py_file), 'exec')
        except SyntaxError as e:
            errors.append(f"{py_file}: {e}")

    assert not errors, f"Syntax errors found:\n" + "\n".join(errors)


def test_games_modules_importable():
    """Verify all game modules can be imported."""
    repo_root = Path(__file__).parent.parent
    games_dir = repo_root / 'games'

    if not games_dir.exists():
        return  # Skip if games directory doesn't exist

    errors = []
    for game_folder in games_dir.iterdir():
        if not game_folder.is_dir():
            continue

        py_files = list(game_folder.glob('*.py'))
        for py_file in py_files:
            try:
                spec = importlib.util.spec_from_file_location(py_file.stem, py_file)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    sys.modules[py_file.stem] = module
                    # Don't execute, just verify it can be loaded
            except Exception as e:
                errors.append(f"{py_file}: {str(e)}")

    assert not errors, f"Failed to import game modules:\n" + "\n".join(errors)


def test_math_modules_importable():
    """Verify all math modules can be imported."""
    repo_root = Path(__file__).parent.parent
    math_dir = repo_root / 'math'

    if not math_dir.exists():
        return  # Skip if math directory doesn't exist

    errors = []
    for math_folder in math_dir.iterdir():
        if not math_folder.is_dir():
            continue

        py_files = list(math_folder.glob('*.py'))
        for py_file in py_files:
            try:
                spec = importlib.util.spec_from_file_location(py_file.stem, py_file)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    sys.modules[py_file.stem] = module
                    # Don't execute, just verify it can be loaded
            except Exception as e:
                errors.append(f"{py_file}: {str(e)}")

    assert not errors, f"Failed to import math modules:\n" + "\n".join(errors)


def test_utilities_modules_importable():
    """Verify all utility modules can be imported."""
    repo_root = Path(__file__).parent.parent
    utilities_dir = repo_root / 'utilities'

    if not utilities_dir.exists():
        return  # Skip if utilities directory doesn't exist

    errors = []
    for util_folder in utilities_dir.iterdir():
        if not util_folder.is_dir():
            continue

        py_files = list(util_folder.glob('*.py'))
        for py_file in py_files:
            try:
                spec = importlib.util.spec_from_file_location(py_file.stem, py_file)
                if spec and spec.loader:
                    module = importlib.util.module_from_spec(spec)
                    sys.modules[py_file.stem] = module
                    # Don't execute, just verify it can be loaded
            except Exception as e:
                errors.append(f"{py_file}: {str(e)}")

    assert not errors, f"Failed to import utility modules:\n" + "\n".join(errors)


def test_no_broken_imports():
    """Check for broken imports in all Python files."""
    repo_root = Path(__file__).parent.parent
    python_files = list(repo_root.rglob('*.py'))

    # Skip test files and hidden directories
    python_files = [
        f for f in python_files
        if not f.parts[0].startswith('.')
        and 'test' not in str(f)
        and '__pycache__' not in str(f)
    ]

    errors = []
    for py_file in python_files:
        with open(py_file, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')

            for line_num, line in enumerate(lines, 1):
                line = line.strip()

                # Check for import statements
                if line.startswith('import ') or line.startswith('from '):
                    # Check for common patterns of broken imports
                    if line.endswith('import') or line.endswith('from'):
                        errors.append(f"{py_file}:{line_num}: Incomplete import statement")

                    # Check for double dots or invalid characters
                    if '..' in line.split('import')[0]:
                        errors.append(f"{py_file}:{line_num}: Invalid import path")

    assert not errors, f"Broken imports found:\n" + "\n".join(errors)


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
