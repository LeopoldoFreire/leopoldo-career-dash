import feedparser
import csv
from datetime import datetime

# RSS Feeds (Exemplos estáveis para vagas remotas)
FEEDS = {
    "RemoteOK": "https://remoteok.com/remote-jobs.rss",
    "WeWorkRemotely": "https://weworkremotely.com/categories/remote-customer-support-jobs.rss"
}

def coletar_vagas():
    vagas = []
    print(f"[{datetime.now()}] Coletando vagas dos feeds RSS...")
    
    for nome, url in FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]: # Pegar as 5 últimas de cada
            vagas.append({
                "cargo": entry.title,
                "fonte": nome,
                "link": entry.link
            })
            
    with open('/home/tellinus/Scripts/Automacao_Carreira/vagas_diarias.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["cargo", "fonte", "link"])
        writer.writeheader()
        writer.writerows(vagas)
    
    print("Sucesso! Lista de vagas atualizada.")

if __name__ == "__main__":
    coletar_vagas()
