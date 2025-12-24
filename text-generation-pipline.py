from transformers import pipeline

# パイプラインの作成 タスクとモデルを指定
pipe = pipeline(
    "text-generation",
    model="gpt2",
)

# テキスト生成の実行
result = pipe(
    "The first thing I do when I wake up is",
    max_new_tokens=50,
    temperature=0.7
)
print(result)

