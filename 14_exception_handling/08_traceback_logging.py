import logging
import sys
import traceback

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s", stream=sys.stdout)
log = logging.getLogger("demo")

def parse_age(text):
    return int(text)

def process(text):
    return parse_age(text) + 1

# 1. Read a traceback from the bottom up
try:
    process("abc")
except ValueError as e:
    tb = traceback.format_exc()
    print(tb)
    print("last line  :", tb.strip().splitlines()[-1])
    print("raised in  :", e.__traceback__.tb_next.tb_next.tb_frame.f_code.co_name)

# 2. Logging an error WITH its traceback, then carrying on
try:
    process("abc")
except ValueError:
    log.exception("could not process input")
log.info("program continues")

# 3. Tools for inspecting exceptions
try:
    1 / 0
except ZeroDivisionError:
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(exc_type.__name__, "|", exc_value)
    print("".join(traceback.format_exception_only(exc_type, exc_value)).strip())
    for frame in traceback.extract_tb(exc_tb):
        print(f"  file {frame.filename.split(chr(92))[-1]}, line {frame.lineno}, in {frame.name}")

# 4. Never print and forget: pick a clear strategy
def good_pattern():
    try:
        return process("abc")
    except ValueError as e:
        log.warning("using default because: %s", e)    # log, then recover
        return 0

print(good_pattern())