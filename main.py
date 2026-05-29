import time
from web3 import Web3

# Подключаемся к публичной ноде сети Mantle
MANTLE_RPC_URL = "https://rpc.mantle.xyz"
web3 = Web3(Web3.HTTPProvider(MANTLE_RPC_URL))

# Настройки порогов для аномалий (наш базовый ИИ-профиль)
MAX_BLOCK_TIME = 5.0  # секунды (норма для Mantle около 2-3 сек)
MAX_GAS_PRICE_GWEI = 50.0

def send_alert(message):
    # В финальной версии здесь будет интеграция с API Telegram/Discord
    print(f"[🚨 ВНИМАНИЕ: АНОМАЛИЯ] {message}")

def monitor_network():
    print("🛡️ Mantle Sentinel запущен. Мониторинг сети начался...\n")
    
    if not web3.is_connected():
        print("Ошибка: Не удалось подключиться к RPC Mantle.")
        return

    latest_block = web3.eth.get_block('latest')
    last_block_time = latest_block.timestamp

    while True:
        try:
            current_block = web3.eth.get_block('latest')
            
            if current_block.number > latest_block.number:
                # 1. Проверка задержки секвенсора (Latency)
                time_diff = current_block.timestamp - last_block_time
                if time_diff > MAX_BLOCK_TIME:
                    send_alert(f"Задержка блока {time_diff} сек. (Блок: {current_block.number}) - Возможен сбой ноды!")
                
                # 2. Проверка скачков газа (Gas Spike / Congestion)
                gas_price_wei = web3.eth.gas_price
                gas_price_gwei = web3.from_wei(gas_price_wei, 'gwei')
                
                if gas_price_gwei > MAX_GAS_PRICE_GWEI:
                    send_alert(f"Резкий скачок комиссий: {gas_price_gwei:.2f} Gwei. Возможна спам-атака.")

                print(f"✅ Блок {current_block.number} проверен. Задержка: {time_diff}с, Газ: {gas_price_gwei:.2f} Gwei")
                
                latest_block = current_block
                last_block_time = current_block.timestamp

            time.sleep(2) # Пауза перед следующим запросом

        except Exception as e:
            print(f"Ошибка при сканировании: {e}")
            time.sleep(5)

if __name__ == "__main__":
    monitor_network()
