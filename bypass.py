import subprocess, os, sys, time, ctypes, json, shutil

print("PUBG Bypass v2.0 для MEmu Play запущен...")

# ============================================
# 1. ПОИСК MEmu Play
# ============================================
paths = [
    r"C:\Program Files\Microvirt\MEmu\MEmu.exe",
    r"D:\Program Files\Microvirt\MEmu\MEmu.exe",
    r"C:\Program Files (x86)\Microvirt\MEmu\MEmu.exe",
    r"D:\Program Files (x86)\Microvirt\MEmu\MEmu.exe"
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

memu_dir = os.path.dirname(memu)
print(f"Найден: {memu_dir}")

# ============================================
# 2. ПОЛНАЯ МАСКИРОВКА УСТРОЙСТВА
# ============================================
print("[1/6] Маскирую устройство...")

os.system('reg add "HKCU\\Software\\Microvirt\\MEmu" /v DeviceModel /t REG_SZ /d "SM-G975F" /f')
os.system('reg add "HKCU\\Software\\Microvirt\\MEmu" /v DeviceBrand /t REG_SZ /d "samsung" /f')
os.system('reg add "HKCU\\Software\\Microvirt\\MEmu" /v DeviceManufacturer /t REG_SZ /d "samsung" /f')
os.system('reg add "HKCU\\Software\\Microvirt\\MEmu" /v DeviceName /t REG_SZ /d "SM-G975F" /f')
os.system('reg add "HKCU\\Software\\Microvirt\\MEmu" /v Hardware /t REG_SZ /d "SM-G975F" /f')
os.system('reg add "HKCU\\Software\\Microvirt\\MEmu" /v IMEI /t REG_SZ /d "353625100000001" /f')
os.system('reg add "HKCU\\Software\\Microvirt\\MEmu" /v MAC /t REG_SZ /d "02:00:00:00:00:01" /f')
os.system('reg add "HKCU\\Software\\Microvirt\\MEmu" /v AndroidID /t REG_SZ /d "9774d56d682e549c" /f')

# ============================================
# 3. ОТКЛЮЧЕНИЕ АНТИ-ЧИТА
# ============================================
print("[2/6] Отключаю анти-чит...")

anti_cheat_files = [
    "libtersafe.so",
    "libgamehelper.so",
    "libshell.so",
    "libMEmu.so",
    "libncurses.so",
    "libcms.so",
    "libshell-super.so",
    "libshell-super.uc.so",
    "libshella-3.8.0.4.so",
    "libshella-3.8.0.4.uc.so"
]

for file in anti_cheat_files:
    for root, dirs, files in os.walk(memu_dir):
        for f in files:
            if f == file:
                path = os.path.join(root, f)
                try:
                    os.rename(path, path + ".bak")
                    print(f"  Отключен: {path}")
                except:
                    pass

# ============================================
# 4. УДАЛЕНИЕ СЛЕДОВ
# ============================================
print("[3/6] Удаляю следы эмулятора...")

log_dirs = [
    os.path.join(memu_dir, "logs"),
    os.path.join(memu_dir, "log"),
    os.path.join(memu_dir, "cache"),
    os.path.join(memu_dir, "tmp")
]

for log_dir in log_dirs:
    if os.path.exists(log_dir):
        shutil.rmtree(log_dir, ignore_errors=True)
        print(f"  Удалено: {log_dir}")

# ============================================
# 5. МАСКИРОВКА РЕЕСТРА
# ============================================
print("[4/6] Маскирую реестр...")

os.system('reg add "HKLM\\SOFTWARE\\Microvirt" /v Emulator /t REG_SZ /d "0" /f')
os.system('reg add "HKCU\\Software\\Microvirt" /v Emulator /t REG_SZ /d "0" /f')
os.system('reg add "HKLM\\SOFTWARE\\Microvirt\\MEmu" /v IsEmulator /t REG_SZ /d "0" /f')
os.system('reg add "HKLM\\SOFTWARE\\Microvirt\\MEmu" /v Model /t REG_SZ /d "SM-G975F" /f')
os.system('reg add "HKLM\\SOFTWARE\\Microvirt\\MEmu" /v Manufacturer /t REG_SZ /d "samsung" /f')
os.system('reg add "HKLM\\SOFTWARE\\Microvirt\\MEmu" /v Brand /t REG_SZ /d "samsung" /f')

# ============================================
# 6. МАСКИРОВКА ФАЙЛОВ
# ============================================
print("[5/6] Маскирую файлы...")

emulator_files = [
    "MEmu.exe",
    "MEmuHeadless.exe",
    "MEmuConsole.exe"
]

for file in emulator_files:
    path = os.path.join(memu_dir, file)
    if os.path.exists(path):
        new_name = path.replace("MEmu", "Samsung")
        try:
            os.rename(path, new_name)
            print(f"  Маскирован: {file} -> {os.path.basename(new_name)}")
        except:
            pass

# ============================================
# 7. ЗАПУСК
# ============================================
print("[6/6] Запускаю MEmu Play с маскировкой...")

os.system(f'start "" "{memu}" -no-sandbox -disable-gpu')
time.sleep(10)

print("\n" + "="*50)
print("ГОТОВО! Обход активирован!")
print("="*50)
print("\nВАЖНО:")
print("1. Запустите PUBG Mobile")
print("2. Если баннер появится - перезапустите")
print("3. Играйте без обнаружения")
print("\n" + "="*50)
input("Нажмите Enter для выхода...")
