from huggingface_hub import snapshot_download

snapshot_download(repo_id="microsoft/phi-2", local_dir="autodl-tmp/datasets/base", local_dir_use_symlinks=False)