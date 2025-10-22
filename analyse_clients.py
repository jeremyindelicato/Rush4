import pandas as pd
import matplotlib.pyplot as plt
import os

# --- 1. CHARGEMENT DES DONNÉES ---
file_path = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\Camp_Market_final.csv'

# --- CRÉATION DU DOSSIER DE SORTIE ---
output_dir = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\graph_clients'
os.makedirs(output_dir, exist_ok=True)

try:
    df = pd.read_csv(file_path)
    print(f"Fichier '{file_path}' chargé avec succès.\n")
    print(f"Dossier de sortie '{output_dir}' prêt.\n")

    # --- 2. PRÉPARATION ET FILTRAGE DES DONNÉES ---
    print("Filtrage des données pour les personnes seules...")
    
    # Définir les statuts pour le groupe "Seul"
    statuts_seul = ['Single', 'Divorced', 'Widow', 'Alone']

    # Filtrer le DataFrame pour ne garder que les personnes seules
    df_seul = df[df['Statut_Marital_Texte'].isin(statuts_seul)].copy()

    # Créer une colonne pour le nombre total d'enfants/ados
    df_seul['Total_Enfants'] = df_seul['Enfants_Maison'] + df_seul['Ados_Maison']

    # Créer une catégorie pour les personnes seules avec ou sans enfants/ados
    df_seul['Type_Menage_Seul'] = df_seul['Total_Enfants'].apply(lambda x: 'Avec Enfants/Ados' if x > 0 else 'Sans Enfants/Ados')

    # --- 3. GRAPHIQUE : POURCENTAGE DE PERSONNES SEULES AVEC/SANS ENFANTS ---
    print("\nGénération du graphique de répartition des personnes seules...")
    
    repartition = df_seul['Type_Menage_Seul'].value_counts()
    
    plt.figure(figsize=(10, 8))
    plt.pie(repartition, labels=repartition.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'], textprops={'fontsize': 14})
    plt.title('Répartition des Personnes Seules (avec ou sans enfants/ados)', fontsize=18, pad=20)
    plt.axis('equal')  # Assure que le pie chart est un cercle.

    # Sauvegarde du graphique
    output_pie_path = os.path.join(output_dir, 'repartition_personnes_seules.png')
    plt.savefig(output_pie_path, dpi=300)
    print(f"\nGraphique de répartition sauvegardé avec succès dans : {output_pie_path}")

    # --- 4. ANALYSE DES DÉPENSES PAR PRODUIT POUR CE SEGMENT ---
    print("\nGénération du graphique de comparaison des dépenses...")

    colonnes_produits = {
        'Achat_Vins': 'Vins', 'Achat_Viandes': 'Viandes', 'Achat_Fruits': 'Fruits',
        'Achat_Poissons': 'Poissons', 'Achat_Produits_Sucres': 'Produits Sucrés', 'Achat_Produits_Or': 'Produits Or'
    }

    depenses_par_groupe = df_seul.groupby('Type_Menage_Seul')[list(colonnes_produits.keys())].sum()
    depenses_par_groupe.columns = colonnes_produits.values()

    depenses_pourcentage = depenses_par_groupe.div(depenses_par_groupe.sum(axis=1), axis=0) * 100

    print("\nRépartition des dépenses pour les personnes seules (%):")
    print(depenses_pourcentage)

    # --- 5. CRÉATION DU GRAPHIQUE 100% EMPILÉ ---
    couleurs_perso = ['#2a7886', '#7ad151', '#fde725', '#414487', '#f57f17', '#000000']
    
    ax = depenses_pourcentage.plot(
        kind='bar', 
        stacked=True, 
        figsize=(14, 9), 
        color=couleurs_perso
    )

    plt.title('Comparaison des Dépenses des Personnes Seules', fontsize=18, pad=20)
    plt.ylabel('Pourcentage des dépenses totales (%)', fontsize=14)
    plt.xlabel('Type de Ménage (Personnes Seules)', fontsize=14)
    plt.xticks(rotation=0)
    plt.legend(title='Catégorie de Produit', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout(rect=[0, 0, 0.88, 1])

    # --- 6. SAUVEGARDE DU GRAPHIQUE ---
    output_bar_path = os.path.join(output_dir, 'comparaison_depenses_personnes_seules.png')
    plt.savefig(output_bar_path, dpi=300)
    print(f"\nGraphique de comparaison des dépenses sauvegardé avec succès dans : {output_bar_path}")

except FileNotFoundError:
    print(f"ERREUR : Le fichier '{file_path}' est introuvable. Assurez-vous qu'il existe bien.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")