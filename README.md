# Version Check Pre-commit Hooks

Pre-commit hooks to check that Python versions in configurations are consistent

## Hooks

### `python_version_runtime_txt_match_pipfile_lock`

This hook ensures that the Python version specified in `Pipfile.lock` matches the one in `runtime.txt`.

## How to Use

1. Install `pre-commit`:
   ```
   pip install pre-commit
   ```

2. Add to your `.pre-commit-config.yaml`:
   ```yaml
   -   repo: https://github.com/RamVasuthevan/version-check-pre-commit-hooks
       rev: v0.1.0  # Adjust for the version you want
       hooks:
       -   id: python_version_runtime_txt_match_pipfile_lock
   ```

3. Set up the git hook scripts:
   ```
   pre-commit install
   ```

Every commit will now run the `python_version_runtime_txt_match_pipfile_lock` hook to ensure consistency between `Pipfile.lock` and `runtime.txt`.

## License

[MIT](./LICENSE)