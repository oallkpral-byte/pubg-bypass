import subprocess, os, sys, time, ctypes, json, shutil, re

print("PUBG Bypass v3.0 - Агрессивный обход")
print("="*50)

# ============================================
# 1. ПРОВЕРКА ПРАВ АДМИНИСТРАТОРА
# ============================================
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("ОШИБКА: Запустите от имени администратора!")
    input("Нажмите Enter...")
    sys.exit()

# ============================================
# 2. ПОИСК MEmu Play
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
print(f"[+] Найден MEmu: {memu_dir}")

# ============================================
# 3. ПОЛНАЯ МАСКИРОВКА УСТРОЙСТВА
# ============================================
print("[1/7] Маскирую устройство...")

# Основные параметры устройства Samsung Galaxy S10
device_params = {
    "DeviceModel": "SM-G975F",
    "DeviceBrand": "samsung",
    "DeviceManufacturer": "samsung",
    "DeviceName": "SM-G975F",
    "Hardware": "SM-G975F",
    "IMEI": "353625100000001",
    "MAC": "02:00:00:00:00:01",
    "AndroidID": "9774d56d682e549c",
    "Serial": "R58M35A1234",
    "PhoneNumber": "+79161234567",
    "DeviceType": "phone",
    "DeviceBoard": "beyond1",
    "DevicePlatform": "exynos9820",
    "DeviceCpuAbi": "arm64-v8a",
    "DeviceCpuAbi2": "armeabi-v7a",
    "DeviceCpuAbiList": "arm64-v8a,armeabi-v7a,armeabi",
    "DeviceGpu": "Mali-G76",
    "DeviceGpuRenderer": "Mali-G76",
    "DeviceGpuVersion": "OpenGL ES 3.2",
    "DeviceScreenSize": "1080x2280",
    "DeviceScreenDensity": "420",
    "DeviceScreenDensityDpi": "420",
    "DeviceScreenRefreshRate": "60",
    "DeviceBattery": "100",
    "DeviceBatteryStatus": "5",
    "DeviceBatteryLevel": "100",
    "DeviceBatteryTemperature": "25.0",
    "DeviceBatteryVoltage": "4200",
    "DeviceBatteryTechnology": "Li-ion",
    "DeviceBatteryHealth": "2",
    "DeviceBatteryPlugged": "1",
    "DeviceBatteryPresent": "true",
    "DeviceBatteryCapacity": "3400",
    "DeviceBatteryChargeCounter": "3400",
    "DeviceBatteryCurrentNow": "0",
    "DeviceBatteryEnergyCounter": "3400",
    "DeviceBatteryTemp": "25.0",
    "DeviceBatteryVoltage": "4200"
}

for key, value in device_params.items():
    os.system(f'reg add "HKCU\\Software\\Microvirt\\MEmu" /v {key} /t REG_SZ /d "{value}" /f')

print("[+] Устройство замаскировано под Samsung Galaxy S10")

# ============================================
# 4. ОТКЛЮЧЕНИЕ ВСЕХ АНТИ-ЧИТОВ
# ============================================
print("[2/7] Отключаю анти-чит...")

# Основные файлы анти-чита
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
    "libshella-3.8.0.4.uc.so",
    "libshella-3.8.0.5.so",
    "libshella-3.8.0.5.uc.so",
    "libshella-3.8.0.6.so",
    "libshella-3.8.0.6.uc.so",
    "libshella-3.8.0.7.so",
    "libshella-3.8.0.7.uc.so",
    "libshella-3.8.0.8.so",
    "libshella-3.8.0.8.uc.so",
    "libshella-3.8.0.9.so",
    "libshella-3.8.0.9.uc.so",
    "libshella-3.8.0.10.so",
    "libshella-3.8.0.10.uc.so"
]

# Отключаем все файлы анти-чита
for file in anti_cheat_files:
    for root, dirs, files in os.walk(memu_dir):
        for f in files:
            if f == file:
                path = os.path.join(root, f)
                try:
                    # Переименовываем и делаем нечитаемым
                    os.rename(path, path + ".disabled")
                    # Делаем файл системным и скрытым
                    ctypes.windll.kernel32.SetFileAttributesW(path + ".disabled", 0x02 | 0x04)
                    print(f"  [OK] Отключен: {file}")
                except:
                    pass

print("[+] Анти-чит отключен")

# ============================================
# 5. ПОЛНОЕ УДАЛЕНИЕ СЛЕДОВ
# ============================================
print("[3/7] Удаляю следы эмулятора...")

# Удаляем все логи и кэши
log_dirs = [
    os.path.join(memu_dir, "logs"),
    os.path.join(memu_dir, "log"),
    os.path.join(memu_dir, "cache"),
    os.path.join(memu_dir, "tmp"),
    os.path.join(memu_dir, "temp"),
    os.path.join(memu_dir, "crash"),
    os.path.join(memu_dir, "crashpad"),
    os.path.join(memu_dir, "debug"),
    os.path.join(memu_dir, "dump"),
    os.path.join(memu_dir, "dumps"),
    os.path.join(memu_dir, "error"),
    os.path.join(memu_dir, "errors"),
    os.path.join(memu_dir, "exception"),
    os.path.join(memu_dir, "exceptions"),
    os.path.join(memu_dir, "logcat"),
    os.path.join(memu_dir, "logcat.log"),
    os.path.join(memu_dir, "logcat.txt")
]

for log_dir in log_dirs:
    if os.path.exists(log_dir):
        try:
            if os.path.isdir(log_dir):
                shutil.rmtree(log_dir, ignore_errors=True)
            else:
                os.remove(log_dir)
            print(f"  [OK] Удалено: {log_dir}")
        except:
            pass

# Удаляем все файлы с логами
for root, dirs, files in os.walk(memu_dir):
    for f in files:
        if any(keyword in f.lower() for keyword in ["log", "debug", "error", "crash", "dump"]):
            try:
                path = os.path.join(root, f)
                os.remove(path)
                print(f"  [OK] Удален файл: {f}")
            except:
                pass

print("[+] Следы эмулятора удалены")

# ============================================
# 6. ПОЛНАЯ МАСКИРОВКА РЕЕСТРА
# ============================================
print("[4/7] Маскирую реестр...")

# Удаляем все следы эмулятора из реестра
reg_keys = [
    "HKCU\\Software\\Microvirt",
    "HKCU\\Software\\MEmu",
    "HKLM\\SOFTWARE\\Microvirt",
    "HKLM\\SOFTWARE\\MEmu",
    "HKCU\\Software\\Microvirt\\MEmu",
    "HKLM\\SOFTWARE\\Microvirt\\MEmu",
    "HKCU\\Software\\Microvirt\\MEmuPlay",
    "HKLM\\SOFTWARE\\Microvirt\\MEmuPlay"
]

for key in reg_keys:
    os.system(f'reg delete "{key}" /f')

# Создаем новые ключи с маскировкой под Samsung
os.system('reg add "HKCU\\Software\\Samsung" /v DeviceModel /t REG_SZ /d "SM-G975F" /f')
os.system('reg add "HKCU\\Software\\Samsung" /v DeviceBrand /t REG_SZ /d "samsung" /f')
os.system('reg add "HKCU\\Software\\Samsung" /v DeviceManufacturer /t REG_SZ /d "samsung" /f')
os.system('reg add "HKCU\\Software\\Samsung" /v DeviceName /t REG_SZ /d "SM-G975F" /f')
os.system('reg add "HKCU\\Software\\Samsung" /v Hardware /t REG_SZ /d "SM-G975F" /f')
os.system('reg add "HKCU\\Software\\Samsung" /v IMEI /t REG_SZ /d "353625100000001" /f')
os.system('reg add "HKCU\\Software\\Samsung" /v MAC /t REG_SZ /d "02:00:00:00:00:01" /f')
os.system('reg add "HKCU\\Software\\Samsung" /v AndroidID /t REG_SZ /d "9774d56d682e549c" /f')
os.system('reg add "HKCU\\Software\\Samsung" /v Serial /t REG_SZ /d "R58M35A1234" /f')

# Маскируем системный реестр
os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion" /v ProductName /t REG_SZ /d "Windows 10 Pro" /f')
os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion" /v EditionID /t REG_SZ /d "Professional" /f')
os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion" /v BuildLabEx /t REG_SZ /d "19041.1.amd64fre.vb_release.191206-1406" /f')
os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion" /v DisplayVersion /t REG_SZ /d "2004" /f')
os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion" /v CurrentBuild /t REG_SZ /d "19041" /f')
os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion" /v CurrentBuildNumber /t REG_SZ /d "19041" /f')
os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion" /v ReleaseId /t REG_SZ /d "2004" /f')
os.system('reg add "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion" /v UBR /t REG_SZ /d "1" /f')

print("[+] Реестр замаскирован")

# ============================================
# 7. МАСКИРОВКА ФАЙЛОВ И ПРОЦЕССОВ
# ============================================
print("[5/7] Маскирую файлы и процессы...")

# Переименовываем файлы эмулятора
emulator_files = [
    "MEmu.exe",
    "MEmuHeadless.exe",
    "MEmuConsole.exe",
    "MEmuSVC.exe",
    "MEmuManage.exe",
    "MEmuMonitor.exe",
    "MEmuUpdater.exe",
    "MEmuService.exe"
]

for file in emulator_files:
    path = os.path.join(memu_dir, file)
    if os.path.exists(path):
        new_name = path.replace("MEmu", "Samsung")
        try:
            os.rename(path, new_name)
            print(f"  [OK] Маскирован: {file} -> {os.path.basename(new_name)}")
        except:
            pass

# Маскируем папки
folder_names = ["MEmu", "Microvirt"]
for folder in folder_names:
    folder_path = os.path.join(memu_dir, folder)
    if os.path.exists(folder_path):
        try:
            os.rename(folder_path, folder_path.replace(folder, "Samsung"))
            print(f"  [OK] Папка {folder} -> Samsung")
        except:
            pass

print("[+] Файлы и процессы замаскированы")

# ============================================
# 8. ОТКЛЮЧЕНИЕ СЛУЖБ И ДРАЙВЕРОВ
# ============================================
print("[6/7] Отключаю службы и драйверы...")

# Останавливаем службы MEmu
services = [
    "MEmuSVC",
    "MEmuService",
    "MEmuMonitor",
    "MEmuUpdater",
    "Microvirt",
    "MEmu"
]

for service in services:
    os.system(f'sc stop {service} 2>nul')
    os.system(f'sc config {service} start= disabled 2>nul')
    print(f"  [OK] Служба {service} отключена")

# Удаляем драйверы эмулятора
drivers = [
    "MEmuVMM",
    "MEmuVBox",
    "MEmuNet",
    "MEmuAudio",
    "MEmuVideo"
]

for driver in drivers:
    os.system(f'sc stop {driver} 2>nul')
    os.system(f'sc delete {driver} 2>nul')
    print(f"  [OK] Драйвер {driver} удален")

print("[+] Службы и драйверы отключены")

# ============================================
# 9. ЗАПУСК MEmu Play
# ============================================
print("[7/7] Запускаю MEmu Play...")

# Запускаем MEmu без параметров
os.startfile(memu)
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
