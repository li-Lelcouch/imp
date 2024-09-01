from huggingface_hub import snapshot_download

snapshot_download(repo_id="google/siglip-so400m-patch14-384", local_dir="checkpoints/base/siglip-so400m-patch14-384", local_dir_use_symlinks=False)