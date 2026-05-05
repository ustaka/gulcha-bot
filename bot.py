import json
import logging
import os
from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    CallbackQueryHandler,
    ConversationHandler, filters, ContextTypes
)

# === SOZLAMALAR ===
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set.")
ADMIN_ID = int(os.getenv("ADMIN_ID", "5594795335"))
CARD_NUMBER = os.getenv("CARD_NUMBER", "8600 6821 2328 4780")
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

# === HOLATLAR ===
(
    REG_NAME, REG_PHONE, REG_ADDRESS,
    ORDER_MENU, ORDER_QUANTITY, ORDER_PAYMENT,
    ORDER_CONFIRM,
    BROADCAST_TEXT, MENU_INPUT
) = range(9)

# === MA'LUMOTLAR ===
users = {}
menu = {}
orders = {}
order_counter = [0]
weekly_stats = {"orders": 0, "revenue": 0, "days": {}}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_data(): ...
def load_data(): ...
def is_admin(user_id): ...
def format_order_for_admin(order, user): ...
def format_order_for_user(order): ...

# Handlers: start, show_main_menu
# Registration: reg_name, reg_phone, reg_address
# Ordering: order_start, show_menu_page, menu_callback,
#           quantity_callback, payment_choice, payment_callback, confirm_callback
# Admin: admin_menu, menu_input, photo_menu_input, menu_done,
#        admin_orders, admin_broadcast_start, broadcast_send, admin_report
# Misc: my_info, cancel, main()
