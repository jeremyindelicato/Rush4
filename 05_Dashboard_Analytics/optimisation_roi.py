import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def main():
    # --- 1. CHARGEMENT ET PRÉPARATION DES DONNÉES ---
    file_path = r'05_Dashboard_Analytics/data/Dataset_Dashboard_Analytics.csv'
    output_dir = r'c:\Users\Utilisateur\Desktop\Epitech\Rush_4\graph_optimisation'
    os.makedirs(output_dir, exist_ok=True)

    try:
        df = pd.read_csv(file_path)
        print(f"Fichier '{file_path}' chargé avec succès.\n")
    except FileNotFoundError:
        print(f"ERREUR : Le fichier '{file_path}' est introuvable.")
        return
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")
        return

    print("="*60)
    print("   SIMULATION D'OPTIMISATION DU ROI MARKETING")
    print("="*60)

    # --- 2. SEGMENTATION DES CLIENTS ---
    quantiles = df['Total_Depense'].quantile([0.25, 0.75]).to_dict()
    q_low = quantiles[0.25]
    q_high = quantiles[0.75]

    def assign_segment(x):
        if x <= q_low: return 'Petits Dépensiers'
        elif x <= q_high: return 'Dépensiers Moyens'
        else: return 'Grands Dépensiers (VIP)'

    df['Segment_Depense'] = df['Total_Depense'].apply(assign_segment)
    
    # --- 3. CALCUL DE L'ÉTAT ACTUEL (ROI PAR SEGMENT) ---
    print("\n--- 1. Analyse de la situation actuelle ---\n")

    cout_par_contact = df['Cout_Contact_Z'].iloc[0]
    revenu_par_conversion = df['Revenus_Z'].iloc[0]

    segments_data = {}
    for segment_name in ['Petits Dépensiers', 'Dépensiers Moyens', 'Grands Dépensiers (VIP)']:
        df_segment = df[df['Segment_Depense'] == segment_name]
        
        nb_clients = len(df_segment)
        total_reponses = df_segment['Total_Campagnes_Acceptees'].sum()
        
        cout_total = nb_clients * cout_par_contact
        revenu_total = total_reponses * revenu_par_conversion
        
        # Éviter la division par zéro si le coût est nul
        roi = ((revenu_total - cout_total) / cout_total) * 100 if cout_total > 0 else 0
        
        segments_data[segment_name] = {
            'nb_clients': nb_clients,
            'cout': cout_total,
            'revenu': revenu_total,
            'roi': roi,
            'taux_conversion': (total_reponses / nb_clients) * 100 if nb_clients > 0 else 0
        }
        print(f"Segment '{segment_name}': ROI actuel = {roi:.2f}%")

    # Calcul du ROI global actuel
    cout_actuel = sum(data['cout'] for data in segments_data.values())
    revenu_actuel = sum(data['revenu'] for data in segments_data.values())
    roi_actuel = ((revenu_actuel - cout_actuel) / cout_actuel) * 100
    print(f"\nROI Global Actuel : {roi_actuel:.2f}%\n")

    # --- 4. SIMULATION DE L'OPTIMISATION ---
    print("\n--- 2. Simulation de l'optimisation ---\n")
    print("Stratégie : Arrêter de cibler les 'Petits Dépensiers' et réallouer le budget aux 'Grands Dépensiers (VIP)'.\n")

    # Budget économisé en ne contactant pas les "Petits Dépensiers"
    budget_realloue = segments_data['Petits Dépensiers']['cout']
    
    # Nouveaux contacts possibles dans le segment VIP avec ce budget
    # On suppose que l'on contacte les clients VIP une fois de plus
    nb_clients_vip = segments_data['Grands Dépensiers (VIP)']['nb_clients']
    
    # Conversions supplémentaires attendues de ces nouveaux contacts
    conversions_supplementaires_vip = nb_clients_vip * (segments_data['Grands Dépensiers (VIP)']['taux_conversion'] / 100)
    
    # Revenu supplémentaire généré
    revenu_supplementaire = conversions_supplementaires_vip * revenu_par_conversion

    print(f"Budget économisé sur les 'Petits Dépensiers' : {budget_realloue:,.0f} €")
    print(f"Revenu supplémentaire estimé : {revenu_supplementaire:,.0f} €\n")

    # Calcul du nouveau ROI global
    # Le coût total ne change pas, il est juste réalloué
    cout_simule = cout_actuel
    # Le nouveau revenu est le revenu des segments rentables + le revenu supplémentaire
    revenu_simule = segments_data['Dépensiers Moyens']['revenu'] + segments_data['Grands Dépensiers (VIP)']['revenu'] + revenu_supplementaire
    roi_simule = ((revenu_simule - cout_simule) / cout_simule) * 100

    print(f"ROI Global Simulé : {roi_simule:.2f}%")
    print(f"Gain de ROI estimé : {roi_simule - roi_actuel:.2f} points")

    # --- 5. CRÉATION DU GRAPHIQUE COMPARATIF ---
    print("\nGénération du graphique comparatif...")
    
    df_roi_comparaison = pd.DataFrame({
        'Scénario': ['ROI Actuel', 'ROI Simulé'],
        'ROI (%)': [roi_actuel, roi_simule]
    })

    plt.figure(figsize=(10, 7))
    barplot = sns.barplot(x='Scénario', y='ROI (%)', data=df_roi_comparaison, palette=['#ff9999', '#66b3ff'])
    
    for p in barplot.patches:
        barplot.annotate(f'{p.get_height():.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=12, weight='bold')

    plt.title('Comparaison du ROI Marketing : Actuel vs. Simulé', fontsize=18, pad=20)
    plt.ylabel('Retour sur Investissement (%)', fontsize=12)
    plt.xlabel('Scénario', fontsize=12)
    plt.tight_layout()

    output_path = os.path.join(output_dir, 'simulation_roi.png')
    plt.savefig(output_path, dpi=300)
    print(f"\nGraphique de simulation sauvegardé avec succès dans : {output_path}")

if __name__ == '__main__':
    main()