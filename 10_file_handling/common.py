from pathlib import Path

# A "scratch" folder next to the scripts, no matter where you run them from
SCRATCH = Path(__file__).resolve().parent / "scratch"
SCRATCH.mkdir(exist_ok=True)