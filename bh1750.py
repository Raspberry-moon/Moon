import smbus2
import time

# I2C 버스 (라즈베리파이 4에서는 bus 번호가 1입니다)
I2C_BUS = 1

# BH1750 주소
BH1750_ADDR = 0x23

# BH1750 모드 설정 (Continuously H-Resolution Mode)
MODE = 0x10

def read_light():
    bus = smbus2.SMBus(I2C_BUS)
    # 명령어 전송
    bus.write_byte(BH1750_ADDR, MODE)
    time.sleep(0.180)  # 데이터가 준비될 때까지 대기 (최대 180ms)
    # 데이터 읽기 (2 바이트)
    data = bus.read_i2c_block_data(BH1750_ADDR, MODE, 2)
    bus.close()
    # 조도 계산
    light_level = (data[0] << 8) | data[1]
    light_level /= 1.2  # 변환 계수 적용
    return light_level

try:
    while True:
        light = read_light()
        print(f"Light Level: {light:.2f} lx")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
