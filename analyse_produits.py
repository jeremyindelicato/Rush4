import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. CHARGEMENT DES DONNÉES ---
# Chemin vers le fichier final que nous avons créé avec aa.py
file_path = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\Camp_Market_final.csv'

# --- CRÉATION DU DOSSIER DE SORTIE ---
output_dir = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\graph_produits'
os.makedirs(output_dir, exist_ok=True)

try:
    df = pd.read_csv(file_path)
    print(f"Fichier '{file_path}' chargé avec succès.\n")
    print(f"Dossier de sortie '{output_dir}' prêt.\n")

    # --- 2. SÉLECTION DES COLONNES DE PRODUITS ---

    # Lister les colonnes correspondant aux dépenses par produit
    colonnes_produits = {
        'Achat_Vins': 'Vins',
        'Achat_Viandes': 'Viandes',
        'Achat_Fruits': 'Fruits',
        'Achat_Poissons': 'Poissons',
        'Achat_Produits_Sucres': 'Produits Sucrés',
        'Achat_Produits_Or': 'Produits Or'
    }

    # Sélectionner et renommer les colonnes pour le graphique
    df_produits = df[list(colonnes_produits.keys())].rename(columns=colonnes_produits)

    # --- 3. CRÉATION DU GRAPHIQUE EN MOUSTACHE (BOX PLOT) ---
    print("Génération du graphique en moustache...")
    plt.figure(figsize=(16, 9))
    
    # Créer le box plot avec Seaborn
    sns.boxplot(data=df_produits, palette='pastel')
    
    # Ajouter des titres et des étiquettes pour une meilleure compréhension
    plt.title('Distribution des Dépenses par Catégorie de Produit', fontsize=18, pad=20)
    plt.ylabel('Montant Dépensé', fontsize=14)
    plt.xlabel('Catégorie de Produit', fontsize=14)
    plt.xticks(rotation=45, ha='right') # Améliorer la lisibilité des étiquettes
    plt.tight_layout() # Ajuster la mise en page

    # --- 4. SAUVEGARDE DU GRAPHIQUE ---
    output_image_path = os.path.join(output_dir, 'boxplot_depenses_produits.png')
    plt.savefig(output_image_path, dpi=300) # Sauvegarder le graphique en haute résolution
    print(f"\nGraphique sauvegardé avec succès dans : {output_image_path}")

    # --- 5. CRÉATION DE LA HEATMAP DE CORRÉLATION ---
    print("\nGénération de la heatmap de corrélation...")
    
    # Calculer la matrice de corrélation
    correlation_matrix = df_produits.corr()

    # Créer la heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    
    # Ajouter des titres et des étiquettes
    plt.title('Heatmap de Corrélation des Dépenses par Catégorie', fontsize=16, pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()

    # --- 6. SAUVEGARDE DE LA HEATMAP ---
    output_heatmap_path = os.path.join(output_dir, 'heatmap_correlation_produits.png')
    plt.savefig(output_heatmap_path, dpi=300)
    print(f"\nHeatmap sauvegardée avec succès dans : {output_heatmap_path}")

    # --- 7. CRÉATION DU GRAPHIQUE DES DÉPENSES TOTALES ---
    print("\nGénération du graphique des dépenses totales par produit...")

    # Calculer les dépenses totales par catégorie
    total_depenses = df_produits.sum().sort_values(ascending=False)

    # Créer le graphique à barres
    plt.figure(figsize=(12, 8))
    sns.barplot(x=total_depenses.index, y=total_depenses.values, palette='viridis')

    # Ajouter des titres et des étiquettes
    plt.title('Dépenses Totales par Catégorie de Produit', fontsize=16, pad=20)
    plt.ylabel('Montant Total Dépensé', fontsize=12)
    plt.xlabel('Catégorie de Produit', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # --- 8. SAUVEGARDE DU GRAPHIQUE ---
    output_barchart_path = os.path.join(output_dir, 'total_depenses_par_produit.png')
    plt.savefig(output_barchart_path, dpi=300)
    print(f"\nGraphique à barres sauvegardé avec succès dans : {output_barchart_path}")

    # --- 9. ANALYSE DE L'INFLUENCE DES PROMOTIONS SUR LES ACHATS ---
    print("\nAnalyse de l'influence des promotions sur les catégories de produits...")

    # Sélectionner les colonnes de produits et la colonne des promotions
    colonnes_analyse_promo = list(colonnes_produits.keys()) + ['Achats_Promotions']
    df_promo = df[colonnes_analyse_promo]

    # Calculer la corrélation de chaque catégorie de produit avec les achats en promotion
    correlation_promo = df_promo.corr()['Achats_Promotions'].drop('Achats_Promotions')
    
    # Renommer les index pour le graphique
    correlation_promo.index = correlation_promo.index.map(colonnes_produits)
    correlation_promo = correlation_promo.sort_values(ascending=False)

    # Créer le graphique à barres
    plt.figure(figsize=(12, 8))
    barplot_promo = sns.barplot(x=correlation_promo.index, y=correlation_promo.values, palette='coolwarm_r')

    # Ajouter les valeurs de corrélation sur les barres
    for p in barplot_promo.patches:
        barplot_promo.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                               ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=11)

    plt.title('Corrélation entre les Achats en Promotion et les Dépenses par Catégorie', fontsize=16, pad=20)
    plt.ylabel('Coefficient de Corrélation', fontsize=12)
    plt.xlabel('Catégorie de Produit', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # --- 10. SAUVEGARDE DU GRAPHIQUE DE CORRÉLATION ---
    output_promo_corr_path = os.path.join(output_dir, 'correlation_produits_promotions.png')
    plt.savefig(output_promo_corr_path, dpi=300)
    print(f"\nGraphique de corrélation avec les promotions sauvegardé avec succès dans : {output_promo_corr_path}")

    # --- 11. NOUVELLE ANALYSE : PART DES PROMOTIONS DANS LES DÉPENSES PAR PRODUIT (ESTIMATION) ---
    print("\nAnalyse de la part estimée des promotions dans les dépenses par produit...")

    # Calculer la dépense moyenne par achat pour chaque client (en gérant les cas de 0 achat)
    # La colonne 'Depense_Moy_Par_Achat' existe déjà dans le CSV final, nous pouvons la réutiliser.
    # S'assurer qu'il n'y a pas de valeurs NaN ou infinies qui pourraient causer des erreurs.
    df['Depense_Moy_Par_Achat'] = df['Depense_Moy_Par_Achat'].fillna(0)

    # Estimer la valeur totale des achats en promotion pour chaque client
    valeur_promo_client = df['Achats_Promotions'] * df['Depense_Moy_Par_Achat']

    # Estimer la part des promotions pour chaque catégorie de produit
    depenses_promo_estimees = {}
    depenses_normales_estimees = {}

    for col, nom in colonnes_produits.items():
        # Proportion de la dépense de ce produit par rapport à la dépense totale du client
        proportion_produit = df[col] / df['Total_Depense'].replace(0, 1) # Remplacer 0 pour éviter la division par zéro
        
        # Estimer la valeur des promotions pour ce produit et pour chaque client
        promo_produit_client = valeur_promo_client * proportion_produit
        
        # Agréger les résultats pour tous les clients
        depenses_promo_estimees[nom] = promo_produit_client.sum()
        depenses_normales_estimees[nom] = df[col].sum() - depenses_promo_estimees[nom]

    # Créer un DataFrame pour le graphique
    df_part_promo = pd.DataFrame({'Promotion': depenses_promo_estimees, 'Normal': depenses_normales_estimees})
    df_part_promo = df_part_promo.sort_values(by='Promotion', ascending=False)

    # Créer le graphique à barres empilées
    ax_part_promo = df_part_promo.plot(kind='bar', stacked=True, figsize=(14, 9), colormap='autumn')

    # Ajouter les pourcentages et les totaux sur les barres
    for i, (index, row) in enumerate(df_part_promo.iterrows()):
        total_depenses = row.sum()
        promo_depenses = row['Promotion']
        
        # Gérer la division par zéro si le total est nul
        if total_depenses > 0:
            pourcentage_promo = (promo_depenses / total_depenses) * 100
        else:
            pourcentage_promo = 0

        # Afficher le total des dépenses au-dessus de la barre
        ax_part_promo.text(i, total_depenses + 5000, f'Total: {total_depenses:,.0f} €'.replace(',', ' '), ha='center', fontsize=11)
        # Afficher le pourcentage de promotion à l'intérieur de la barre de promotion
        ax_part_promo.text(i, promo_depenses / 2, f'{pourcentage_promo:.1f}%', ha='center', va='center', color='white', fontsize=11, weight='bold')

    plt.title('Part Estimée des Ventes en Promotion par Catégorie de Produit', fontsize=18, pad=20)
    plt.ylabel('Montant Total Dépensé (€)', fontsize=14)
    plt.xlabel('Catégorie de Produit', fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Type de Vente')
    plt.tight_layout()

    # --- 12. SAUVEGARDE DU NOUVEAU GRAPHIQUE ---
    output_part_promo_path = os.path.join(output_dir, 'part_promotions_par_produit.png')
    plt.savefig(output_part_promo_path, dpi=300)
    print(f"\nGraphique de la part des promotions sauvegardé avec succès dans : {output_part_promo_path}")

except FileNotFoundError:
    print(f"ERREUR : Le fichier '{file_path}' est introuvable. Assurez-vous qu'il existe bien.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")
