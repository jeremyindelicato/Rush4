import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- 1. CHARGEMENT DES DONNÉES ---
file_path = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\Camp_Market_final.csv'

# --- CRÉATION DU DOSSIER DE SORTIE ---
output_dir = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\graph_jours_campagnes'
os.makedirs(output_dir, exist_ok=True)

try:
    df = pd.read_csv(file_path)
    print(f"Fichier '{file_path}' chargé avec succès.\n")
    print(f"Dossier de sortie '{output_dir}' prêt.\n")

    # --- 2. PRÉPARATION DES DONNÉES ---
    print("Préparation des données sur les jours d'inscription...")
    
    # Définir un ordre logique pour les jours de la semaine
    ordre_jours = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['Jour_Inscription'] = pd.Categorical(df['Jour_Inscription'], categories=ordre_jours, ordered=True)

    # --- 3. GRAPHIQUE 1 : RÉPARTITION GLOBALE DES INSCRIPTIONS ---
    print("\nGénération du graphique de la répartition globale des inscriptions...")
    
    plt.figure(figsize=(14, 8))
    ax1 = sns.countplot(x='Jour_Inscription', data=df, order=ordre_jours, palette='crest')
    
    # Ajouter les nombres au-dessus des barres
    for p in ax1.patches:
        ax1.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=12)

    plt.title('Répartition des Inscriptions par Jour de la Semaine', fontsize=18, pad=20)
    plt.ylabel('Nombre d\'inscriptions', fontsize=14)
    plt.xlabel('Jour de la semaine', fontsize=14)
    plt.xticks(rotation=0)
    plt.tight_layout()

    # Sauvegarde du graphique
    output_repartition_path = os.path.join(output_dir, 'repartition_inscriptions_par_jour.png')
    plt.savefig(output_repartition_path, dpi=300)
    print(f"\nGraphique de répartition sauvegardé avec succès dans : {output_repartition_path}")

    # --- 4. GRAPHIQUE 2 : RÉPARTITION DES PLAINTES PAR JOUR D'INSCRIPTION ---
    print("\nGénération du graphique de la répartition des plaintes par jour d'inscription...")

    # Agréger le nombre de plaintes par jour d'inscription
    plaintes_par_jour = df.groupby('Jour_Inscription')['Plainte'].sum().reset_index()

    plt.figure(figsize=(14, 8))
    ax2 = sns.barplot(x='Jour_Inscription', y='Plainte', data=plaintes_par_jour, order=ordre_jours, palette='Reds_d')

    # Ajouter les nombres au-dessus des barres
    for p in ax2.patches:
        # Ne pas annoter si la hauteur est 0
        if p.get_height() > 0:
            ax2.annotate(f'{int(p.get_height())}', 
                         (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=12)

    plt.title('Répartition des Plaintes par Jour d\'Inscription', fontsize=18, pad=20)
    plt.ylabel('Nombre de Plaintes', fontsize=14)
    plt.xlabel('Jour de la semaine', fontsize=14)
    plt.xticks(rotation=0)
    plt.tight_layout()

    # Sauvegarde du graphique
    output_plaintes_path = os.path.join(output_dir, 'repartition_plaintes_par_jour.png')
    plt.savefig(output_plaintes_path, dpi=300)
    print(f"\nGraphique des plaintes sauvegardé avec succès dans : {output_plaintes_path}")

except FileNotFoundError:
    print(f"ERREUR : Le fichier '{file_path}' est introuvable. Assurez-vous qu'il existe bien.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")