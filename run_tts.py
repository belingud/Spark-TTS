import logging
import json
import torch

import sys
sys.path.append(".")

from cli.inference import run_tts, parse_args


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
