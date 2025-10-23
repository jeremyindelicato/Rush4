import pandas as pd
import os

def segmenter_depenses(file_path=r'c:\Users\Utilisateur\Desktop\Rush 04\Rush4\Camp_Market_final.csv'):
    """
    Ajoute une colonne de segmentation des dépensiers à un fichier CSV de marketing
    en se basant sur le montant total des dépenses.

    La segmentation est définie comme suit :
    - Les 559 clients qui dépensent le plus sont des "Grand Dépensier".
    - Les 567 clients qui dépensent le moins sont des "Petits Dépensier".
    - Tous les autres sont des "Moyens Dépensier".

    Args:
        file_path (str): Le chemin vers le fichier CSV à traiter.
    """
    try:
        # 1. Charger le fichier CSV
        df = pd.read_csv(file_path)
        print("Fichier CSV chargé avec succès.")

        # 2. S'assurer que la colonne 'Total_Depense' existe
        if 'Total_Depense' not in df.columns:
            print("ERREUR : La colonne 'Total_Depense' est introuvable dans le fichier.")
            return

        # 3. Trier le DataFrame par 'Total_Depense' pour identifier les segments
        # ascending=False pour avoir les plus grandes dépenses en premier
        df_sorted = df.sort_values(by='Total_Depense', ascending=False)

        # 4. Définir le nombre de clients pour chaque segment
        nb_grands_depensiers = 559
        nb_petits_depensiers = 567

        # 5. Identifier les index pour chaque segment
        grands_depensiers_indices = df_sorted.head(nb_grands_depensiers).index
        petits_depensiers_indices = df_sorted.tail(nb_petits_depensiers).index

        # 6. Créer la nouvelle colonne et assigner les segments
        df['Segmentation_Dépensier'] = 'Moyens_Depensier' # Valeur par défaut
        df.loc[grands_depensiers_indices, 'Segmentation_Dépensier'] = 'Grand_Depensier'
        df.loc[petits_depensiers_indices, 'Segmentation_Dépensier'] = 'Petits_Depensier'
        
        print("\nSegmentation terminée. Voici la répartition :")
        print(df['Segmentation_Dépensier'].value_counts())

        # 7. Sauvegarder le DataFrame modifié dans le même fichier
        df.to_csv(file_path, index=False)
        print(f"\nLe fichier '{os.path.basename(file_path)}' a été mis à jour avec la colonne 'Segmentation_Dépensier'.")

    except FileNotFoundError:
        print(f"ERREUR : Le fichier '{file_path}' est introuvable. Veuillez vérifier le chemin.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

# --- Exécution du script ---
if __name__ == '__main__':
    segmenter_depenses()