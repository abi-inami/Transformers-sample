from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "Qwen/Qwen3-0.6B"

prompt = "The \"Transformers\" library is amazing!"

# 1.前処理
# トークナイザーのロード
tokenizer = AutoTokenizer.from_pretrained(model_id)

# 1-1.トークン化: テキスト → トークン（文字列の配列）
tokens = tokenizer.tokenize(prompt)
print("1-1. After tokenization (tokens):\n", tokens)


# 1-2.トークンID化: トークン → ID（整数の配列）
token_ids = tokenizer.convert_tokens_to_ids(tokens)
print("1-2. After token ID conversion:\n", token_ids)


# 1-3.テンソル化: ID → テンソル
inputs = {
    'input_ids': torch.tensor([token_ids]),
    'attention_mask': torch.tensor([[1] * len(token_ids)])
}
print("1-3. After tensorization:\n", inputs)

# 2.モデル実行: テンソル → テンソル
model = AutoModelForCausalLM.from_pretrained(
    model_id,
)
outputs = model.generate(
    **inputs,
    max_new_tokens=50,
    temperature=0.7,
    do_sample=True
)
print("2. After generation:\n", outputs)


# 3.後処理: テンソル → テキスト
text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("3. After decoding:\n", text)
