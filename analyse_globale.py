import pandas as pd
import os

# --- 1. CHARGEMENT DES DONNÉES ---
file_path = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\Camp_Market_final.csv'

try:
    df = pd.read_csv(file_path)
    print(f"Fichier '{file_path}' chargé avec succès.\n")
    
    print("="*50)
    print("   RAPPORT GLOBAL DES TENDANCES CLIENTS")
    print("="*50)

    # --- 2. TENDANCES SUR LES DONNÉES NUMÉRIQUES CLÉS ---
    print("\n--- 1. Tendances Numériques (Moyennes, Médianes...) ---\n")
    
    # Pour le revenu, on exclut les valeurs à 0 pour une moyenne plus juste
    revenu_stats = df[df['Revenu'] > 0]['Revenu'].describe()
    
    print(f"Âge moyen des clients : {df['Age_Inscription'].mean():.1f} ans")
    print(f"Revenu annuel moyen (hors revenus nuls) : {revenu_stats['mean']:,.2f} €".replace(',', ' '))
    print(f"Dépense totale moyenne par client : {df['Total_Depense'].mean():,.2f} €".replace(',', ' '))
    print(f"Dépense totale (tous clients confondus) : {df['Total_Depense'].sum():,.2f} €".replace(',', ' '))
    print(f"Panier moyen (dépense moyenne par achat) : {df['Depense_Moy_Par_Achat'].mean():,.2f} €".replace(',', ' '))
    print(f"Nombre moyen d'achats total par client : {df['Total_Achats'].mean():.1f}")
    print(f"Nombre de jours moyen depuis le dernier achat : {df['Jours_Dernier_Achat'].mean():.1f} jours")

    # --- 3. TENDANCES SUR LES DONNÉES CATÉGORIELLES ---
    print("\n--- 2. Répartition par Catégorie ---\n")

    # Niveau d'éducation
    print("Répartition par Niveau d'Éducation :")
    education_dist = df['Niveau_Education'].value_counts(normalize=True) * 100
    for level, percentage in education_dist.items():
        print(f"  - {level}: {percentage:.1f}%")

    # Statut Marital
    print("\nRépartition par Statut Marital :")
    # On regroupe les statuts pour plus de clarté
    statuts_couple = ['Married', 'Together']
    df['Type_Relation'] = df['Statut_Marital_Texte'].apply(lambda x: 'En Couple' if x in statuts_couple else 'Seul')
    relation_dist = df['Type_Relation'].value_counts(normalize=True) * 100
    for status, percentage in relation_dist.items():
        print(f"  - {status}: {percentage:.1f}%")

    # Présence d'enfants
    print("\nRépartition par Type de Ménage :")
    df['Total_Enfants'] = df['Enfants_Maison'] + df['Ados_Maison']
    df['Type_Menage'] = df['Total_Enfants'].apply(lambda x: 'Avec Enfants/Ados' if x > 0 else 'Sans Enfants/Ados')
    menage_dist = df['Type_Menage'].value_counts(normalize=True) * 100
    for menage_type, percentage in menage_dist.items():
        print(f"  - {menage_type}: {percentage:.1f}%")

    # --- 4. TENDANCES SUR LES PRODUITS ET PLATEFORMES ---
    print("\n--- 3. Tendances d'Achat (Produits et Plateformes) ---\n")

    # Dépenses par produit
    print("Répartition des dépenses par catégorie de produit :")
    colonnes_produits = ['Achat_Vins', 'Achat_Viandes', 'Achat_Fruits', 'Achat_Poissons', 'Achat_Produits_Sucres', 'Achat_Produits_Or']
    total_depenses_produits = df[colonnes_produits].sum()
    total_depenses_global = total_depenses_produits.sum()
    produits_dist = (total_depenses_produits / total_depenses_global) * 100
    for produit, percentage in produits_dist.sort_values(ascending=False).items():
        nom_produit = produit.replace('Achat_', '').replace('_', ' ')
        print(f"  - {nom_produit}: {percentage:.1f}%")

    # Achats par plateforme
    print("\nRépartition des achats par plateforme :")
    colonnes_plateformes = ['Achats_En_Ligne', 'Achats_Catalogue', 'Achats_En_Magasin']
    total_achats_plateformes = df[colonnes_plateformes].sum()
    total_achats_global = total_achats_plateformes.sum()
    plateformes_dist = (total_achats_plateformes / total_achats_global) * 100
    for plateforme, percentage in plateformes_dist.sort_values(ascending=False).items():
        nom_plateforme = plateforme.replace('Achats_', '').replace('_', ' ')
        print(f"  - {nom_plateforme}: {percentage:.1f}%")

    # --- 5. TENDANCES SUR LES CAMPAGNES ET PLAINTES ---
    print("\n--- 4. Tendances sur l'Engagement et la Satisfaction ---\n")

    # On suppose que les colonnes Cout_Contact_Z et Revenus_Z sont constantes
    cout_par_contact = df['Cout_Contact_Z'].iloc[0]
    revenu_par_conversion = df['Revenus_Z'].iloc[0]

    # Taux de conversion et ROI par campagne
    colonnes_campagnes = ['Reponse_Campagne_1', 'Reponse_Campagne_2', 'Reponse_Campagne_3', 'Reponse_Campagne_4', 'Reponse_Campagne_5']
    print("Performance par campagne :")
    for campagne in colonnes_campagnes:
        nom_campagne = campagne.replace('Reponse_', '').replace('_', ' ')
        
        taux_conversion = df[campagne].mean() * 100
        
        # Calcul du ROI pour la campagne
        reponses_campagne = df[campagne].sum()
        cout_campagne = len(df) * cout_par_contact
        revenu_campagne = reponses_campagne * revenu_par_conversion
        roi_campagne = ((revenu_campagne - cout_campagne) / cout_campagne) * 100 if cout_campagne > 0 else 0
        
        print(f"  - {nom_campagne}: Taux de conversion = {taux_conversion:.1f}%, ROI = {roi_campagne:.2f}%")
        
    print(f"\nTaux de réponse global à la dernière campagne : {df['Reponse_Derniere_Campagne'].mean() * 100:.1f}%")
    
    total_reponses = df['Reponse_Derniere_Campagne'].sum()
    cout_total = len(df) * cout_par_contact
    revenu_total = total_reponses * revenu_par_conversion
    roi_global = ((revenu_total - cout_total) / cout_total) * 100
    print(f"\nROI de la dernière campagne : {roi_global:.2f}%")

    # Taux de plainte
    taux_plainte = df['Plainte'].mean() * 100
    print(f"Taux de plainte global : {taux_plainte:.2f}%")
    
    print("\n" + "="*50)
    print("   SEGMENTATION ET COMPORTEMENT DES CLIENTS")
    print("="*50)

    # --- 6. SEGMENTATION PAR NIVEAU DE DÉPENSE ---
    print("\n--- 5. Profil des Segments de Clients par Dépense ---\n")

    # Créer 3 segments basés sur les quantiles de dépense totale
    quantiles = df['Total_Depense'].quantile([0.25, 0.75]).to_dict()
    q_low = quantiles[0.25]
    q_high = quantiles[0.75]

    def assign_segment(x):
        if x <= q_low:
            return 'Petits Dépensiers'
        elif x <= q_high:
            return 'Dépensiers Moyens'
        else:
            return 'Grands Dépensiers (VIP)'

    df['Segment_Depense'] = df['Total_Depense'].apply(assign_segment)

    # Analyser chaque segment
    for segment in ['Petits Dépensiers', 'Dépensiers Moyens', 'Grands Dépensiers (VIP)']:
        df_segment = df[df['Segment_Depense'] == segment]
        print(f"--- Profil du segment : {segment} ---\n")

        # Caractéristiques démographiques
        print(f"  Nombre de clients : {len(df_segment)}")
        print(f"  Revenu annuel moyen : {df_segment[df_segment['Revenu'] > 0]['Revenu'].mean():,.0f} €".replace(',', ' '))
        print(f"  Âge moyen : {df_segment['Age_Inscription'].mean():.1f} ans")
        
        # Comportement d'achat
        print(f"  Dépense totale moyenne : {df_segment['Total_Depense'].mean():,.0f} €".replace(',', ' '))
        
        # Produit préféré (basé sur la part des dépenses)
        total_depenses_segment = df_segment[colonnes_produits].sum()
        produit_prefere = (total_depenses_segment / total_depenses_segment.sum()).idxmax().replace('Achat_', '')
        print(f"  Catégorie de produit préférée : {produit_prefere}")

        # Engagement et Rentabilité
        total_reponses_segment = df_segment['Reponse_Derniere_Campagne'].sum()
        taux_conversion_segment = df_segment['Reponse_Derniere_Campagne'].mean() * 100
        print(f"  Taux de conversion (dernière campagne) : {taux_conversion_segment:.1f}%")

        # Calcul du ROI pour le segment
        cout_segment = len(df_segment) * cout_par_contact
        revenu_segment = total_reponses_segment * revenu_par_conversion
        roi_segment = ((revenu_segment - cout_segment) / cout_segment) * 100
        print(f"  ROI du segment (dernière campagne) : {roi_segment:.2f}%")
        print("-" * 40 + "\n")

    # --- 7. SEGMENTATION PAR CLASSE D'ÂGE ---
    print("\n" + "="*50)
    print("   ROI PAR CLASSE D'ÂGE (DERNIÈRE CAMPAGNE)")
    print("="*50)

    # Définir un ordre logique pour les catégories d'âge
    ordre_age = ['Jeune (18-25)', 'Adulte (26-35)', 'Adulte confirmé (36-50)', 'Senior (51-65)', 'Vétéran (65+)']
    df['Categorie_Age'] = pd.Categorical(df['Categorie_Age'], categories=ordre_age, ordered=True)

    print("\n--- 6. Profil des Segments de Clients par Âge ---\n")
    
    roi_par_age = []
    for age_group in ordre_age:
        df_age_segment = df[df['Categorie_Age'] == age_group]
        
        if len(df_age_segment) == 0:
            continue

        reponses_segment = df_age_segment['Reponse_Derniere_Campagne'].sum()
        cout_segment = len(df_age_segment) * cout_par_contact
        revenu_segment = reponses_segment * revenu_par_conversion
        roi_age_segment = ((revenu_segment - cout_segment) / cout_segment) * 100
        
        roi_par_age.append(roi_age_segment)
        
        print(f"--- Profil du segment : {age_group} ---")
        print(f"  Nombre de clients : {len(df_age_segment)}")
        print(f"  Taux de conversion : {df_age_segment['Reponse_Derniere_Campagne'].mean() * 100:.1f}%")
        print(f"  ROI : {roi_age_segment:.2f}%\n")

    # --- 8. CONCLUSION : QUELLE SEGMENTATION EST LA PLUS PERTINENTE ? ---
    print("\n" + "="*50)
    print("   CONCLUSION : ÂGE OU REVENU, QUEL EST LE PLUS PERTINENT ?")
    print("="*50)
    print("\nPour prédire la rentabilité (ROI) d'une campagne, la segmentation par niveau de dépense (qui est directement liée au revenu) est **nettement plus pertinente** que la segmentation par âge.")
    print("\nPourquoi ?")
    print("1. **Forte Corrélation** : Le ROI augmente de manière très claire et prévisible avec le niveau de dépense. Il passe de fortement négatif pour les 'Petits Dépensiers' à très positif pour les 'Grands Dépensiers (VIP)'.")
    print("2. **Faible Variation par Âge** : Le ROI varie peu entre les différentes classes d'âge. Bien que les 'Seniors' et 'Vétérans' soient légèrement plus rentables, la différence n'est pas aussi marquée. Toutes les tranches d'âge ont un ROI négatif ou proche de zéro.")
    print("\n**Recommandation** : Pour optimiser vos campagnes, il est plus efficace de cibler les clients en fonction de leur comportement d'achat et de leur revenu plutôt que de leur âge.")

    print("\n" + "="*50)
    print("   FIN DU RAPPORT")
    print("="*50)

except FileNotFoundError:
    print(f"ERREUR : Le fichier '{file_path}' est introuvable. Assurez-vous qu'il existe bien.")
except Exception as e:
    print(f"Une erreur inattendue est survenue : {e}")