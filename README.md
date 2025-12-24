# Transformers-sample

Hugging Face Transformersライブラリを使ったサンプルコード集です。

## ファイル構成

- `text-generation-pipline.py` - パイプラインを使ったテキスト生成の簡単な実行例
- `text-generation-process.py` - テキスト生成におけるトークン化から生成までの詳細なプロセス確認用
- `prompt-engineering-practice.py` - 感情分析タスクでFew-shotを実践するプロンプトエンジニアリング実践例
- `prompt-engineering-practice_2.py` - お礼メール文生成タスクでFew-shotを実践するプロンプトエンジニアリング実践例


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

# プロンプトエンジニアリング実践（感情分析）
python prompt-engineering-practice.py

# プロンプトエンジニアリング実践（お礼メール文生成）
python prompt-engineering-practice_2.py
```

## プロンプトエンジニアリングについて

### Few-shot学習とは
モデルに少数の例を示すことで、タスクを理解させ精度を向上させる手法です。

**比較パターン:**
- **Zero-shot**: 例なし（指示のみ）
- **Few-shot**: 3〜5個の例
- **Many-shot**: 8個以上の例

**注意点:**
- 例が多すぎると逆効果（コンテキスト長の限界、パターン過学習）
- T5-baseの場合、**3〜5例が最適**

## 必要なパッケージ
- transformers: Hugging Faceの機械学習ライブラリ
- torch: PyTorchバックエンド
- sentencepiece: トークナイザー
- protobuf: モデル設定ファイル用
- tiktoken: 一部のトークナイザー用
