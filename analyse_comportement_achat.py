import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. CHARGEMENT DES DONNÉES ---
file_path = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\Camp_Market_final.csv'

# --- CRÉATION DU DOSSIER DE SORTIE ---
output_dir = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\graph_comportement'
os.makedirs(output_dir, exist_ok=True)

try:
    df = pd.read_csv(file_path)
    print(f"Fichier '{file_path}' chargé avec succès.\n")
    print(f"Dossier de sortie '{output_dir}' prêt.\n")

    # --- 2. PRÉPARATION DES DONNÉES ---
    print("Préparation des données pour l'analyse...")
    
    # Filtrer les données pour une analyse pertinente :
    # - On enlève les revenus nuls/manquants et les dépenses moyennes nulles.
    # - On filtre les revenus extrêmes (> 200k€) pour une meilleure lisibilité du graphique.
    df_analysis = df[(df['Revenu'] > 0) & (df['Revenu'] < 200000) & (df['Depense_Moy_Par_Achat'] > 0)].copy()

    # Définir un ordre logique pour les niveaux d'éducation pour une légende claire
    ordre_education = ['Basic', '2n Cycle', 'Graduation', 'Master', 'PhD']
    df_analysis['Niveau_Education'] = pd.Categorical(df_analysis['Niveau_Education'], categories=ordre_education, ordered=True)

    # --- 3. CRÉATION DU GRAPHIQUE (NUAGE DE POINTS) ---
    print("\nGénération du graphique de la relation entre revenu, dépense moyenne et éducation...")
    
    # Utiliser lmplot de Seaborn pour créer un nuage de points avec des lignes de régression par catégorie d'éducation
    g = sns.lmplot(
        data=df_analysis,
        x='Revenu',
        y='Depense_Moy_Par_Achat',
        hue='Niveau_Education',
        hue_order=ordre_education,
        height=10,
        aspect=1.5,
        scatter_kws={'alpha':0.6} # Rendre les points légèrement transparents
    )

    # Ajouter des titres et des étiquettes
    g.fig.suptitle('Relation entre Revenu, Dépense Moyenne par Achat et Niveau d\'Éducation', fontsize=20, y=1.03)
    g.set_axis_labels('Revenu Annuel (€)', 'Dépense Moyenne par Achat (€)', fontsize=14)
    g.legend.set_title('Niveau d\'Éducation')

    # --- 4. SAUVEGARDE DU GRAPHIQUE ---
    output_path = os.path.join(output_dir, 'relation_revenu_depense_education.png')
    plt.savefig(output_path, dpi=300)
    print(f"\nGraphique sauvegardé avec succès dans : {output_path}")

except FileNotFoundError:
    print(f"ERREUR : Le fichier '{file_path}' est introuvable. Assurez-vous qu'il existe bien.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")