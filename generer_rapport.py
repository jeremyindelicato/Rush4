import os
import webbrowser
from datetime import datetime

def main():
    """
    Génère un rapport HTML qui rassemble tous les graphiques d'analyse.
    """
    print("Début de la génération du rapport HTML...")

    # --- 1. DÉFINIR LES CHEMINS ET LA STRUCTURE ---
    base_dir = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4'
    report_filename = 'rapport_analyse.html'
    report_filepath = os.path.join(base_dir, report_filename)

    # Dictionnaire des graphiques à inclure, organisés par section
    # La clé est le titre de la section, la valeur est le nom du dossier
    sections = {
        "Synthèse & Optimisation": "graph_optimisation",
        "Analyse du Comportement d'Achat": "graph_comportement",
        "Analyse des Produits": "graph_produits",
        "Analyse des Lieux d'Achat": "graph_lieux",
        "Analyse des Campagnes": "graph_campagnes",
        "Analyse des Plaintes": "graph_plaintes",
        "Analyse par Profil Client": "graph_clients",
        "Analyse par Statut Marital": "graph_statut_marital",
        "Analyse par Composition du Ménage": "graph_enfants",
        "Analyse par Revenu": "graph_revenu",
        "Analyse par Niveau d'Éducation": "graph_education",
        "Analyse par Jour d'Inscription": "graph_jours_campagnes"
    }

    # --- 2. CONSTRUCTION DU CONTENU HTML ---
    html_content = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Rapport d'Analyse Marketing</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                background-color: #f4f4f9;
                margin: 0;
                padding: 20px;
            }
            .container {
                max-width: 1200px;
                margin: auto;
                background: #fff;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
            header {
                text-align: center;
                border-bottom: 2px solid #e0e0e0;
                padding-bottom: 20px;
                margin-bottom: 30px;
            }
            header h1 {
                color: #2c3e50;
                margin-bottom: 5px;
            }
            header p {
                color: #7f8c8d;
                font-size: 1.1em;
            }
            .section {
                margin-bottom: 40px;
                padding-bottom: 20px;
                border-bottom: 1px solid #eee;
            }
            .section h2 {
                color: #34495e;
                border-left: 4px solid #3498db;
                padding-left: 15px;
            }
            .graph-container {
                text-align: center;
                margin-top: 20px;
            }
            .graph-container img {
                max-width: 95%;
                height: auto;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                margin-bottom: 25px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>Rapport d'Analyse Marketing</h1>
                <p>Généré le """ + datetime.now().strftime('%d/%m/%Y à %H:%M:%S') + """</p>
            </header>
    """

    # Boucler sur chaque section pour ajouter les graphiques
    for title, folder in sections.items():
        folder_path = os.path.join(base_dir, folder)
        
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            images = [f for f in os.listdir(folder_path) if f.endswith('.png')]
            if images:
                html_content += f'<div class="section"><h2>{title}</h2>'
                for image in sorted(images):
                    # Utiliser des chemins relatifs pour que le HTML fonctionne n'importe où
                    relative_path = os.path.join(folder, image)
                    html_content += f'<div class="graph-container"><img src="{relative_path}" alt="{image}"></div>'
                html_content += '</div>'

    html_content += """
        </div>
    </body>
    </html>
    """

    # --- 3. ÉCRIRE LE FICHIER ET L'OUVRIR ---
    with open(report_filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\nRapport '{report_filename}' généré avec succès.")
    
    # Ouvrir le rapport dans le navigateur par défaut
    webbrowser.open('file://' + os.path.realpath(report_filepath))

if __name__ == '__main__':
    main()