import logging
import json

from cli.inference import run_tts, parse_args


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    args = parse_args()
    if args.text.endswith(".json"):
        with open(args.text, "r", encoding="utf-8") as f:
            args.text = json.load(f)["content"]

    if isinstance(args.text, list):
        for _, text in enumerate(args.text):
            args.text = text
            run_tts(args)
    else:
        run_tts(args)
