import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

# --- 1. CHARGEMENT DES DONNÉES ---
file_path = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\Camp_Market_final.csv'

# --- CRÉATION DU DOSSIER DE SORTIE ---
output_dir = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\graph_revenu'
os.makedirs(output_dir, exist_ok=True)

try:
    df = pd.read_csv(file_path)
    print(f"Fichier '{file_path}' chargé avec succès.\n")
    print(f"Dossier de sortie '{output_dir}' prêt.\n")

    # --- 2. PRÉPARATION DES DONNÉES DE REVENU ---
    print("Préparation des données et création des tranches de revenus...")
    
    # Filtrer les revenus non valides (nuls ou manquants) pour une analyse plus juste
    df_revenu = df[df['Revenu'] > 0].copy()

    # Créer des tranches de revenus pour la segmentation
    bins = [0, 25000, 50000, 75000, 100000, np.inf]
    labels = ['< 25k €', '25k-50k €', '50k-75k €', '75k-100k €', '> 100k €']
    df_revenu['Categorie_Revenu'] = pd.cut(df_revenu['Revenu'], bins=bins, labels=labels, right=False)

    # Calculer la proportion d'achats en promotion par rapport au total des achats pour chaque client
    # Remplacer 0 par 1 dans 'Total_Achats' pour éviter la division par zéro
    df_revenu['Proportion_Promo'] = (df_revenu['Achats_Promotions'] / df_revenu['Total_Achats'].replace(0, 1)) * 100

    # --- 3. ANALYSE ET AGRÉGATION ---
    # Calculer la proportion moyenne d'achats en promotion pour chaque catégorie de revenu
    promo_par_revenu = df_revenu.groupby('Categorie_Revenu')['Proportion_Promo'].mean().reset_index()

    print("\nProportion moyenne des achats en promotion par tranche de revenu :")
    print(promo_par_revenu)

    # --- 4. CRÉATION DU GRAPHIQUE ---
    print("\nGénération du graphique...")
    plt.figure(figsize=(14, 8))
    barplot = sns.barplot(x='Categorie_Revenu', y='Proportion_Promo', data=promo_par_revenu, palette='magma')

    # Ajouter les valeurs en pourcentage sur les barres
    for p in barplot.patches:
        barplot.annotate(f'{p.get_height():.1f}%', 
                         (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=12)

    plt.title('Proportion Moyenne des Achats en Promotion par Tranche de Revenu', fontsize=18, pad=20)
    plt.ylabel('Proportion moyenne des achats en promotion (%)', fontsize=14)
    plt.xlabel('Tranche de Revenu Annuel', fontsize=14)
    plt.xticks(rotation=0)
    plt.tight_layout()

    # --- 5. SAUVEGARDE DU GRAPHIQUE ---
    output_path = os.path.join(output_dir, 'proportion_promo_par_revenu.png')
    plt.savefig(output_path, dpi=300)
    print(f"\nGraphique sauvegardé avec succès dans : {output_path}")

    # --- 6. ANALYSE DES DÉPENSES PAR PRODUIT ET PAR REVENU ---
    print("\nGénération du graphique des dépenses par produit en fonction du revenu...")

    # Lister les colonnes de produits
    colonnes_produits = {
        'Achat_Vins': 'Vins',
        'Achat_Viandes': 'Viandes',
        'Achat_Fruits': 'Fruits',
        'Achat_Poissons': 'Poissons',
        'Achat_Produits_Sucres': 'Produits Sucrés',
        'Achat_Produits_Or': 'Produits Or'
    }

    # Agréger les dépenses par catégorie de revenu pour chaque produit
    depenses_par_revenu = df_revenu.groupby('Categorie_Revenu')[list(colonnes_produits.keys())].sum()
    depenses_par_revenu.columns = colonnes_produits.values()

    # Calculer le pourcentage de chaque produit par rapport au total des dépenses de la catégorie
    depenses_pourcentage = depenses_par_revenu.div(depenses_par_revenu.sum(axis=1), axis=0) * 100

    print("\nRépartition des dépenses par produit et par tranche de revenu (%):")
    print(depenses_pourcentage)

    # --- 7. CRÉATION DU GRAPHIQUE 100% EMPILÉ ---
    # Définir une liste de couleurs personnalisée pour que "Produits Or" soit en noir
    # L'ordre des couleurs doit correspondre à l'ordre des colonnes dans 'depenses_pourcentage'
    couleurs_perso = [
        '#2a7886',  # Vins
        '#7ad151',  # Viandes
        '#fde725',  # Fruits
        '#414487',  # Poissons
        '#f57f17',  # Produits Sucrés
        '#000000'   # Produits Or (Noir)
    ]
    ax_produits_revenu = depenses_pourcentage.plot(
        kind='bar', 
        stacked=True, 
        figsize=(16, 10), 
        color=couleurs_perso
    )

    plt.title('Répartition des Dépenses par Catégorie de Produit en fonction du Revenu', fontsize=18, pad=20)
    plt.ylabel('Pourcentage des dépenses totales (%)', fontsize=14)
    plt.xlabel('Tranche de Revenu Annuel', fontsize=14)
    plt.xticks(rotation=0)
    plt.legend(title='Catégorie de Produit', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout(rect=[0, 0, 0.88, 1]) # Ajuster pour que la légende ne soit pas coupée

    # --- 8. SAUVEGARDE DU NOUVEAU GRAPHIQUE ---
    output_produits_path = os.path.join(output_dir, 'repartition_depenses_par_revenu.png')
    plt.savefig(output_produits_path, dpi=300)
    print(f"\nGraphique des dépenses par revenu sauvegardé avec succès dans : {output_produits_path}")

except FileNotFoundError:
    print(f"ERREUR : Le fichier '{file_path}' est introuvable. Assurez-vous qu'il existe bien.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")