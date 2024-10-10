FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*
# rm -rf /var/lib/apt/lists/*
# Dockerイメージのサイズを削減するためのベストプラクティス
# 古いパッケージリストを削除することで、潜在的な脆弱性情報も削除できる


# Pythonの依存関係をインストール
RUN pip install --no-cache-dir pandas reportlab Pillow
# --no-cache-dir
# パッケージのインストール時にキャッシュを使用しない
# インストール後にキャッシュを保存しない
# このオプションの主な目的は：
# Dockerイメージのサイズを小さく保つ
# ビルド時間を短縮する（特に、CIシステムなどで毎回クリーンビルドを行う場合）
# 常に最新のパッケージをインストールすることを保証する

# ワーキングディレクトリを設定
WORKDIR /scripts
