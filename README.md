# Transformers-sample

Hugging Face Transformersライブラリを使ったサンプルコード集です。

## ファイル構成

- `text-generation-pipline.py` - パイプラインを使ったテキスト生成の簡単な実行例
- `text-generation-process.py` - テキスト生成におけるトークン化から生成までの詳細なプロセス確認用


## 環境構築

### 前提条件
- Python 3.11 想定

### 1. 仮想環境の作成と有効化
```bash
python -m venv .venv # pip の場合
# または
uv venv # uv の場合
```

```
source .venv/bin/activate  # Linux/Mac
# または
.venv\Scripts\activate  # Windows
```

### 2. パッケージのインストール
```bash
pip install -r requirements.txt # pip の場合
# または
uv pip install -r requirements.txt # uv の場合
```

### 3. 実行
以下参考に実行してください。
```bash
# パイプラインを使った簡単な実行
python text-generation-pipline.py

# 詳細なプロセスを確認する
python text-generation-process.py
```

## 必要なパッケージ
- transformers: Hugging Faceの機械学習ライブラリ
- torch: PyTorchバックエンド
- sentencepiece: トークナイザー
- protobuf: モデル設定ファイル用
- tiktoken: 一部のトークナイザー用
