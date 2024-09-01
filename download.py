from huggingface_hub import snapshot_download

snapshot_download(repo_id="liuhaotian/LLaVA-Pretrain", local_dir="autodl-tmp/datasets", local_dir_use_symlinks=False)