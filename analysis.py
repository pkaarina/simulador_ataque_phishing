import csv
from collections import Counter
from datetime import datetime

def analisar_dados():
    tentativas = 0
    ips = []
    ultimos = []

    try:
        with open("captured_data.csv", mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                tentativas += 1
                ips.append(row[2])
                ultimos.append(row[3])
        print(f"\nRelatório de Simulação de Phishing")
        print(f"------------------------------------")
        print(f"Total de tentativas: {tentativas}")
        print(f"IPs únicos: {len(set(ips))}")
        print(f"Última tentativa: {ultimos[-1] if ultimos else "N/A"}")

        ip_count = Counter(ips)
        print("\nIPs mais frequentes:")
        for ip, count in ip_count.most_common(5):
            print(f" - {ip}: {count} tentativa(s)")
        
    except FileNotFoundError:
        print(f"Arquivo 'captured_data.csv' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar dados: {e}")

if __name__ == "__main__":
    analisar_dados()