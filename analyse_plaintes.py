import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

# --- 1. CHARGEMENT ET PRÉPARATION DES DONNÉES ---
file_path = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\Camp_Market_final.csv'

# --- CRÉATION DU DOSSIER DE SORTIE ---
output_dir = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\graph_plaintes'
os.makedirs(output_dir, exist_ok=True)

try:
    df = pd.read_csv(file_path)
    print(f"Fichier '{file_path}' chargé avec succès.\n")
    print(f"Dossier de sortie '{output_dir}' prêt.\n")

    # --- 2. PRÉPARATION DES CATÉGORIES DE CLIENTS ---
    print("Préparation des catégories de clients pour l'analyse des plaintes...")

    # Catégorie Statut Marital
    statuts_couple = ['Married', 'Together']
    df['Type_Relation'] = df['Statut_Marital_Texte'].apply(lambda x: 'En Couple' if x in statuts_couple else 'Seul')

    # Catégorie Enfants
    df['Total_Enfants'] = df['Enfants_Maison'] + df['Ados_Maison']
    df['Type_Menage'] = df['Total_Enfants'].apply(lambda x: 'Avec Enfants/Ados' if x > 0 else 'Sans Enfants/Ados')

    # Catégorie Revenu
    df_revenu = df[df['Revenu'] > 0].copy()
    bins = [0, 25000, 50000, 75000, 100000, np.inf]
    labels = ['< 25k €', '25k-50k €', '50k-75k €', '75k-100k €', '> 100k €']
    df_revenu['Categorie_Revenu'] = pd.cut(df_revenu['Revenu'], bins=bins, labels=labels, right=False)

    # Ordre pour le niveau d'éducation
    ordre_education = ['Basic', '2n Cycle', 'Graduation', 'Master', 'PhD']
    df['Niveau_Education'] = pd.Categorical(df['Niveau_Education'], categories=ordre_education, ordered=True)

    # --- 3. CALCUL DES TAUX DE PLAINTE ---
    def calculate_complaint_rate(dataframe, group_col):
        # Calculer le nombre total de clients et le nombre de plaintes par groupe
        grouped = dataframe.groupby(group_col).agg(
            Total_Clients=('ID_Client', 'count'),
            Total_Plaintes=('Plainte', 'sum')
        ).reset_index()
        # Calculer le taux de plainte en pourcentage
        grouped['Taux_Plainte'] = (grouped['Total_Plaintes'] / grouped['Total_Clients']) * 100
        return grouped

    # Calculer les taux pour chaque catégorie
    rate_education = calculate_complaint_rate(df, 'Niveau_Education')
    rate_relation = calculate_complaint_rate(df, 'Type_Relation')
    rate_menage = calculate_complaint_rate(df, 'Type_Menage')
    rate_revenu = calculate_complaint_rate(df_revenu, 'Categorie_Revenu')

    # --- 4. CRÉATION DU TABLEAU DE BORD (DASHBOARD) ---
    print("\nGénération du tableau de bord des plaintes...")
    fig, axes = plt.subplots(2, 2, figsize=(20, 16))
    fig.suptitle('Profil des Clients qui se Plaignent', fontsize=24, weight='bold')

    # Fonction pour créer chaque sous-graphique
    def create_subplot(ax, data, x_col, y_col, title, order=None):
        sns.barplot(ax=ax, x=x_col, y=y_col, data=data, palette='Reds_d', order=order)
        ax.set_title(title, fontsize=16)
        ax.set_xlabel('')
        ax.set_ylabel('Taux de Plainte (%)', fontsize=12)
        for p in ax.patches:
            if p.get_height() > 0:
                ax.annotate(f'{p.get_height():.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=11)

    # Créer les 4 graphiques
    create_subplot(axes[0, 0], rate_education, 'Niveau_Education', 'Taux_Plainte', 'Par Niveau d\'Éducation', order=ordre_education)
    create_subplot(axes[0, 1], rate_relation, 'Type_Relation', 'Taux_Plainte', 'Par Statut Marital')
    create_subplot(axes[1, 0], rate_menage, 'Type_Menage', 'Taux_Plainte', 'Par Type de Ménage')
    create_subplot(axes[1, 1], rate_revenu, 'Categorie_Revenu', 'Taux_Plainte', 'Par Tranche de Revenu')

    # Ajuster la mise en page et sauvegarder
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    output_path = os.path.join(output_dir, 'dashboard_profil_plaintes.png')
    plt.savefig(output_path, dpi=300)
    print(f"\nTableau de bord des plaintes sauvegardé avec succès dans : {output_path}")

except FileNotFoundError:
    print(f"ERREUR : Le fichier '{file_path}' est introuvable. Assurez-vous qu'il existe bien.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")