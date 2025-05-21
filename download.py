from huggingface_hub import snapshot_download

# 下載整個資料集到當前目錄
local_dir = snapshot_download(
    repo_id="dodofk/ntusldl2024_miniproject_2",  # 資料集名稱
    repo_type="dataset",                        # 指定為資料集
    local_dir="."                               # 當前目錄
)

print(f"Downloaded dataset to: {local_dir}")
