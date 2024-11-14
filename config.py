from decouple import config

APN: str = config("APN", default='nbiot', cast=str)
BLYNK_TOKEN: str = config("BLYNK_TOKEN", cast=str)
BROKER_ADDRESS: str = config("BROKER_ADDRESS", default='blynk.cloud', cast=str)
DEVICE_NAME: str = config("DEVICE_NAME", cast=str)
DEVICE_SECRET: str = config("DEVICE_SECRET", cast=str)


# Hardware configuration
LED_PIN = 25  # onboard led
LED_PIN_MAIN = 2  # external led
PWR_EN = 14  # power control pin for SIM7020
UART_PORT = 0
UART_BAUDRATE = 115200

# Initialize device and setup pins
LED_ONBOARD = Pin(LED_PIN, Pin.OUT)
LED_MAIN = Pin(LED_PIN_MAIN, Pin.OUT)
PWR_KEY = Pin(PWR_EN, Pin.OUT)

# Instantiate SIM7020 and Blynk classes
SIM_7020 = SIM7020(port=UART_PORT, baudrate=UART_BAUDRATE)
BLYNK = BlynkIntegration(port=UART_PORT, apn=APN, blynk_token=BLYNK_TOKEN)