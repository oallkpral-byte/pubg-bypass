import subprocess, os, sys, time, ctypes, json

print("PUBG Bypass для MEmu Play запущен...")
print("Ищу MEmu Play...")

paths = [
    r"C:\Program Files\Microvirt\MEmu\MEmu.exe",
    r"D:\Program Files\Microvirt\MEmu\MEmu.exe",
    r"C:\Program Files (x86)\Microvirt\MEmu\MEmu.exe"
]

memu = None
for p in paths:
    if os.path.exists(p):
        memu = p
        break

if not memu:
    print("MEmu Play не найден!")
    input("Нажмите Enter...")
    sys.exit()

print(f"Найден: {memu}")

# Маскировка устройства
print("Маскирую устройство...")
os.system('reg add "HKCU\\Software\\Microvirt\\MEmu" /v DeviceModel /t REG_SZ /d "SM-G975F" /f')
os.system('reg add "HKCU\\Software\\Microvirt\\MEmu" /v DeviceBrand /t REG_SZ /d "samsung" /f')
os.system('reg add "HKCU\\Software\\Microvirt\\MEmu" /v DeviceManufacturer /t REG_SZ /d "samsung" /f')

# Отключение анти-чита
print("Отключаю анти-чит...")
files = [
    r"C:\Program Files\Microvirt\MEmu\lib\libtersafe.so",
    r"D:\Program Files\Microvirt\MEmu\lib\libtersafe.so",
    r"C:\Program Files\Microvirt\MEmu\lib\libgamehelper.so",
    r"D:\Program Files\Microvirt\MEmu\lib\libgamehelper.so"
]

for f in files:
    if os.path.exists(f):
        os.rename(f, f + ".bak")
        print(f"Отключен: {f}")

# Скрытие следов эмулятора
print("Скрываю следы эмулятора...")
os.system('reg add "HKLM\\SOFTWARE\\Microvirt" /v Emulator /t REG_SZ /d "0" /f')
os.system('reg add "HKCU\\Software\\Microvirt" /v Emulator /t REG_SZ /d "0" /f')

# Дополнительная маскировка
print("Дополнительная маскировка...")
os.system('reg add "HKCU\\Software\\Microvirt\\MEmu" /v RAM /t REG_SZ /d "4096" /f')
os.system('reg add "HKCU\\Software\\Microvirt\\MEmu" /v CPU /t REG_SZ /d "4" /f')

# Удаление логов
print("Удаляю логи...")
log_paths = [
    r"C:\Program Files\Microvirt\MEmu\logs",
    r"D:\Program Files\Microvirt\MEmu\logs"
]
for lp in log_paths:
    if os.path.exists(lp):
        os.system(f'rmdir /s /q "{lp}"')
        print(f"Логи удалены: {lp}")

print("Готово! Запускаю MEmu Play...")
os.startfile(memu)
print("Играйте!")
input("Нажмите Enter для выхода...")