import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. CHARGEMENT DES DONNÉES ---
file_path = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\Camp_Market_final.csv'

# --- CRÉATION DU DOSSIER DE SORTIE ---
output_dir = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\graph_enfants'
os.makedirs(output_dir, exist_ok=True)

try:
    df = pd.read_csv(file_path)
    print(f"Fichier '{file_path}' chargé avec succès.\n")
    print(f"Dossier de sortie '{output_dir}' prêt.\n")

    # --- 2. PRÉPARATION DES DONNÉES ---
    print("Préparation des données et création des types de ménages...")
    
    # Créer une colonne pour le nombre total d'enfants/ados
    df['Total_Enfants'] = df['Enfants_Maison'] + df['Ados_Maison']

    # Créer une catégorie pour les ménages avec ou sans enfants/ados
    df['Type_Menage'] = df['Total_Enfants'].apply(lambda x: 'Avec Enfants/Ados' if x > 0 else 'Sans Enfants/Ados')

    # Calculer la proportion d'achats en promotion pour chaque client
    df['Proportion_Promo'] = (df['Achats_Promotions'] / df['Total_Achats'].replace(0, 1)) * 100

    # --- 3. ANALYSE DES DÉPENSES PAR PRODUIT ET TYPE DE MÉNAGE ---
    print("\nGénération du graphique des dépenses par produit en fonction de la présence d'enfants...")

    # Lister les colonnes de produits
    colonnes_produits = {
        'Achat_Vins': 'Vins',
        'Achat_Viandes': 'Viandes',
        'Achat_Fruits': 'Fruits',
        'Achat_Poissons': 'Poissons',
        'Achat_Produits_Sucres': 'Produits Sucrés',
        'Achat_Produits_Or': 'Produits Or'
    }

    # Agréger les dépenses par type de ménage pour chaque produit
    depenses_par_menage = df.groupby('Type_Menage')[list(colonnes_produits.keys())].sum()
    depenses_par_menage.columns = colonnes_produits.values()

    # Calculer le pourcentage de chaque produit par rapport au total des dépenses de la catégorie
    depenses_pourcentage = depenses_par_menage.div(depenses_par_menage.sum(axis=1), axis=0) * 100

    print("\nRépartition des dépenses par produit et par type de ménage (%):")
    print(depenses_pourcentage)

    # --- 4. CRÉATION DU GRAPHIQUE 100% EMPILÉ ---
    # Définir une liste de couleurs personnalisée pour que "Produits Or" soit en noir
    couleurs_perso = [
        '#2a7886',  # Vins
        '#7ad151',  # Viandes
        '#fde725',  # Fruits
        '#414487',  # Poissons
        '#f57f17',  # Produits Sucrés
        '#000000'   # Produits Or (Noir)
    ]
    
    ax = depenses_pourcentage.plot(
        kind='bar', 
        stacked=True, 
        figsize=(14, 9), 
        color=couleurs_perso
    )

    plt.title('Répartition des Dépenses par Produit selon la Présence d\'Enfants/Ados', fontsize=18, pad=20)
    plt.ylabel('Pourcentage des dépenses totales (%)', fontsize=14)
    plt.xlabel('Type de Ménage', fontsize=14)
    plt.xticks(rotation=0)
    plt.legend(title='Catégorie de Produit', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout(rect=[0, 0, 0.88, 1])

    # --- 5. SAUVEGARDE DU GRAPHIQUE ---
    output_path = os.path.join(output_dir, 'repartition_depenses_par_type_menage.png')
    plt.savefig(output_path, dpi=300)
    print(f"\nGraphique sauvegardé avec succès dans : {output_path}")

    # --- 6. ANALYSE DE LA PROPORTION DES ACHATS EN PROMOTION ---
    print("\nAnalyse de la proportion des achats en promotion par type de ménage...")

    # Calculer la proportion moyenne d'achats en promotion pour chaque type de ménage
    promo_par_menage_prop = df.groupby('Type_Menage')['Proportion_Promo'].mean().reset_index()

    print("\nProportion moyenne des achats en promotion par type de ménage :")
    print(promo_par_menage_prop)

    # --- 7. CRÉATION DU GRAPHIQUE DE PROPORTION DES PROMOTIONS ---
    plt.figure(figsize=(12, 7))
    barplot_promo = sns.barplot(x='Type_Menage', y='Proportion_Promo', data=promo_par_menage_prop, palette='coolwarm')

    # Ajouter les valeurs en pourcentage sur les barres
    for p in barplot_promo.patches:
        barplot_promo.annotate(f'{p.get_height():.1f}%', 
                               (p.get_x() + p.get_width() / 2., p.get_height()),
                               ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=12)

    plt.title('Proportion Moyenne des Achats en Promotion par Type de Ménage', fontsize=16, pad=20)
    plt.ylabel('Proportion moyenne des achats en promotion (%)', fontsize=12)
    plt.xlabel('Type de Ménage', fontsize=12)
    plt.tight_layout()

    # --- 8. SAUVEGARDE DU NOUVEAU GRAPHIQUE ---
    output_promo_path = os.path.join(output_dir, 'proportion_promo_par_menage.png')
    plt.savefig(output_promo_path, dpi=300)
    print(f"\nGraphique de la proportion des promotions sauvegardé avec succès dans : {output_promo_path}")

except FileNotFoundError:
    print(f"ERREUR : Le fichier '{file_path}' est introuvable. Assurez-vous qu'il existe bien.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")