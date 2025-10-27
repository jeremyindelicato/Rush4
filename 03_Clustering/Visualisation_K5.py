"""
Visualisation de la Segmentation Client K=5
Graphiques professionnels avec légendes complètes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
import warnings
warnings.filterwarnings('ignore')

# Configuration visuelle
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("Set2")
plt.rcParams['figure.figsize'] = (14, 10)
plt.rcParams['font.size'] = 11

print("=" * 80)
print("🎨 VISUALISATION SEGMENTATION K=5")
print("=" * 80)

# ============================================================================
# CHARGEMENT ET PRÉPARATION DES DONNÉES
# ============================================================================

print("\n📊 Chargement des données...")
df = pd.read_csv('../01_Data/ML_DataSet.csv')
print(f"✅ {len(df)} clients chargés")

# Sélectionner les features pour le clustering
features_clustering = [
    # Démographiques
    'Revenu', 'Age_Inscription', 'Total_Enfants',

    # Comportement d'achat
    'Total_Depense', 'Total_Achats', 'Depense_Moy_Par_Achat',

    # Préférences produits
    'Achat_Vins', 'Achat_Viandes', 'Achat_Poissons', 'Achat_Produits_Or',

    # Canaux d'achat
    'Achats_En_Ligne', 'Achats_Catalogue', 'Achats_En_Magasin',

    # Engagement
    'Visites_Web_Mois', 'Engagement_Web', 'Sensibilite_Promo',

    # Historique campagnes
    'Total_Campagnes_Acceptees', 'Taux_Reponse_Historique'
]

X_cluster = df[features_clustering].copy()

# Gérer les valeurs manquantes
imputer = SimpleImputer(strategy='median')
X_cluster = pd.DataFrame(
    imputer.fit_transform(X_cluster),
    columns=features_clustering,
    index=X_cluster.index
)

# Normalisation
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_cluster)

print("✅ Données préparées et normalisées")

# ============================================================================
# CLUSTERING K=5
# ============================================================================

print("\n🔍 Clustering K=5...")
kmeans_k5 = KMeans(n_clusters=5, random_state=42, n_init=20)
clusters = kmeans_k5.fit_predict(X_scaled)
df['Cluster'] = clusters

print("✅ Clustering terminé")
print(f"\nDistribution des clusters :")
print(df['Cluster'].value_counts().sort_index())

# ============================================================================
# NOMMAGE DES CLUSTERS AVEC LÉGENDES MARKETING
# ============================================================================

cluster_names = {
    0: "Familles Budget-Conscientes\n(47% - Revenus modestes, peu dépensiers)",
    1: "Connaisseurs Aisés\n(20% - Revenus élevés, acheteurs réguliers)",
    2: "Familles Équilibrées\n(27% - Classe moyenne, fort engagement digital)",
    3: "VIP Ultra-Réactifs\n(6% - Segment premium, 63% taux réponse)",
    4: "Outlier\n(0.04% - Anomalie)"
}

cluster_names_short = {
    0: "Familles Budget",
    1: "Connaisseurs Aisés",
    2: "Familles Équilibrées",
    3: "VIP Ultra-Réactifs",
    4: "Outlier"
}

cluster_colors = {
    0: '#FF6B6B',  # Rouge (attention)
    1: '#4ECDC4',  # Turquoise (bon segment)
    2: '#95E1D3',  # Vert clair (potentiel)
    3: '#FFD93D',  # Or (premium)
    4: '#AAAAAA'   # Gris (à ignorer)
}

# ============================================================================
# GRAPHIQUE 1 : VUE D'ENSEMBLE PCA 2D
# ============================================================================

print("\n📈 Création des visualisations...")

# PCA pour projection 2D
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_scaled)

fig = plt.figure(figsize=(20, 12))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# Graphique principal : PCA
ax_main = fig.add_subplot(gs[:2, :2])

# Filtrer l'outlier pour un meilleur affichage
df_plot = df[df['Cluster'] != 4].copy()
X_pca_plot = X_pca[df['Cluster'] != 4]

for cluster_id in sorted(df_plot['Cluster'].unique()):
    mask = df_plot['Cluster'] == cluster_id
    cluster_data = df_plot[mask]

    # Scatter plot
    ax_main.scatter(
        X_pca_plot[mask.values, 0],
        X_pca_plot[mask.values, 1],
        c=cluster_colors[cluster_id],
        label=cluster_names[cluster_id],
        s=100,
        alpha=0.6,
        edgecolors='white',
        linewidth=0.5
    )

    # Ajouter le centroïde
    centroid_x = X_pca_plot[mask.values, 0].mean()
    centroid_y = X_pca_plot[mask.values, 1].mean()
    ax_main.scatter(
        centroid_x, centroid_y,
        c=cluster_colors[cluster_id],
        s=500,
        marker='*',
        edgecolors='black',
        linewidth=2,
        zorder=10
    )

    # Étiquette du cluster
    ax_main.annotate(
        cluster_names_short[cluster_id],
        (centroid_x, centroid_y),
        fontsize=10,
        fontweight='bold',
        ha='center',
        va='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor=cluster_colors[cluster_id],
                  edgecolor='black', linewidth=2, alpha=0.9)
    )

ax_main.set_xlabel(f'Composante Principale 1 ({pca.explained_variance_ratio_[0]:.1%} variance)',
                   fontsize=13, fontweight='bold')
ax_main.set_ylabel(f'Composante Principale 2 ({pca.explained_variance_ratio_[1]:.1%} variance)',
                   fontsize=13, fontweight='bold')
ax_main.set_title('🎯 Segmentation Client K=5 - Vue d\'Ensemble PCA',
                  fontsize=16, fontweight='bold', pad=20)
ax_main.legend(loc='upper left', fontsize=10, frameon=True, shadow=True)
ax_main.grid(True, alpha=0.3)

# ============================================================================
# GRAPHIQUE 2 : DISTRIBUTION DES CLUSTERS (camembert)
# ============================================================================

ax_pie = fig.add_subplot(gs[0, 2])

sizes = df[df['Cluster'] != 4]['Cluster'].value_counts().sort_index()
colors_pie = [cluster_colors[i] for i in sorted(sizes.index)]
labels_pie = [f"{cluster_names_short[i]}\n{sizes[i]} clients\n({sizes[i]/len(df)*100:.1f}%)"
              for i in sorted(sizes.index)]

wedges, texts, autotexts = ax_pie.pie(
    sizes,
    labels=labels_pie,
    colors=colors_pie,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 9, 'fontweight': 'bold'}
)

# Améliorer les pourcentages
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_fontweight('bold')

ax_pie.set_title('📊 Répartition des Segments', fontsize=12, fontweight='bold', pad=10)

# ============================================================================
# GRAPHIQUE 3 : PROFIL FINANCIER PAR CLUSTER
# ============================================================================

ax_finance = fig.add_subplot(gs[1, 2])

cluster_profiles = df[df['Cluster'] != 4].groupby('Cluster').agg({
    'Revenu': 'mean',
    'Total_Depense': 'mean',
    'Total_Achats': 'mean'
}).reset_index()

x_pos = np.arange(len(cluster_profiles))
width = 0.25

bars1 = ax_finance.bar(x_pos - width, cluster_profiles['Revenu']/1000, width,
                       label='Revenu Moyen (K€)', color='#4ECDC4', alpha=0.8)
bars2 = ax_finance.bar(x_pos, cluster_profiles['Total_Depense'], width,
                       label='Dépenses (€)', color='#FFD93D', alpha=0.8)
bars3 = ax_finance.bar(x_pos + width, cluster_profiles['Total_Achats']*50, width,
                       label='Achats (x50)', color='#95E1D3', alpha=0.8)

ax_finance.set_xlabel('Segments', fontsize=11, fontweight='bold')
ax_finance.set_ylabel('Montants', fontsize=11, fontweight='bold')
ax_finance.set_title('💰 Profil Financier par Segment', fontsize=12, fontweight='bold')
ax_finance.set_xticks(x_pos)
ax_finance.set_xticklabels([cluster_names_short[i] for i in cluster_profiles['Cluster']],
                           rotation=45, ha='right', fontsize=9)
ax_finance.legend(fontsize=9)
ax_finance.grid(True, alpha=0.3, axis='y')

# Ajouter les valeurs sur les barres
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax_finance.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.0f}',
                       ha='center', va='bottom', fontsize=8)

# ============================================================================
# GRAPHIQUE 4 : TAUX DE RÉPONSE PAR CLUSTER
# ============================================================================

ax_response = fig.add_subplot(gs[2, 0])

response_rates = df[df['Cluster'] != 4].groupby('Cluster')['Reponse_Derniere_Campagne'].mean() * 100

bars = ax_response.barh(
    [cluster_names_short[i] for i in response_rates.index],
    response_rates.values,
    color=[cluster_colors[i] for i in response_rates.index],
    alpha=0.8,
    edgecolor='black',
    linewidth=1.5
)

ax_response.set_xlabel('Taux de Réponse (%)', fontsize=11, fontweight='bold')
ax_response.set_title('📧 Réactivité Marketing par Segment', fontsize=12, fontweight='bold')
ax_response.grid(True, alpha=0.3, axis='x')

# Ajouter les valeurs
for i, (bar, value) in enumerate(zip(bars, response_rates.values)):
    ax_response.text(value + 1, i, f'{value:.1f}%',
                     va='center', fontsize=10, fontweight='bold')

# Ligne de moyenne
mean_response = response_rates.mean()
ax_response.axvline(mean_response, color='red', linestyle='--', linewidth=2,
                   label=f'Moyenne : {mean_response:.1f}%', alpha=0.7)
ax_response.legend(fontsize=9)

# ============================================================================
# GRAPHIQUE 5 : ENGAGEMENT DIGITAL
# ============================================================================

ax_digital = fig.add_subplot(gs[2, 1])

digital_engagement = df[df['Cluster'] != 4].groupby('Cluster').agg({
    'Visites_Web_Mois': 'mean',
    'Engagement_Web': 'mean'
}).reset_index()

x_pos = np.arange(len(digital_engagement))
width = 0.35

bars1 = ax_digital.bar(x_pos - width/2, digital_engagement['Visites_Web_Mois'], width,
                       label='Visites Web/Mois', color='#4ECDC4', alpha=0.8)
bars2 = ax_digital.bar(x_pos + width/2, digital_engagement['Engagement_Web']*10, width,
                       label='Engagement Web (x10)', color='#FFD93D', alpha=0.8)

ax_digital.set_xlabel('Segments', fontsize=11, fontweight='bold')
ax_digital.set_ylabel('Score', fontsize=11, fontweight='bold')
ax_digital.set_title('💻 Engagement Digital par Segment', fontsize=12, fontweight='bold')
ax_digital.set_xticks(x_pos)
ax_digital.set_xticklabels([cluster_names_short[i] for i in digital_engagement['Cluster']],
                           rotation=45, ha='right', fontsize=9)
ax_digital.legend(fontsize=9)
ax_digital.grid(True, alpha=0.3, axis='y')

# ============================================================================
# GRAPHIQUE 6 : PROFIL DÉMOGRAPHIQUE
# ============================================================================

ax_demo = fig.add_subplot(gs[2, 2])

demo_profile = df[df['Cluster'] != 4].groupby('Cluster').agg({
    'Age_Inscription': 'mean',
    'Total_Enfants': 'mean'
}).reset_index()

# Scatter avec taille selon le nombre de clients
sizes_scatter = df[df['Cluster'] != 4]['Cluster'].value_counts().sort_index()

for i, row in demo_profile.iterrows():
    cluster_id = int(row['Cluster'])
    ax_demo.scatter(
        row['Age_Inscription'],
        row['Total_Enfants'],
        s=sizes_scatter[cluster_id]*2,
        c=cluster_colors[cluster_id],
        alpha=0.7,
        edgecolors='black',
        linewidth=2,
        label=cluster_names_short[cluster_id]
    )

    # Ajouter étiquette
    ax_demo.annotate(
        cluster_names_short[cluster_id],
        (row['Age_Inscription'], row['Total_Enfants']),
        fontsize=9,
        fontweight='bold',
        xytext=(5, 5),
        textcoords='offset points'
    )

ax_demo.set_xlabel('Âge Moyen (ans)', fontsize=11, fontweight='bold')
ax_demo.set_ylabel('Nombre d\'Enfants Moyen', fontsize=11, fontweight='bold')
ax_demo.set_title('👨‍👩‍👧 Profil Démographique par Segment', fontsize=12, fontweight='bold')
ax_demo.legend(fontsize=8, loc='upper right')
ax_demo.grid(True, alpha=0.3)

plt.suptitle('🎯 ANALYSE COMPLÈTE - SEGMENTATION CLIENT K=5',
             fontsize=18, fontweight='bold', y=0.995)

plt.tight_layout()
plt.savefig('Written_Results/Segmentation_K5_Complete.png', dpi=300, bbox_inches='tight')
print("✅ Graphique principal sauvegardé : Written_Results/Segmentation_K5_Complete.png")
plt.show()

# ============================================================================
# GRAPHIQUE BONUS : HEATMAP DÉTAILLÉE DES PROFILS
# ============================================================================

print("\n📊 Création de la heatmap détaillée...")

fig, ax = plt.subplots(figsize=(16, 8))

# Calculer les moyennes par cluster
heatmap_data = df[df['Cluster'] != 4].groupby('Cluster').agg({
    'Revenu': 'mean',
    'Total_Depense': 'mean',
    'Total_Achats': 'mean',
    'Age_Inscription': 'mean',
    'Total_Enfants': 'mean',
    'Visites_Web_Mois': 'mean',
    'Total_Campagnes_Acceptees': 'mean',
    'Reponse_Derniere_Campagne': lambda x: x.mean() * 100,
    'Engagement_Web': lambda x: x.mean() * 100,
    'Achat_Vins': 'mean',
    'Achat_Viandes': 'mean',
    'Depense_Moy_Par_Achat': 'mean'
})

# Normaliser pour la heatmap (0-1)
heatmap_normalized = (heatmap_data - heatmap_data.min()) / (heatmap_data.max() - heatmap_data.min())

# Créer la heatmap
sns.heatmap(
    heatmap_normalized.T,
    annot=False,
    cmap='RdYlGn',
    cbar_kws={'label': 'Score Normalisé (0 = Min, 1 = Max)'},
    linewidths=0.5,
    linecolor='gray',
    ax=ax
)

# Personnaliser les labels
ax.set_xticklabels([cluster_names_short[i] for i in heatmap_normalized.index],
                   rotation=45, ha='right', fontsize=11, fontweight='bold')
ax.set_yticklabels([
    'Revenu', 'Dépenses Totales', 'Nombre Achats', 'Âge', 'Enfants',
    'Visites Web/Mois', 'Campagnes Acceptées', 'Taux Réponse (%)',
    'Engagement Web (%)', 'Achats Vins', 'Achats Viandes', 'Panier Moyen'
], rotation=0, fontsize=10)

ax.set_title('🔥 Heatmap des Profils - Segmentation K=5\n(Plus c\'est vert, plus la valeur est élevée)',
             fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('Written_Results/Segmentation_K5_Heatmap.png', dpi=300, bbox_inches='tight')
print("✅ Heatmap sauvegardée : Written_Results/Segmentation_K5_Heatmap.png")
plt.show()

# ============================================================================
# TABLEAU RÉCAPITULATIF
# ============================================================================

print("\n" + "=" * 80)
print("📋 TABLEAU RÉCAPITULATIF DES SEGMENTS K=5")
print("=" * 80)

summary = df[df['Cluster'] != 4].groupby('Cluster').agg({
    'ID_Client': 'count',
    'Revenu': 'mean',
    'Total_Depense': 'mean',
    'Total_Achats': 'mean',
    'Age_Inscription': 'mean',
    'Total_Enfants': 'mean',
    'Reponse_Derniere_Campagne': lambda x: f"{x.mean()*100:.1f}%",
    'Engagement_Web': lambda x: f"{x.mean()*100:.1f}%"
})

summary.columns = ['Nb Clients', 'Revenu Moyen', 'Dépenses Moy.', 'Achats/an',
                   'Âge Moyen', 'Enfants', 'Taux Réponse', 'Engagement Web']

# Ajouter les noms
summary.index = [cluster_names_short[i] for i in summary.index]

print(summary.to_string())

# Ajouter pourcentages
print("\n📊 Répartition :")
for cluster_id in sorted(df[df['Cluster'] != 4]['Cluster'].unique()):
    count = (df['Cluster'] == cluster_id).sum()
    pct = count / len(df) * 100
    print(f"  {cluster_names_short[cluster_id]:<30} : {count:>4} clients ({pct:>5.1f}%)")

print("\n" + "=" * 80)
print("✅ ANALYSE K=5 TERMINÉE")
print("=" * 80)
print("\n📁 Fichiers générés :")
print("  • Written_Results/Segmentation_K5_Complete.png")
print("  • Written_Results/Segmentation_K5_Heatmap.png")
print("\n💡 Ces graphiques sont prêts à être intégrés dans vos présentations !")
