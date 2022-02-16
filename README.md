# pre-commit-hooks

Some pre-commit hooks for OpenTAI projects.

## Using pre-commit-hooks with pre-commit

Add this to your `.pre-commit-config.yaml`

```
- repo: https://github.com/OpenTAI/pre-commit-hooks
  rev: main  # Use the ref you want to point at
  hooks:
    - id: check-copyright
      args: ["dir_to_check"]  # replace the dir_to_check with your expected directory to check
```

## Hooks available

### say-hello

A template to show how to implement a pre-commit hook

### check-copyright

Check whether the code contains copyright

`includes` - directory to add copyright.
`--excludes` - exclude directory.
`--suffixes` - copyright will be added to files with suffix.
