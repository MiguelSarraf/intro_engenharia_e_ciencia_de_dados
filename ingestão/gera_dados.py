import psutil
import json
from datetime import datetime, timedelta
import os


def pega_cpu():
    return {
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "cpu_usage_percent_total": psutil.cpu_percent(interval=1),
        "cpu_usage_percent_per_core": psutil.cpu_percent(interval=1, percpu=True),
        "cpu_freq": {
            "current_mhz": psutil.cpu_freq().current if psutil.cpu_freq() else None,
            "min_mhz": psutil.cpu_freq().min if psutil.cpu_freq() else None,
            "max_mhz": psutil.cpu_freq().max if psutil.cpu_freq() else None,
        }
    }


def pega_memoria():
    virtual_mem = psutil.virtual_memory()
    swap = psutil.swap_memory()

    return {
        "virtual_memory": {
            "total": virtual_mem.total,
            "available": virtual_mem.available,
            "used": virtual_mem.used,
            "percent": virtual_mem.percent
        },
        "swap_memory": {
            "total": swap.total,
            "used": swap.used,
            "free": swap.free,
            "percent": swap.percent
        }
    }


def pega_disco():
    partitions = psutil.disk_partitions()
    disk_data = []

    disk_io = psutil.disk_io_counters()

    return {
        "disk_io": {
            "read_bytes": disk_io.read_bytes,
            "write_bytes": disk_io.write_bytes,
            "read_count": disk_io.read_count,
            "write_count": disk_io.write_count
        }
    }


def pega_rede():
    net_io = psutil.net_io_counters()
    return {
        "bytes_sent": net_io.bytes_sent,
        "bytes_recv": net_io.bytes_recv,
        "packets_sent": net_io.packets_sent,
        "packets_recv": net_io.packets_recv
    }


def pega_temperatura():
    temps = {}
    try:
        sensor_temps = psutil.sensors_temperatures()
        for name, entries in sensor_temps.items():
            temps[name] = []
            for entry in entries:
                temps[name].append({
                    "label": entry.label,
                    "current": entry.current,
                    "high": entry.high,
                    "critical": entry.critical
                })
    except Exception:
        temps = "Temperature sensors not supported on this system"

    return temps

def pega_bateria():
    battery = psutil.sensors_battery()

    if battery is None:
        return {
            "present": False,
        }

    return {
        "present": True,
        "percent": battery.percent,
        "plugged_in": battery.power_plugged,
        "secs_left": battery.secsleft,
        "time_left_formatted": (
            str(timedelta(seconds=battery.secsleft))
            if battery.secsleft not in (psutil.POWER_TIME_UNLIMITED, psutil.POWER_TIME_UNKNOWN)
            else None
        )
    }

def coleta_informacoes_sistema():
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d_%H:%M:%S"),
        "cpu": pega_cpu(),
        "memory": pega_memoria(),
        "disk": pega_disco(),
        "network": pega_rede(),
        "temperatures": pega_temperatura(),
        "battery": pega_bateria(),
    }

def salva_json(data, nome="system_info.json"):
    with open(nome, "w") as arquivo:
        json.dump(data, arquivo, indent=4)


informacoes_sistema = coleta_informacoes_sistema()

caminho_arquivo = rf"{os.environ.get('PASTA_INGESTAO')}{informacoes_sistema['timestamp']}.json"
salva_json(informacoes_sistema, nome=caminho_arquivo)

