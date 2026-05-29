import os
import time
import requests
from web3 import Web3
from dotenv import load_dotenv

# Загружаем настройки из файла .env
load_dotenv()

# Инициализируем подключение к RPC-узлу сети Mantle
MANTLE_RPC_URL = os.getenv("MANTLE_RPC_URL", "https://rpc.mantle.xyz")
w3 = Web3(Web3.HTTPProvider(MANTLE_RPC_URL))

# Настройки для отправки уведомлений
DISCORD_WEBHOOK_URL = os.getenv("ALERT_WEBHOOK_URL")

# Настройки для функции активной защиты (Circuit Breaker)
BOT_PRIVATE_KEY = os.getenv("BOT_PRIVATE_KEY", "0x0000000000000000000000000000000000000000000000000000000000000000")
CONTRACT_TO_PROTECT = os.getenv("CONTRACT_TO_PROTECT", "0x0000000000000000000000000000000000000000")

# Получаем адрес кошелька бота из его приватного ключа
if BOT_PRIVATE_KEY != "0x0000000000000000000000000000000000000000000000000000000000000000":
    BOT_ADDRESS = w3.eth.account.from_key(BOT_PRIVATE_KEY).address
else:
    BOT_ADDRESS = "0x0000000000000000000000000000000000000000"

# Минимальный ABI контрактной функции паузы для интеграции с блокчейном
PAUSE_ABI = '[{"inputs":[],"name":"emergencyPause","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

def send_alert(message):
    """Отправка мгновенных алертов в Discord/Telegram команды разработчиков"""
    print(f"[ALERT] {message}")
    if DISCORD_WEBHOOK_URL:
        try:
            requests.post(DISCORD_WEBHOOK_URL, json={"content": message})
        except Exception as e:
            print(f"Ошибка отправки вебхука: {e}")

def trigger_circuit_breaker():
    """ФУНКЦИЯ CIRCUIT BREAKER: Экстренная автоматическая заморозка смарт-контракта"""
    if BOT_PRIVATE_KEY == "0x0000000000000000000000000000000000000000000000000000000000000000":
        send_alert("⚠️ [Mantle Sentinel] АНОМАЛИЯ КРИТИЧЕСКАЯ! Режим имитации: Сигнал автоматической защиты сформирован, но приватный ключ не задан.")
        return

    send_alert("🚨 [Mantle Sentinel] ОБНАРУЖЕНА КРИТИЧЕСКАЯ УГРОЗА! Активирую автоматический прерыватель (Circuit Breaker)...")
    
    try:
        contract = w3.eth.contract(address=w3.to_checksum_address(CONTRACT_TO_PROTECT), abi=PAUSE_ABI)
        
        # Шаг 1: Сборка транзакции экстренной паузы
        tx = contract.functions.emergencyPause().build_transaction({
            'from': BOT_ADDRESS,
            'nonce': w3.eth.get_transaction_count(BOT_ADDRESS),
            'gas': 2000000,
            'gasPrice': w3.eth.gas_price
        })

        # Шаг 2: Криптографическая подпись транзакции ключом ИИ-агента
        signed_tx = w3.eth.account.sign_transaction(tx, BOT_PRIVATE_KEY)
        
        # Шаг 3: Отправка защитной транзакции в пул сети Mantle
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        send_alert(f"🛡️ [Mantle Sentinel] Защитная транзакция отправлена в Mantle! Tx Hash: {tx_hash.hex()}")
        
        # Ожидание подтверждения блока сетью
        w3.eth.wait_for_transaction_receipt(tx_hash)
        send_alert("🔒 [Mantle Sentinel] СМАРТ-КОНТРАКТ УСПЕШНО ЗАМОРОЖЕН. Атака заблокирована, средства пользователей в безопасности.")
        
    except Exception as e:
        send_alert(f"❌ Ошибка при активации Circuit Breaker: {e}")

def analyze_block(block_number):
    """Анализ метрик свежего блока Mantle на наличие аномалий"""
    try:
        block = w3.eth.get_block(block_number, full_transactions=True)
        tx_count = len(block['transactions'])
        gas_used = block['gasUsed']
        
        print(f"[Мониторинг] Блок #{block_number} | Транзакций: {tx_count} | Использовано Газа: {gas_used}")
        
        # Имитация ИИ-анализа оттока средств и аномального потребления газа
        # Если обнаруживается сильное статистическое отклонение (например, спам-атака или эксплойт):
        if tx_count > 500 or gas_used > 25000000: 
            send_alert(f"⚠️ [Mantle Sentinel] Внимание! Зафиксирован аномальный всплеск активности в блоке #{block_number}!")
            
            # Если уровень угрозы оценивается ИИ как критический взлом — включаем защиту:
            if tx_count > 800:
                trigger_circuit_breaker()
                
    except Exception as e:
        print(f"Ошибка при анализе блока #{block_number}: {e}")

def main():
    print("🛡️ Инициализация автономного ИИ-агента Mantle Sentinel...")
    if not w3.is_connected():
        print("❌ Не удалось подключиться к RPC сети Mantle. Проверьте настройки.")
        return
    
    print(f"✅ Успешное подключение к Mantle RPC. Защита активна для адреса: {CONTRACT_TO_PROTECT}")
    
    # Запуск бесконечного цикла отслеживания новых блоков
    latest_block = w3.eth.block_number
    while True:
        current_block = w3.eth.block_number
        if current_block > latest_block:
            for b in range(latest_block + 1, current_block + 1):
                analyze_block(b)
            latest_block = current_block
        time.sleep(1) # Опрос сети каждую секунду

if __name__ == "__main__":
    main()
  
