import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyser_visites_web(file_path=r'c:\Users\Utilisateur\Desktop\Rush 04\Rush4\Camp_Market_final.csv'):
    """
    Analyse le nombre moyen de visites web par mois en fonction du segment de dépensier.

    Args:
        file_path (str): Le chemin vers le fichier CSV à traiter.
    """
    # --- 1. DÉFINIR LES CHEMINS ---
    output_dir = r'c:\Users\Utilisateur\Desktop\Rush 04\Rush4\graph_visites_web'
    os.makedirs(output_dir, exist_ok=True)

    try:
        # --- 2. CHARGEMENT DES DONNÉES ---
        df = pd.read_csv(file_path)
        print(f"Fichier '{os.path.basename(file_path)}' chargé avec succès.")

        # Vérifier la présence des colonnes nécessaires
        if 'Segmentation_Dépensier' not in df.columns or 'Visites_Web_Mois' not in df.columns:
            print("ERREUR : Les colonnes 'Segmentation_Dépensier' ou 'Visites_Web_Mois' sont introuvables.")
            return

        # --- 3. ANALYSE ET AGRÉGATION ---
        print("\nCalcul du nombre moyen de visites web par segment...")
        visites_par_segment = df.groupby('Segmentation_Dépensier')['Visites_Web_Mois'].mean().reset_index()

        # Définir un ordre logique pour l'affichage
        ordre_segment = ['Petits Dépensier', 'Moyens Dépensier', 'Grand Dépensier']
        visites_par_segment['Segmentation_Dépensier'] = pd.Categorical(visites_par_segment['Segmentation_Dépensier'], categories=ordre_segment, ordered=True)
        visites_par_segment = visites_par_segment.sort_values('Segmentation_Dépensier')

        print(visites_par_segment)

        # --- 4. CRÉATION DU GRAPHIQUE ---
        print("\nGénération du graphique...")
        plt.figure(figsize=(12, 8))
        barplot = sns.barplot(x='Segmentation_Dépensier', y='Visites_Web_Mois', data=visites_par_segment, palette='viridis')

        for p in barplot.patches:
            barplot.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                             ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=12)

        plt.title('Nombre Moyen de Visites Web par Mois par Segment de Dépensier', fontsize=18, pad=20)
        plt.ylabel('Nombre Moyen de Visites', fontsize=14)
        plt.xlabel('Segment de Dépensier', fontsize=14)
        plt.xticks(rotation=0)
        plt.tight_layout()

        # --- 5. SAUVEGARDE DU GRAPHIQUE ---
        output_path = os.path.join(output_dir, 'visites_web_par_segment.png')
        plt.savefig(output_path, dpi=300)
        print(f"\nGraphique sauvegardé avec succès dans : {output_path}")

    except FileNotFoundError:
        print(f"ERREUR : Le fichier '{file_path}' est introuvable.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == '__main__':
    analyser_visites_web()