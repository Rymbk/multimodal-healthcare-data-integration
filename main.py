"""
main.py — End-to-end pipeline runner
Run: python main.py
"""
from utils.config_loader import load_config
from utils.logger import logger


def run_pipeline():
    config = load_config()
    logger.info(f"Starting: {config['project']['name']} v{config['project']['version']}")

    # Each step will be filled in as modules are built
    steps = [
        ("1. Data Ingestion",        None),
        ("2. Preprocessing",         None),
        ("3. Anomaly Detection",     None),
        ("4. Record Linkage",        None),
        ("5. OCR",                   None),
        ("6. Image Analysis",        None),
        ("7. Integration Layer",     None),
    ]

    for name, fn in steps:
        logger.info(f"Step {name}")
        if fn:
            fn(config)
        else:
            logger.warning(f"  → Not yet implemented")

    logger.success("Pipeline complete.")


if __name__ == "__main__":
    run_pipeline()
