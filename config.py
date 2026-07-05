"""
Iran Analyzer
Configuration File
"""

from pathlib import Path

# ==========================
# Project Paths
# ==========================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

OUTPUT_DIR = BASE_DIR / "output"

LOG_DIR = BASE_DIR / "logs"

DATABASE_DIR = BASE_DIR / "database"

DATABASE_FILE = DATABASE_DIR / "market.db"

# ایجاد پوشه‌ها در صورت نبودن
OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
DATABASE_DIR.mkdir(exist_ok=True)

# ==========================
# Data Settings
# ==========================

DEFAULT_DAYS = 300

TIMEFRAME = "D"

# ==========================
# Indicator Settings
# ==========================

RSI_PERIOD = 14

EMA_FAST = 20
EMA_SLOW = 50

MACD_FAST = 12
MACD_SLOW = 26
MACD_SIGNAL = 9

ADX_PERIOD = 14

ICHIMOKU_TENKAN = 9
ICHIMOKU_KIJUN = 26
ICHIMOKU_SPAN_B = 52

# ==========================
# Analysis Settings
# ==========================

MIN_DATA_LENGTH = 120

# ==========================
# Score Weights
# ==========================

WEIGHT_ICHIMOKU = 30
WEIGHT_MACD = 20
WEIGHT_RSI = 15
WEIGHT_ADX = 15
WEIGHT_VOLUME = 10
WEIGHT_TREND = 10

# ==========================
# Report
# ==========================

EXPORT_EXCEL = True

EXPORT_HTML = False

SHOW_CHART = True

# ==========================
# Version
# ==========================

APP_NAME = "Iran Analyzer"

VERSION = "1.0.0"