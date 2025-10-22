import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. CHARGEMENT DES DONNÉES ---
file_path = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\Camp_Market_final.csv'

# --- CRÉATION DU DOSSIER DE SORTIE ---
output_dir = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\graph_statut_marital'
os.makedirs(output_dir, exist_ok=True)

try:
    df = pd.read_csv(file_path)
    print(f"Fichier '{file_path}' chargé avec succès.\n")
    print(f"Dossier de sortie '{output_dir}' prêt.\n")

    # --- 2. PRÉPARATION DES DONNÉES ---
    print("Préparation des données et création des groupes (Seul vs En Couple)...")
    
    # Définir les statuts pour chaque groupe
    statuts_couple = ['Married', 'Together']
    statuts_seul = ['Single', 'Divorced', 'Widow', 'Alone']

    # Filtrer le DataFrame pour ne garder que les statuts pertinents
    df_statut = df[df['Statut_Marital_Texte'].isin(statuts_couple + statuts_seul)].copy()

    # Créer une catégorie pour les ménages (Seul vs En Couple)
    df_statut['Type_Relation'] = df_statut['Statut_Marital_Texte'].apply(lambda x: 'En Couple' if x in statuts_couple else 'Seul')

    # Calculer la proportion d'achats en promotion pour chaque client
    df_statut['Proportion_Promo'] = (df_statut['Achats_Promotions'] / df_statut['Total_Achats'].replace(0, 1)) * 100

    # --- 3. ANALYSE DES DÉPENSES PAR PRODUIT ET STATUT MARITAL ---
    print("\nGénération du graphique des dépenses par produit en fonction du statut marital...")

    colonnes_produits = {
        'Achat_Vins': 'Vins', 'Achat_Viandes': 'Viandes', 'Achat_Fruits': 'Fruits',
        'Achat_Poissons': 'Poissons', 'Achat_Produits_Sucres': 'Produits Sucrés', 'Achat_Produits_Or': 'Produits Or'
    }

    depenses_par_statut = df_statut.groupby('Type_Relation')[list(colonnes_produits.keys())].sum()
    depenses_par_statut.columns = colonnes_produits.values()

    depenses_pourcentage = depenses_par_statut.div(depenses_par_statut.sum(axis=1), axis=0) * 100

    print("\nRépartition des dépenses par produit et par statut marital (%):")
    print(depenses_pourcentage)

    # --- 4. CRÉATION DU GRAPHIQUE 100% EMPILÉ ---
    couleurs_perso = ['#2a7886', '#7ad151', '#fde725', '#414487', '#f57f17', '#000000']
    
    ax = depenses_pourcentage.plot(kind='bar', stacked=True, figsize=(14, 9), color=couleurs_perso)

    plt.title('Répartition des Dépenses par Produit selon le Statut Marital', fontsize=18, pad=20)
    plt.ylabel('Pourcentage des dépenses totales (%)', fontsize=14)
    plt.xlabel('Statut Marital', fontsize=14)
    plt.xticks(rotation=0)
    plt.legend(title='Catégorie de Produit', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout(rect=[0, 0, 0.88, 1])

    output_path = os.path.join(output_dir, 'repartition_depenses_par_statut.png')
    plt.savefig(output_path, dpi=300)
    print(f"\nGraphique des dépenses par statut sauvegardé avec succès dans : {output_path}")

    # --- 5. ANALYSE DE LA PROPORTION DES ACHATS EN PROMOTION ---
    print("\nAnalyse de la proportion des achats en promotion par statut marital...")

    promo_par_statut_prop = df_statut.groupby('Type_Relation')['Proportion_Promo'].mean().reset_index()
    print("\nProportion moyenne des achats en promotion par statut marital :")
    print(promo_par_statut_prop)

    plt.figure(figsize=(12, 7))
    barplot_promo = sns.barplot(x='Type_Relation', y='Proportion_Promo', data=promo_par_statut_prop, palette='coolwarm')

    for p in barplot_promo.patches:
        barplot_promo.annotate(f'{p.get_height():.1f}%', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=12)

    plt.title('Proportion Moyenne des Achats en Promotion par Statut Marital', fontsize=16, pad=20)
    plt.ylabel('Proportion moyenne des achats en promotion (%)', fontsize=12)
    plt.xlabel('Statut Marital', fontsize=12)
    plt.tight_layout()

    output_promo_path = os.path.join(output_dir, 'proportion_promo_par_statut.png')
    plt.savefig(output_promo_path, dpi=300)
    print(f"\nGraphique de la proportion des promotions sauvegardé avec succès dans : {output_promo_path}")

except FileNotFoundError:
    print(f"ERREUR : Le fichier '{file_path}' est introuvable. Assurez-vous qu'il existe bien.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")