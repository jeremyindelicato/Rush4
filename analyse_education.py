import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. CHARGEMENT DES DONNÉES ---
file_path = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\Camp_Market_final.csv'

# --- CRÉATION DU DOSSIER DE SORTIE ---
output_dir = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\graph_education'
os.makedirs(output_dir, exist_ok=True)

try:
    df = pd.read_csv(file_path)
    print(f"Fichier '{file_path}' chargé avec succès.\n")
    print(f"Dossier de sortie '{output_dir}' prêt.\n")

    # --- 2. PRÉPARATION DES DONNÉES D'ÉDUCATION ---
    print("Préparation des données d'éducation...")
    
    # Calculer la proportion d'achats en promotion par rapport au total des achats pour chaque client
    df['Proportion_Promo'] = (df['Achats_Promotions'] / df['Total_Achats'].replace(0, 1)) * 100

    # Définir un ordre logique pour les niveaux d'éducation pour les graphiques
    ordre_education = ['Basic', '2n Cycle', 'Graduation', 'Master', 'PhD']
    df['Niveau_Education'] = pd.Categorical(df['Niveau_Education'], categories=ordre_education, ordered=True)

    # --- 3. ANALYSE : PROMOTION PAR NIVEAU D'ÉDUCATION ---
    # Calculer la proportion moyenne d'achats en promotion pour chaque niveau d'éducation
    promo_par_education = df.groupby('Niveau_Education')['Proportion_Promo'].mean().reset_index()

    print("\nProportion moyenne des achats en promotion par niveau d'éducation :")
    print(promo_par_education)

    # --- 4. CRÉATION DU GRAPHIQUE (PROMOTIONS) ---
    print("\nGénération du graphique des promotions par niveau d'éducation...")
    plt.figure(figsize=(14, 8))
    barplot = sns.barplot(x='Niveau_Education', y='Proportion_Promo', data=promo_par_education, palette='viridis', order=ordre_education)

    for p in barplot.patches:
        barplot.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=12)

    plt.title('Proportion Moyenne des Achats en Promotion par Niveau d\'Éducation', fontsize=18, pad=20)
    plt.ylabel('Proportion moyenne des achats en promotion (%)', fontsize=14)
    plt.xlabel('Niveau d\'Éducation', fontsize=14)
    plt.xticks(rotation=0)
    plt.tight_layout()

    output_promo_path = os.path.join(output_dir, 'proportion_promo_par_education.png')
    plt.savefig(output_promo_path, dpi=300)
    print(f"\nGraphique des promotions sauvegardé avec succès dans : {output_promo_path}")

    # --- 5. ANALYSE DES DÉPENSES PAR PRODUIT ET PAR NIVEAU D'ÉDUCATION ---
    print("\nGénération du graphique des dépenses par produit en fonction du niveau d'éducation...")

    colonnes_produits = {
        'Achat_Vins': 'Vins', 'Achat_Viandes': 'Viandes', 'Achat_Fruits': 'Fruits',
        'Achat_Poissons': 'Poissons', 'Achat_Produits_Sucres': 'Produits Sucrés', 'Achat_Produits_Or': 'Produits Or'
    }

    depenses_par_education = df.groupby('Niveau_Education')[list(colonnes_produits.keys())].sum()
    depenses_par_education.columns = colonnes_produits.values()

    depenses_pourcentage = depenses_par_education.div(depenses_par_education.sum(axis=1), axis=0) * 100

    print("\nRépartition des dépenses par produit et par niveau d'éducation (%):")
    print(depenses_pourcentage)

    # --- 6. CRÉATION DU GRAPHIQUE 100% EMPILÉ (DÉPENSES) ---
    couleurs_perso = ['#2a7886', '#7ad151', '#fde725', '#414487', '#f57f17', '#000000']
    
    ax_produits_edu = depenses_pourcentage.loc[ordre_education].plot(
        kind='bar', 
        stacked=True, 
        figsize=(16, 10), 
        color=couleurs_perso
    )

    plt.title('Répartition des Dépenses par Catégorie de Produit en fonction du Niveau d\'Éducation', fontsize=18, pad=20)
    plt.ylabel('Pourcentage des dépenses totales (%)', fontsize=14)
    plt.xlabel('Niveau d\'Éducation', fontsize=14)
    plt.xticks(rotation=0)
    plt.legend(title='Catégorie de Produit', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout(rect=[0, 0, 0.88, 1])

    output_depenses_path = os.path.join(output_dir, 'repartition_depenses_par_education.png')
    plt.savefig(output_depenses_path, dpi=300)
    print(f"\nGraphique des dépenses par éducation sauvegardé avec succès dans : {output_depenses_path}")

except FileNotFoundError:
    print(f"ERREUR : Le fichier '{file_path}' est introuvable. Assurez-vous qu'il existe bien.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")