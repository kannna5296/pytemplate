# Poetryからuvへの移行手順書

このドキュメントは、本プロジェクトをPoetryからuvへ移行するための詳細な手順を記載しています。

## 目次

1. [前提知識](#前提知識)
2. [移行前の確認事項](#移行前の確認事項)
3. [手順](#手順)
4. [移行後の確認](#移行後の確認)
5. [コマンド対応表](#コマンド対応表)
6. [トラブルシューティング](#トラブルシューティング)

---

## 前提知識

### uvとは

- Rustで書かれた高速なPythonパッケージマネージャー
- Poetryやpipenvの代替として使用可能
- PEP 621形式の`pyproject.toml`を標準として使用
- Poetry形式の`pyproject.toml`も解釈可能だが、PEP 621形式への移行を推奨

### 移行のメリット

- **高速性**: Poetryと比べて依存関係の解決とインストールが大幅に高速
- **標準準拠**: PEP 621形式を使用することで、より標準的なプロジェクト構造
- **シンプルさ**: 軽量で高速な実装

---

## 移行前の確認事項

以下の点を確認してください：

- [ ] 現在の`poetry.lock`が最新であること（`poetry lock`を実行済み）
- [ ] すべての依存関係が正しく動作していること
- [ ] 開発環境で移行をテストできること
- [ ] チームメンバーへの通知（uv移行について）

---

## 手順

### ステップ1: `pyproject.toml`をPEP 621形式に変換

現在の`pyproject.toml`を、Poetry形式からPEP 621形式に変換します。

#### 1.1 基本情報の変換

**変更前（Poetry形式）:**
```toml
[tool.poetry]
name = "pytemplate"
version = "0.1.0"
description = "S3 data aggregation and Google Slides automation"
authors = ["Your Name <your.email@example.com>"]
readme = "README.md"
packages = [{include = "src"}]
```

**変更後（PEP 621形式）:**
```toml
[project]
name = "pytemplate"
version = "0.1.0"
description = "S3 data aggregation and Google Slides automation"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
readme = "README.md"
requires-python = ">=3.11"
```

**変更点:**
- `[tool.poetry]` → `[project]`
- `authors`を配列形式に変更
- `packages`を削除（uvは自動検出するため不要）
- `requires-python`を追加

#### 1.2 依存関係の変換

**変更前（Poetry形式）:**
```toml
[tool.poetry.dependencies]
python = "^3.11"
boto3 = "^1.34.0"
pandas = "^2.1.0"
google-api-python-client = "^2.108.0"
google-auth = "^2.23.0"
google-auth-oauthlib = "^1.1.0"
google-auth-httplib2 = "^0.1.1"
python-dotenv = "^1.0.0"
beautifulsoup4 = "^4.12.3"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
ruff = "^0.1.0"
mypy = "^1.10.0"
boto3-stubs = {extras = ["essential"], version = "^1.34.0"}
```

**変更後（PEP 621形式）:**
```toml
[project]
# ... 基本情報 ...
dependencies = [
    "boto3>=1.34.0",
    "pandas>=2.1.0",
    "google-api-python-client>=2.108.0",
    "google-auth>=2.23.0",
    "google-auth-oauthlib>=1.1.0",
    "google-auth-httplib2>=0.1.1",
    "python-dotenv>=1.0.0",
    "beautifulsoup4>=4.12.3",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "ruff>=0.1.0",
    "mypy>=1.10.0",
    "boto3-stubs[essential]>=1.34.0",
]
```

**変更点:**
- `python = "^3.11"`を`requires-python = ">=3.11"`に移動（基本情報セクション）
- `[tool.poetry.dependencies]` → `[project].dependencies`
- `[tool.poetry.group.dev.dependencies]` → `[project.optional-dependencies].dev`
- バージョン指定を`^`から`>=`に変更（PEP 508準拠）
- `boto3-stubs`の`extras`表記を`[essential]`形式に変更

#### 1.3 スクリプトの変換

**変更前:**
```toml
[tool.poetry.scripts]
main = "src.project.main:main"
```

**変更後:**
```toml
[project.scripts]
main = "src.project.main:main"
```

#### 1.4 その他の設定

以下の設定は変更不要（そのまま残す）:
- `[tool.ruff]` - Ruffの設定
- `[tool.pytest.ini_options]` - pytestの設定
- `[tool.mypy]` - mypyの設定

#### 1.5 完全な変換後の例

```toml
# プロジェクト基本情報
[project]
name = "pytemplate"
version = "0.1.0"
description = "S3 data aggregation and Google Slides automation"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "boto3>=1.34.0",
    "pandas>=2.1.0",
    "google-api-python-client>=2.108.0",
    "google-auth>=2.23.0",
    "google-auth-oauthlib>=1.1.0",
    "google-auth-httplib2>=0.1.1",
    "python-dotenv>=1.0.0",
    "beautifulsoup4>=4.12.3",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "ruff>=0.1.0",
    "mypy>=1.10.0",
    "boto3-stubs[essential]>=1.34.0",
]

[project.scripts]
main = "src.project.main:main"

# ruff設定（black、flake8、isortの統合）
[tool.ruff]
target-version = "py311"
line-length = 88
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4", # flake8-comprehensions
    "UP", # pyupgrade
]
ignore = [
    "E501",  # line too long, handled by black
    "B008",  # do not perform function calls in argument defaults
    "C901",  # too complex
]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"

[tool.ruff.lint.isort]
known-first-party = ["src"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]

[tool.mypy]
python_version = "3.11"
check_untyped_defs = true
ignore_missing_imports = true
strict = true
explicit_package_bases = true
```

---

### ステップ2: `Dockerfile`の更新

`.devcontainer/Dockerfile`を更新して、Poetryをuvに置き換えます。

**変更前:**
```dockerfile
# poetryインストール（バージョン固定）
RUN pip install --no-cache-dir poetry==2.1.3
```

**変更後:**
```dockerfile
# uvインストール
RUN pip install --no-cache-dir uv
```

**完全なDockerfile:**
```dockerfile
FROM python:3.11.13-slim

# システムパッケージの更新とgit、makeインストール procps...プロセス監視
RUN apt-get update && apt-get install -y \
    git procps make\
    && rm -rf /var/lib/apt/lists/*
    #↑キャッシュを削除してイメージサイズを削減

# uvインストール
RUN pip install --no-cache-dir uv

WORKDIR /workspace
```

---

### ステップ3: `devcontainer.json`の更新

`.devcontainer/devcontainer.json`の`postCreateCommand`を更新します。

**変更前:**
```json
"postCreateCommand": "git config --global --add safe.directory /workspace && poetry install && poetry run python -c 'print(\"✅ Poetry environment ready!\")'"
```

**変更後:**
```json
"postCreateCommand": "git config --global --add safe.directory /workspace && uv sync --all-extras && uv run python -c 'print(\"✅ UV environment ready!\")'"
```

**説明:**
- `poetry install` → `uv sync --all-extras`
  - `uv sync`は依存関係をインストール（Poetryの`install`に相当）
  - `--all-extras`オプションで`[project.optional-dependencies]`の`dev`も含めてインストール
- `poetry run` → `uv run`
- 仮想環境は自動で`.venv`に作成される（`POETRY_VIRTUALENVS_IN_PROJECT=true`相当）

---

### ステップ4: `Makefile`の更新

`Makefile`内の`poetry run`を`uv run`に変更します。

**変更前:**
```makefile
# devcontainer上で実行する前提
format:
	poetry run ruff format .

lint:
	poetry run ruff check --fix .
```

**変更後:**
```makefile
# devcontainer上で実行する前提
format:
	uv run ruff format .

lint:
	uv run ruff check --fix .
```

---

### ステップ5: `poetry.lock`の削除

`poetry.lock`ファイルを削除してください。uvは`uv.lock`を自動生成します。

```bash
rm poetry.lock
```

**注意:** `uv.lock`は`.gitignore`に含めず、バージョン管理にコミットしてください（Poetryと同様）。

---

### ステップ6: `.gitignore`の確認（オプション）

`.gitignore`に以下の行があることを確認してください（通常は既にあるはず）:

```
.venv/
__pycache__/
*.pyc
```

uvは`.venv`ディレクトリを使用します。

---

## 移行後の確認

### 1. devcontainerの再構築

VS Codeでdevcontainerを再構築してください：
- `Ctrl+Shift+P` (または `Cmd+Shift+P`) → "Dev Containers: Rebuild Container"

### 2. 依存関係のインストール確認

```bash
# 依存関係のインストール（開発依存も含む）
uv sync --all-extras

# インストールされたパッケージの確認
uv pip list
```

### 3. 仮想環境の確認

```bash
# 仮想環境の場所を確認
which python
# 出力: /workspace/.venv/bin/python

# Pythonのバージョン確認
uv run python --version
```

### 4. パッケージの実行確認

```bash
# プロジェクトのスクリプト実行
uv run main

# または直接Pythonモジュール実行
uv run python -m src.project.main
```

### 5. 開発ツールの実行確認

```bash
# フォーマット
make format
# または
uv run ruff format .

# リンター
make lint
# または
uv run ruff check --fix .

# テスト
uv run pytest
```

### 6. 型チェック

```bash
uv run mypy .
```

---

## コマンド対応表

| Poetry | uv | 説明 |
|--------|-----|------|
| `poetry install` | `uv sync` | 依存関係をインストール |
| `poetry install --with dev` | `uv sync --all-extras` | 開発依存も含めてインストール |
| `poetry add <package>` | `uv add <package>` | パッケージを追加 |
| `poetry add --group dev <package>` | `uv add --dev <package>` | 開発依存として追加 |
| `poetry remove <package>` | `uv remove <package>` | パッケージを削除 |
| `poetry run <command>` | `uv run <command>` | 仮想環境内でコマンド実行 |
| `poetry update` | `uv sync --upgrade` | 依存関係を更新 |
| `poetry lock` | `uv lock` | ロックファイルを生成/更新 |
| `poetry show` | `uv pip list` | インストール済みパッケージ一覧 |
| `poetry shell` | `source .venv/bin/activate` | 仮想環境をアクティベート |
| `poetry export -f requirements.txt` | `uv pip compile pyproject.toml -o requirements.txt` | requirements.txtを出力 |

---

## トラブルシューティング

### 問題1: `uv sync`でエラーが発生する

**症状:** 依存関係の解決に失敗する

**対処法:**
```bash
# 詳細なエラーログを確認
uv sync --all-extras -v

# pyproject.tomlの構文を確認
uv sync --check
```

### 問題2: 仮想環境が作成されない

**症状:** `.venv`ディレクトリが作成されない

**対処法:**
```bash
# 手動で仮想環境を作成
uv venv

# その後依存関係をインストール
uv sync --all-extras
```

### 問題3: VS CodeがPythonインタープリターを認識しない

**症状:** VS Codeが`.venv/bin/python`を見つけられない

**対処法:**
1. `Ctrl+Shift+P` → "Python: Select Interpreter"
2. `/workspace/.venv/bin/python`を選択
3. または`devcontainer.json`の`python.defaultInterpreterPath`が正しく設定されているか確認

### 問題4: `uv run`が動作しない

**症状:** `uv run`コマンドでエラーが発生する

**対処法:**
```bash
# uvが正しくインストールされているか確認
which uv
uv --version

# 仮想環境が正しく作成されているか確認
ls -la .venv/bin/python
```

### 問題5: パッケージがインストールされない

**症状:** `uv sync`後もパッケージが見つからない

**対処法:**
```bash
# ロックファイルを再生成
rm uv.lock
uv lock

# 再度インストール
uv sync --all-extras
```

### 問題6: 開発依存（dev）がインストールされない

**症状:** `uv sync`後、`pytest`などが使えない

**対処法:**
```bash
# --all-extrasオプションを付けて実行
uv sync --all-extras
```

---

## 追加リソース

- [uv公式ドキュメント](https://github.com/astral-sh/uv)
- [PEP 621 - Python project metadata](https://peps.python.org/pep-0621/)
- [uvとPoetryの比較](https://github.com/astral-sh/uv/blob/main/docs/comparison.md)

---

## 移行チェックリスト

移行作業の完了を確認するためのチェックリストです。

- [ ] `pyproject.toml`をPEP 621形式に変換
- [ ] `Dockerfile`でuvをインストールするように変更
- [ ] `devcontainer.json`の`postCreateCommand`を更新
- [ ] `Makefile`のコマンドを`uv run`に変更
- [ ] `poetry.lock`を削除
- [ ] devcontainerを再構築
- [ ] `uv sync --all-extras`が正常に動作する
- [ ] `uv run python --version`でPythonが認識される
- [ ] `make format`が動作する
- [ ] `make lint`が動作する
- [ ] `uv run pytest`が動作する
- [ ] `uv run mypy .`が動作する
- [ ] プロジェクトのメインスクリプトが実行できる

---

**最終更新日:** 2024年（移行実施日を記載してください）

