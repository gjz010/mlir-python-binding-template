<div align="center">

# 🐍 MLIR Python ➕ Nix ❄️

**A batteries-included, bleeding-edge template for MLIR Python development.**

[![built with nix](https://img.shields.io/static/v1?logo=nixos&logoColor=white&label=&message=Built%20with%20Nix&color=41439a)](https://builtwithnix.org)
[![Built with Devenv](https://img.shields.io/badge/Built%20with-Devenv-_330882.svg?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDgwIiBoZWlnaHQ9IjQ4MCIgdmlld0JveD0iMCAwIDQ4MCA0ODAiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0yNDUuMzA4IDMxVjExMC42OTJIMzI1VjMxTDI0NS4zMDggMzFaIiBmaWxsPSIjNDI1QzgyIi8+CjxwYXRoIGQ9Ik0zMzQuOTYyIDEyMC42NTRWMjAwLjM0Nkg0MTQuNjU0VjEyMC42NTRIMzM0Ljk2MloiIGZpbGw9IiM0MjVDODIiLz4KPHBhdGggZD0iTTI0NS4zMDggMTIwLjY1NFYyMDAuMzQ2SDMyNVYxMjAuNjU0SDI0NS4zMDhaIiBmaWxsPSIjNDI1QzgyIi8+CjxwYXRoIGQ9Ik0zMzQuOTYyIDIxMC4zMDhWMjkwSDQxNC42NTRWMjEwLjMwOEgzMzQuOTYyWiIgZmlsbD0iIzQyNUM4MiIvPgo8cGF0aCBkPSJNMjQ1LjMwOCAyMTAuMzA4VjI5MEgzMjVWMjEwLjMwOEgyNDUuMzA4WiIgZmlsbD0iIzEwMTAxMCIvPgo8cGF0aCBkPSJNMTU1LjY1NCAyMTAuMzA4VjI5MEgyMzUuMzQ2VjIxMC4zMDhIMTU1LjY1NFoiIGZpbGw9IiMxMDEwMTAiLz4KPHBhdGggZD0iTTY2IDIxMC4zMDhWMjkwSDE0NS42OTJWMjEwLjMwOEg2NloiIGZpbGw9IiMxMDEwMTAiLz4KPHBhdGggZD0iTTE1NS42NTQgMTIwLjY1NFYyMDAuMzQ2SDIzNS4zNDZWMTIwLjY1NEgxNTUuNjU0WiIgZmlsbD0iIzEwMTAxMCIvPgo8cGF0aCBkPSJNMTA0LjI1IDQxNkgxMDAuMTI1TDkzLjUgNDA2LjgxMkM5MS44NzUgNDA4LjI3MSA5MC4xNDU4IDQwOS42NDYgODguMzEyNSA0MTAuOTM4Qzg2LjUyMDggNDEyLjE4OCA4NC42MjUgNDEzLjI5MiA4Mi42MjUgNDE0LjI1QzgwLjYyNSA0MTUuMTY3IDc4LjU2MjUgNDE1Ljg5NiA3Ni40Mzc1IDQxNi40MzhDNzQuMzU0MiA0MTYuOTc5IDcyLjIyOTIgNDE3LjI1IDcwLjA2MjUgNDE3LjI1QzY1LjM1NDIgNDE3LjI1IDYwLjkxNjcgNDE2LjM3NSA1Ni43NSA0MTQuNjI1QzUyLjYyNSA0MTIuODMzIDQ5IDQxMC4zNzUgNDUuODc1IDQwNy4yNUM0Mi43OTE3IDQwNC4wODMgNDAuMzU0MiA0MDAuMzU0IDM4LjU2MjUgMzk2LjA2MkMzNi43NzA4IDM5MS43MjkgMzUuODc1IDM4Ny4wMjEgMzUuODc1IDM4MS45MzhDMzUuODc1IDM3Ni44OTYgMzYuNzcwOCAzNzIuMjA4IDM4LjU2MjUgMzY3Ljg3NUM0MC4zNTQyIDM2My41NDIgNDIuNzkxNyAzNTkuNzkyIDQ1Ljg3NSAzNTYuNjI1QzQ5IDM1My40NTggNTIuNjI1IDM1MC45NzkgNTYuNzUgMzQ5LjE4OEM2MC45MTY3IDM0Ny4zOTYgNjUuMzU0MiAzNDYuNSA3MC4wNjI1IDM0Ni41QzcxLjU2MjUgMzQ2LjUgNzMuMTA0MiAzNDYuNjI1IDc0LjY4NzUgMzQ2Ljg3NUM3Ni4zMTI1IDM0Ny4xMjUgNzcuODc1IDM0Ny41NDIgNzkuMzc1IDM0OC4xMjVDODAuOTE2NyAzNDguNjY3IDgyLjM1NDIgMzQ5LjM5NiA4My42ODc1IDM1MC4zMTJDODUuMDIwOCAzNTEuMjI5IDg2LjE0NTggMzUyLjM1NCA4Ny4wNjI1IDM1My42ODhWMzIyLjQzOEgxMDQuMjVWNDE2Wk04Ny4wNjI1IDM4MS45MzhDODcuMDYyNSAzNzkuNjA0IDg2LjYwNDIgMzc3LjM1NCA4NS42ODc1IDM3NS4xODhDODQuODEyNSAzNzIuOTc5IDgzLjYwNDIgMzcxLjA0MiA4Mi4wNjI1IDM2OS4zNzVDODAuNTIwOCAzNjcuNjY3IDc4LjcwODMgMzY2LjMxMiA3Ni42MjUgMzY1LjMxMkM3NC41ODMzIDM2NC4yNzEgNzIuMzk1OCAzNjMuNzUgNzAuMDYyNSAzNjMuNzVDNjcuNzI5MiAzNjMuNzUgNjUuNTIwOCAzNjQuMTY3IDYzLjQzNzUgMzY1QzYxLjM5NTggMzY1LjgzMyA1OS42MDQyIDM2Ny4wNDIgNTguMDYyNSAzNjguNjI1QzU2LjU2MjUgMzcwLjE2NyA1NS4zNzUgMzcyLjA2MiA1NC41IDM3NC4zMTJDNTMuNjI1IDM3Ni41NjIgNTMuMTg3NSAzNzkuMTA0IDUzLjE4NzUgMzgxLjkzOEM1My4xODc1IDM4NC4zOTYgNTMuNjI1IDM4Ni43MjkgNTQuNSAzODguOTM4QzU1LjM3NSAzOTEuMTQ2IDU2LjU2MjUgMzkzLjA4MyA1OC4wNjI1IDM5NC43NUM1OS42MDQyIDM5Ni40MTcgNjEuMzk1OCAzOTcuNzI5IDYzLjQzNzUgMzk4LjY4OEM2NS41MjA4IDM5OS42NDYgNjcuNzI5MiA0MDAuMTI1IDcwLjA2MjUgNDAwLjEyNUM3Mi4zOTU4IDQwMC4xMjUgNzQuNTgzMyAzOTkuNjI1IDc2LjYyNSAzOTguNjI1Qzc4LjcwODMgMzk3LjU4MyA4MC41MjA4IDM5Ni4yMjkgODIuMDYyNSAzOTQuNTYyQzgzLjYwNDIgMzkyLjg1NCA4NC44MTI1IDM5MC45MTcgODUuNjg3NSAzODguNzVDODYuNjA0MiAzODYuNTQyIDg3LjA2MjUgMzg0LjI3MSA4Ny4wNjI1IDM4MS45MzhaIiBmaWxsPSIjMTAxMDEwIi8+CjxwYXRoIGQ9Ik0xNDMuOTM4IDM5OS42MjVDMTQ0LjYwNCAzOTkuODMzIDE0NS4yNzEgMzk5Ljk3OSAxNDUuOTM4IDQwMC4wNjJDMTQ2LjYwNCA0MDAuMTA0IDE0Ny4yNzEgNDAwLjEyNSAxNDcuOTM4IDQwMC4xMjVDMTQ5LjYwNCA0MDAuMTI1IDE1MS4yMDggMzk5Ljg5NiAxNTIuNzUgMzk5LjQzOEMxNTQuMjkyIDM5OC45NzkgMTU1LjcyOSAzOTguMzMzIDE1Ny4wNjIgMzk3LjVDMTU4LjQzOCAzOTYuNjI1IDE1OS42NDYgMzk1LjU4MyAxNjAuNjg4IDM5NC4zNzVDMTYxLjc3MSAzOTMuMTI1IDE2Mi42NDYgMzkxLjc1IDE2My4zMTIgMzkwLjI1TDE3NS44MTIgNDAyLjgxMkMxNzQuMjI5IDQwNS4wNjIgMTcyLjM5NiA0MDcuMDgzIDE3MC4zMTIgNDA4Ljg3NUMxNjguMjcxIDQxMC42NjcgMTY2LjA0MiA0MTIuMTg4IDE2My42MjUgNDEzLjQzOEMxNjEuMjUgNDE0LjY4OCAxNTguNzI5IDQxNS42MjUgMTU2LjA2MiA0MTYuMjVDMTUzLjQzOCA0MTYuOTE3IDE1MC43MjkgNDE3LjI1IDE0Ny45MzggNDE3LjI1QzE0My4yMjkgNDE3LjI1IDEzOC43OTIgNDE2LjM3NSAxMzQuNjI1IDQxNC42MjVDMTMwLjUgNDEyLjg3NSAxMjYuODc1IDQxMC40MzggMTIzLjc1IDQwNy4zMTJDMTIwLjY2NyA0MDQuMTg4IDExOC4yMjkgNDAwLjQ3OSAxMTYuNDM4IDM5Ni4xODhDMTE0LjY0NiAzOTEuODU0IDExMy43NSAzODcuMTA0IDExMy43NSAzODEuOTM4QzExMy43NSAzNzYuNjQ2IDExNC42NDYgMzcxLjgxMiAxMTYuNDM4IDM2Ny40MzhDMTE4LjIyOSAzNjMuMDYyIDEyMC42NjcgMzU5LjMzMyAxMjMuNzUgMzU2LjI1QzEyNi44NzUgMzUzLjE2NyAxMzAuNSAzNTAuNzcxIDEzNC42MjUgMzQ5LjA2MkMxMzguNzkyIDM0Ny4zNTQgMTQzLjIyOSAzNDYuNSAxNDcuOTM4IDM0Ni41QzE1MC43MjkgMzQ2LjUgMTUzLjQ1OCAzNDYuODMzIDE1Ni4xMjUgMzQ3LjVDMTU4Ljc5MiAzNDguMTY3IDE2MS4zMTIgMzQ5LjEyNSAxNjMuNjg4IDM1MC4zNzVDMTY2LjEwNCAzNTEuNjI1IDE2OC4zNTQgMzUzLjE2NyAxNzAuNDM4IDM1NUMxNzIuNTIxIDM1Ni43OTIgMTc0LjM1NCAzNTguODEyIDE3NS45MzggMzYxLjA2MkwxNDMuOTM4IDM5OS42MjVaTTE1Mi42ODggMzY0LjQzOEMxNTEuODk2IDM2NC4xNDYgMTUxLjEwNCAzNjMuOTU4IDE1MC4zMTIgMzYzLjg3NUMxNDkuNTYyIDM2My43OTIgMTQ4Ljc3MSAzNjMuNzUgMTQ3LjkzOCAzNjMuNzVDMTQ1LjYwNCAzNjMuNzUgMTQzLjM5NiAzNjQuMTg4IDE0MS4zMTIgMzY1LjA2MkMxMzkuMjcxIDM2NS44OTYgMTM3LjQ3OSAzNjcuMTA0IDEzNS45MzggMzY4LjY4OEMxMzQuNDM4IDM3MC4yNzEgMTMzLjI1IDM3Mi4xODggMTMyLjM3NSAzNzQuNDM4QzEzMS41IDM3Ni42NDYgMTMxLjA2MiAzNzkuMTQ2IDEzMS4wNjIgMzgxLjkzOEMxMzEuMDYyIDM4Mi41NjIgMTMxLjA4MyAzODMuMjcxIDEzMS4xMjUgMzg0LjA2MkMxMzEuMjA4IDM4NC44NTQgMTMxLjMxMiAzODUuNjY3IDEzMS40MzggMzg2LjVDMTMxLjYwNCAzODcuMjkyIDEzMS43OTIgMzg4LjA2MiAxMzIgMzg4LjgxMkMxMzIuMjA4IDM4OS41NjIgMTMyLjQ3OSAzOTAuMjI5IDEzMi44MTIgMzkwLjgxMkwxNTIuNjg4IDM2NC40MzhaIiBmaWxsPSIjMTAxMDEwIi8+CjxwYXRoIGQ9Ik0yMDIuNjg4IDQxNkwxNzcuMTg4IDM0OS4wNjJIMTk2LjYyNUwyMTEuMjUgMzkwLjgxMkwyMjUuODEyIDM0OS4wNjJIMjQ1LjMxMkwyMTkuODEyIDQxNkgyMDIuNjg4WiIgZmlsbD0iIzEwMTAxMCIvPgo8cGF0aCBkPSJNMjc2LjQzOCAzOTkuNjI1QzI3Ny4xMDQgMzk5LjgzMyAyNzcuNzcxIDM5OS45NzkgMjc4LjQzOCA0MDAuMDYyQzI3OS4xMDQgNDAwLjEwNCAyNzkuNzcxIDQwMC4xMjUgMjgwLjQzOCA0MDAuMTI1QzI4Mi4xMDQgNDAwLjEyNSAyODMuNzA4IDM5OS44OTYgMjg1LjI1IDM5OS40MzhDMjg2Ljc5MiAzOTguOTc5IDI4OC4yMjkgMzk4LjMzMyAyODkuNTYyIDM5Ny41QzI5MC45MzggMzk2LjYyNSAyOTIuMTQ2IDM5NS41ODMgMjkzLjE4OCAzOTQuMzc1QzI5NC4yNzEgMzkzLjEyNSAyOTUuMTQ2IDM5MS43NSAyOTUuODEyIDM5MC4yNUwzMDguMzEyIDQwMi44MTJDMzA2LjcyOSA0MDUuMDYyIDMwNC44OTYgNDA3LjA4MyAzMDIuODEyIDQwOC44NzVDMzAwLjc3MSA0MTAuNjY3IDI5OC41NDIgNDEyLjE4OCAyOTYuMTI1IDQxMy40MzhDMjkzLjc1IDQxNC42ODggMjkxLjIyOSA0MTUuNjI1IDI4OC41NjIgNDE2LjI1QzI4NS45MzggNDE2LjkxNyAyODMuMjI5IDQxNy4yNSAyODAuNDM4IDQxNy4yNUMyNzUuNzI5IDQxNy4yNSAyNzEuMjkyIDQxNi4zNzUgMjY3LjEyNSA0MTQuNjI1QzI2MyA0MTIuODc1IDI1OS4zNzUgNDEwLjQzOCAyNTYuMjUgNDA3LjMxMkMyNTMuMTY3IDQwNC4xODggMjUwLjcyOSA0MDAuNDc5IDI0OC45MzggMzk2LjE4OEMyNDcuMTQ2IDM5MS44NTQgMjQ2LjI1IDM4Ny4xMDQgMjQ2LjI1IDM4MS45MzhDMjQ2LjI1IDM3Ni42NDYgMjQ3LjE0NiAzNzEuODEyIDI0OC45MzggMzY3LjQzOEMyNTAuNzI5IDM2My4wNjIgMjUzLjE2NyAzNTkuMzMzIDI1Ni4yNSAzNTYuMjVDMjU5LjM3NSAzNTMuMTY3IDI2MyAzNTAuNzcxIDI2Ny4xMjUgMzQ5LjA2MkMyNzEuMjkyIDM0Ny4zNTQgMjc1LjcyOSAzNDYuNSAyODAuNDM4IDM0Ni41QzI4My4yMjkgMzQ2LjUgMjg1Ljk1OCAzNDYuODMzIDI4OC42MjUgMzQ3LjVDMjkxLjI5MiAzNDguMTY3IDI5My44MTIgMzQ5LjEyNSAyOTYuMTg4IDM1MC4zNzVDMjk4LjYwNCAzNTEuNjI1IDMwMC44NTQgMzUzLjE2NyAzMDIuOTM4IDM1NUMzMDUuMDIxIDM1Ni43OTIgMzA2Ljg1NCAzNTguODEyIDMwOC40MzggMzYxLjA2MkwyNzYuNDM4IDM5OS42MjVaTTI4NS4xODggMzY0LjQzOEMyODQuMzk2IDM2NC4xNDYgMjgzLjYwNCAzNjMuOTU4IDI4Mi44MTIgMzYzLjg3NUMyODIuMDYyIDM2My43OTIgMjgxLjI3MSAzNjMuNzUgMjgwLjQzOCAzNjMuNzVDMjc4LjEwNCAzNjMuNzUgMjc1Ljg5NiAzNjQuMTg4IDI3My44MTIgMzY1LjA2MkMyNzEuNzcxIDM2NS44OTYgMjY5Ljk3OSAzNjcuMTA0IDI2OC40MzggMzY4LjY4OEMyNjYuOTM4IDM3MC4yNzEgMjY1Ljc1IDM3Mi4xODggMjY0Ljg3NSAzNzQuNDM4QzI2NCAzNzYuNjQ2IDI2My41NjIgMzc5LjE0NiAyNjMuNTYyIDM4MS45MzhDMjYzLjU2MiAzODIuNTYyIDI2My41ODMgMzgzLjI3MSAyNjMuNjI1IDM4NC4wNjJDMjYzLjcwOCAzODQuODU0IDI2My44MTIgMzg1LjY2NyAyNjMuOTM4IDM4Ni41QzI2NC4xMDQgMzg3LjI5MiAyNjQuMjkyIDM4OC4wNjIgMjY0LjUgMzg4LjgxMkMyNjQuNzA4IDM4OS41NjIgMjY0Ljk3OSAzOTAuMjI5IDI2NS4zMTIgMzkwLjgxMkwyODUuMTg4IDM2NC40MzhaIiBmaWxsPSIjMTAxMDEwIi8+CjxwYXRoIGQ9Ik0zMzQuMTI1IDQxNkgzMTcuMDYyVjM0OS4wNjJIMzIxLjE4OEwzMjYuODEyIDM1NS41NjJDMzI5LjU2MiAzNTMuMDYyIDMzMi42NjcgMzUxLjE0NiAzMzYuMTI1IDM0OS44MTJDMzM5LjYyNSAzNDguNDM4IDM0My4yNzEgMzQ3Ljc1IDM0Ny4wNjIgMzQ3Ljc1QzM1MS4xNDYgMzQ3Ljc1IDM1NSAzNDguNTQyIDM1OC42MjUgMzUwLjEyNUMzNjIuMjUgMzUxLjY2NyAzNjUuNDE3IDM1My44MTIgMzY4LjEyNSAzNTYuNTYyQzM3MC44MzMgMzU5LjI3MSAzNzIuOTU4IDM2Mi40NTggMzc0LjUgMzY2LjEyNUMzNzYuMDgzIDM2OS43NSAzNzYuODc1IDM3My42MjUgMzc2Ljg3NSAzNzcuNzVWNDE2SDM1OS44MTJWMzc3Ljc1QzM1OS44MTIgMzc2IDM1OS40NzkgMzc0LjM1NCAzNTguODEyIDM3Mi44MTJDMzU4LjE0NiAzNzEuMjI5IDM1Ny4yMjkgMzY5Ljg1NCAzNTYuMDYyIDM2OC42ODhDMzU0Ljg5NiAzNjcuNTIxIDM1My41NDIgMzY2LjYwNCAzNTIgMzY1LjkzOEMzNTAuNDU4IDM2NS4yNzEgMzQ4LjgxMiAzNjQuOTM4IDM0Ny4wNjIgMzY0LjkzOEMzNDUuMjcxIDM2NC45MzggMzQzLjU4MyAzNjUuMjcxIDM0MiAzNjUuOTM4QzM0MC40MTcgMzY2LjYwNCAzMzkuMDQyIDM2Ny41MjEgMzM3Ljg3NSAzNjguNjg4QzMzNi43MDggMzY5Ljg1NCAzMzUuNzkyIDM3MS4yMjkgMzM1LjEyNSAzNzIuODEyQzMzNC40NTggMzc0LjM1NCAzMzQuMTI1IDM3NiAzMzQuMTI1IDM3Ny43NVY0MTZaIiBmaWxsPSIjMTAxMDEwIi8+CjxwYXRoIGQ9Ik00MDUuMzEyIDQxNkwzNzkuODEyIDM0OS4wNjJIMzk5LjI1TDQxMy44NzUgMzkwLjgxMkw0MjguNDM4IDM0OS4wNjJINDQ3LjkzOEw0MjIuNDM4IDQxNkg0MDUuMzEyWiIgZmlsbD0iIzEwMTAxMCIvPgo8L3N2Zz4K)](https://devenv.sh/)
[![Python Version](https://img.shields.io/badge/Python-3.12+-blue.svg?logo=python)](https://www.python.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://pre-commit.com/)

</div>

> [!WARNING]
> This `README.md` is generated by Gemini 2.5 Pro Preview 06-05.

---

This template uses the power of [Nix](https://nixos.org/) and [Devenv](https://devenv.sh/) to build [MLIR](https://mlir.llvm.org/) from source and seamlessly inject its Python bindings into a modern, fast development environment.

## 🌟 Features

-   🧊 **Fully Reproducible Environment**: Powered by [Nix Flakes](https://nixos.wiki/wiki/Flakes), the exact versions of all system-level dependencies (like LLVM, compilers, and libraries) are pinned for absolute consistency.

-   ⚙️ **Custom MLIR Build**: The Nix Flake automatically compiles a specific version of LLVM/MLIR with Python bindings enabled. No manual `cmake` or `make` required!
:python:
-   🐍 **Seamless Python Integration**: The compiled `mlir` Python bindings are automatically available in your virtual environment. Just `import mlir` and go!

-   ⚡️ **Blazing-fast Python Tooling**: Uses [`uv`](https://github.com/astral-sh/uv) for rapid dependency management and venv creation, all managed via `pyproject.toml`.

-   ✅ **Automated Code Quality**: Comes with pre-configured [pre-commit](https://pre-commit.com/) hooks via `devenv` for formatters (`black`, `nixfmt-rfc-style`) and linters (`mypy`, `flake8`).

-   🐳 **Dev Container Ready**: Get a one-click, fully configured development environment in VS Code, powered by `devenv`.

-   🌐 **Cross-Platform (Work in Progress)**: The environment is defined for multiple systems (`x86_64-linux`, `aarch64-darwin`, etc.), but has not yet been fully tested across all architectures. Cross-compilation is not yet configured.

## 🚀 Getting Started

### Prerequisites

You need [Nix installed with Flakes enabled](https://nixos.org/download.html). If you haven't enabled flakes yet, add this to your Nix config (`/etc/nix/nix.conf` or `~/.config/nix/nix.conf`):

```
experimental-features = nix-command flakes
```

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd <your-repo-name>
```

### 2. Enter the Magic Shell

```sh
direnv allow
```

or if you want to enter the devenv manually:

```sh
nix develop ./nix --impure
```

> [!NOTE]
> The first time you run this, Nix will download and build all dependencies, specifically building a MLIR compiler with Python3 binding support.
> **This will take a while!** ☕ Subsequent runs will be instantaneous thanks to the Nix cache.

This command activates your new shell, where all tools, libraries, and Python packages are ready to use.

## ✅ Verification & Usage

Once inside the devenv shell:

#### 1. Run the Example Script

The `hello-mlir/hello_mlir.py` script confirms that the bindings work.

```sh
python -m hello-mlir.hello_mlir
```

#### 2. Check the Linters and Hooks

The environment comes with pre-commit hooks configured in `.pre-commit-config.yaml` and managed by `devenv`. They will run automatically when you `git commit`. You can also run them manually:

```sh
# Run mypy to check types (it should find the mlir stubs!)
mypy hello-mlir/hello_mlir.py
# Success: no issues found in 1 source file

# Run all hooks on all files
pre-commit run --all-files
```

## 🐳 VS Code & Dev Containers

For the ultimate one-click setup, this project is configured for [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers).

### How to Use

1.  **Prerequisites**:
    -   [Docker Desktop](https://www.docker.com/products/docker-desktop/) or another container runtime.
    -   [Visual Studio Code](https://code.visualstudio.com/).
    -   The [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code.

2.  **Launch**:
    -   Open the project folder in VS Code.
    -   A notification will appear in the bottom-right corner: "Reopen in Container". Click it.
    -   Alternatively, open the command palette (`Ctrl/Cmd + Shift + P`) and select `Dev Containers: Reopen in Container`.

VS Code will now build the container and start a terminal with the devenv already active. The recommended `mkhl.direnv` extension will be installed automatically for a seamless experience.



## 🛠️ How It Works


1.  **The Brain (`nix/flake.nix`)**: This is the central control hub. It uses Nix Flakes to define all dependencies, including a custom-built MLIR.

2.  **The Custom Build**: We take the standard `mlir` package from `nixpkgs` and override its build process to:
    -   Enable Python bindings with `-DMLIR_ENABLE_BINDINGS_PYTHON=ON`.
    -   Link it against the correct Python interpreter.
    -   Ensure `pybind11` is available during the build.

3.  **The Magic Shell (`devenv.shells.default`)**: [Devenv](https://devenv.sh/) wraps everything into a perfect development shell. It installs our custom MLIR package and sets up the Python environment.

4.  **The Python Bridge (`nix/python.nix`)**:
    -   Devenv and `uv` work together to create a local virtual environment (`.devenv/state/venv`).
    -   The `PYTHONPATH` is surgically modified to include the path to the Nix-built `mlir` python packages.
    -   `LD_LIBRARY_PATH` is set so the Python bindings can find their C++ shared library dependencies at runtime.
