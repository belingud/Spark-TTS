import logging
import json
import torch

import sys
from pathlib import Path
# 获取当前文件的绝对路径
current_file_path = Path(__file__).resolve()
# 获取当前文件所在的目录
current_directory = current_file_path.parent
print(f"当前文件所在的目录：{current_directory}")
sys.path.append(str(current_directory))

from .cli.inference import run_tts, parse_args  # noqa: E402


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    args = parse_args()
    
    # 检查CUDA是否可用，如果不可用则使用CPU
    if not torch.cuda.is_available():
        logging.info("CUDA不可用，将使用CPU进行推理")
        args.device = "cpu"

    if args.text.endswith(".json"):
        with open(args.text, "r", encoding="utf-8") as f:
            args.text = json.load(f)["content"]

    if isinstance(args.text, list):
        for _, text in enumerate(args.text):
            args.text = text
            run_tts(args)
    else:
        run_tts(args)
