"""RuntimeCoder data pipeline - fixture generation, SFT, FIM, and file boundary datasets."""

from runtime_coder.data_pipeline.fixtures import generate_all_fixtures
from runtime_coder.data_pipeline.sft_example_builder import build_sft_examples

__all__ = ["generate_all_fixtures", "build_sft_examples"]
