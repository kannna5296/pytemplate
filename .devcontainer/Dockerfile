FROM python:3.11.13-slim

# システムパッケージの更新とgit、makeインストール procps...プロセス監視
RUN apt-get update && apt-get install -y \
    git procps make\
    && rm -rf /var/lib/apt/lists/*
    #↑キャッシュを削除してイメージサイズを削減

# uvインストール（バージョン固定）
RUN pip install --no-cache-dir uv==0.9.7

WORKDIR /workspace
