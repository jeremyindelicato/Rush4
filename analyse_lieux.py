import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# --- 1. CHARGEMENT DES DONNÉES ---
# Chemin vers le fichier final
file_path = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\Camp_Market_final.csv'

# --- CRÉATION DU DOSSIER DE SORTIE ---
output_dir = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\graph_lieux'
os.makedirs(output_dir, exist_ok=True)

try:
    df = pd.read_csv(file_path)
    print(f"Fichier '{file_path}' chargé avec succès.\n")
    print(f"Dossier de sortie '{output_dir}' prêt.\n")

    # --- 2. CRÉATION DU GRAPHIQUE DES ACHATS PAR PLATEFORME AVEC PROMOTIONS ---
    print("\nGénération du graphique des achats par plateforme avec promotions...")

    # Sélectionner les colonnes relatives aux plateformes d'achat
    colonnes_plateformes = {
        'Achats_En_Ligne': 'En Ligne',
        'Achats_Catalogue': 'Catalogue',
        'Achats_En_Magasin': 'En Magasin'
    }

    # --- NOUVELLE MÉTHODE D'ESTIMATION (CLIENT PAR CLIENT) ---
    # Estimer la part des promotions pour chaque plateforme en se basant sur les habitudes de chaque client
    promo_par_plateforme = {}
    normaux_par_plateforme = {}

    for col, nom in colonnes_plateformes.items():
        # Proportion des achats de ce client sur cette plateforme
        # Remplacer 0 par 1 dans 'Total_Achats' pour éviter la division par zéro pour les clients sans achat
        proportion_plateforme_client = df[col] / df['Total_Achats'].replace(0, 1)
        
        # Estimer le nombre d'achats en promotion pour cette plateforme et pour chaque client
        promo_plateforme_client = df['Achats_Promotions'] * proportion_plateforme_client
        
        # Agréger les résultats pour tous les clients
        total_promo_estime = promo_plateforme_client.sum()
        promo_par_plateforme[nom] = total_promo_estime
        normaux_par_plateforme[nom] = df[col].sum() - total_promo_estime

    # Créer un DataFrame pour le graphique
    df_plateformes = pd.DataFrame({
        'Promotion': promo_par_plateforme,
        'Normal': normaux_par_plateforme
    }).rename(index=colonnes_plateformes)

    # Créer le graphique à barres empilées
    ax = df_plateformes.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='plasma')

    # Ajouter les pourcentages et les totaux
    for i, (index, row) in enumerate(df_plateformes.iterrows()):
        total_ventes = row.sum()
        promo_ventes = row['Promotion']        
        # Gérer la division par zéro si le total est nul
        if total_ventes == 0:
            continue
        pourcentage_promo = (promo_ventes / total_ventes) * 100
        ax.text(i, total_ventes + 50, f'Total: {total_ventes:,.0f}', ha='center', fontsize=10)
        ax.text(i, promo_ventes / 2, f'{pourcentage_promo:.1f}%', ha='center', va='center', color='white', fontsize=10)

    plt.title('Répartition des Achats par Plateforme (avec et sans Promotion)', fontsize=16, pad=20)
    plt.ylabel('Nombre d\'Achats', fontsize=12)
    plt.xlabel('Plateforme d\'Achat', fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title='Type d\'Achat')
    plt.tight_layout()

    output_plateforme_path = os.path.join(output_dir, 'repartition_achats_plateforme.png')
    plt.savefig(output_plateforme_path, dpi=300)
    print(f"\nGraphique des plateformes sauvegardé avec succès dans : {output_plateforme_path}")

    # --- 3. CRÉATION DU GRAPHIQUE DES DÉPENSES PAR PRODUIT ET PAR PLATEFORME (ESTIMATION) ---
    print("\nGénération du graphique des dépenses estimées par produit et par plateforme...")

    # Lister les colonnes de produits
    colonnes_produits = {
        'Achat_Vins': 'Vins',
        'Achat_Viandes': 'Viandes',
        'Achat_Fruits': 'Fruits',
        'Achat_Poissons': 'Poissons',
        'Achat_Produits_Sucres': 'Produits Sucrés',
        'Achat_Produits_Or': 'Produits Or'
    }

    # Calculer les dépenses totales pour chaque catégorie de produit
    total_depenses_produit = df[list(colonnes_produits.keys())].sum()

    # Créer un DataFrame pour stocker les dépenses estimées par plateforme
    df_depenses_estimees = pd.DataFrame(index=colonnes_produits.values())

    # Estimer les dépenses pour chaque produit sur chaque plateforme
    for col_plateforme, nom_plateforme in colonnes_plateformes.items():
        # Proportion des achats de chaque client sur cette plateforme
        proportion_plateforme_client = df[col_plateforme] / df['Total_Achats'].replace(0, 1)
        # Estimer les dépenses pour chaque produit sur cette plateforme
        depenses_estimees_plateforme = (proportion_plateforme_client.values[:, np.newaxis] * df[list(colonnes_produits.keys())]).sum()
        df_depenses_estimees[nom_plateforme] = depenses_estimees_plateforme.values

    # Renommer les colonnes du DataFrame pour le graphique
    df_depenses_estimees = df_depenses_estimees.rename(columns={'Achats_En_Ligne': 'En Ligne', 'Achats_Catalogue': 'Catalogue', 'Achats_En_Magasin': 'En Magasin'})

    # Créer le graphique à barres empilées
    ax_produits = df_depenses_estimees.T.plot(kind='bar', stacked=True, figsize=(16, 10), colormap='terrain')

    # Ajouter des titres et des étiquettes
    plt.title('Dépenses Estimées par Catégorie de Produit sur Chaque Plateforme', fontsize=18, pad=20)
    plt.ylabel('Montant Total Dépensé (Estimation en €)', fontsize=14)
    plt.xlabel('Plateforme d\'Achat', fontsize=14)
    plt.xticks(rotation=0)
    plt.legend(title='Catégorie de Produit', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout(rect=[0, 0, 0.85, 1]) # Ajuster pour que la légende ne soit pas coupée

    # Sauvegarder le nouveau graphique
    output_produits_plateforme_path = os.path.join(output_dir, 'repartition_produits_par_plateforme.png')
    plt.savefig(output_produits_plateforme_path, dpi=300)
    print(f"\nGraphique des produits par plateforme sauvegardé avec succès dans : {output_produits_plateforme_path}")

except FileNotFoundError:
    print(f"ERREUR : Le fichier '{file_path}' est introuvable. Assurez-vous qu'il existe bien.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")