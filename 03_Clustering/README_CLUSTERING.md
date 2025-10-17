# 🎯 Clustering - Segmentation Clients

## 📋 Vue d'Ensemble

Ce dossier contient l'analyse de clustering pour segmenter la base clients en groupes homogènes.

**Objectif :** Identifier des segments de clients avec des comportements similaires pour adapter les stratégies marketing.

---

## 📂 Contenu

| Fichier | Description | Status |
|---------|-------------|--------|
| **ML_Clustering.ipynb** | Notebook principal de clustering | ✅ Prêt |
| **cluster_profiles.csv** | Profils exportés des segments | (créé après exécution) |

---

## 🎯 Méthodes de Clustering

### 1. **K-Means** (Principal)
- Algorithme de partition basé sur les centroïdes
- Méthode du coude pour trouver K optimal
- Métriques : Silhouette Score, Davies-Bouldin, Calinski-Harabasz

### 2. **Hierarchical Clustering**
- Dendrogramme pour visualiser la hiérarchie
- Confirmation de K optimal
- Méthode : Ward linkage

### 3. **DBSCAN**
- Détection des outliers
- Clustering basé sur la densité
- Identification des clients atypiques

---

## 🚀 Comment Exécuter

### Option 1 : VSCode (Recommandé)
```bash
1. Ouvrez ML_Clustering.ipynb
2. Sélectionnez le kernel .venv
3. Run All (ou cellule par cellule)
```

### Option 2 : Jupyter Notebook
```bash
cd "03_Clustering"
jupyter notebook ML_Clustering.ipynb
```

**Temps d'exécution :** ~5-10 minutes

---

## 📊 Features Utilisées pour le Clustering

### Démographiques (3)
- `Revenu`
- `Age_Inscription`
- `Total_Enfants`

### Comportement d'Achat (6)
- `Total_Depense`
- `Total_Achats`
- `Depense_Moy_Par_Achat`
- `Achat_Vins`
- `Achat_Viandes`
- `Achat_Poissons`
- `Achat_Produits_Or`

### Canaux d'Achat (3)
- `Achats_En_Ligne`
- `Achats_Catalogue`
- `Achats_En_Magasin`

### Engagement (5)
- `Visites_Web_Mois`
- `Engagement_Web`
- `Sensibilite_Promo`
- `Total_Campagnes_Acceptees`
- `Taux_Reponse_Historique`

**Total : 18 features**

---

## 📈 Résultats Attendus

### K Optimal
D'après la méthode du coude et les métriques, **K=3 ou 4** devrait être optimal.

### Segments Typiques Attendus

**Exemple avec K=4 :**

1. **Segment VIP - Gros Dépensiers**
   - Revenu élevé (>70k€)
   - Dépense moyenne élevée (>1500€)
   - Taux de réponse élevé (~25-30%)
   - Préférence : Vins, Viandes premium

2. **Segment Digital - Jeunes Connectés**
   - 25-35 ans
   - Fort engagement web
   - Achats principalement en ligne
   - Sensibles aux promotions flash

3. **Segment Occasionnel - Faible Engagement**
   - Dépense faible (<300€)
   - Peu d'achats
   - Faible engagement
   - Taux de réponse bas (~5-10%)

4. **Segment Senior - Magasin Fidèle**
   - 50+ ans
   - Achats principalement en magasin
   - Fidèles mais peu digitaux
   - Taux de réponse moyen (~15%)

*(À ajuster selon vos résultats réels)*

---

## 📊 Visualisations Incluses

### 1. Méthode du Coude
- Graphique Inertia vs K
- Silhouette Score vs K
- Davies-Bouldin Score vs K
- Calinski-Harabasz Score vs K

### 2. Visualisation PCA 2D
- Projection des clients en 2 dimensions
- Coloration par cluster
- Centroïdes affichés

### 3. Taux de Réponse par Cluster
- Barplot du taux de réponse à la campagne
- Permet d'identifier les segments les plus réactifs

### 4. Heatmap des Profils
- Comparaison visuelle des clusters
- Toutes les features moyennes par cluster
- Valeurs normalisées (0-1)

### 5. Dendrogramme
- Hierarchical clustering
- Visualisation de la hiérarchie des clusters

---

## 💡 Comment Interpréter les Résultats

### Silhouette Score
- **0.7 - 1.0** : Excellent (clusters bien séparés)
- **0.5 - 0.7** : Bon
- **0.25 - 0.5** : Acceptable
- **< 0.25** : Mauvais (clusters se chevauchent)

### Davies-Bouldin Score
- **Plus bas = meilleur**
- Mesure la séparation entre clusters
- Valeur typique : 0.5 - 2.0

### Calinski-Harabasz Score
- **Plus élevé = meilleur**
- Ratio de la dispersion inter-cluster / intra-cluster
- Valeur typique : > 100

---

## 🎯 Utilisation des Résultats

### 1. Marketing Ciblé
Adapter les campagnes selon le segment :
- VIP → Offres premium
- Digital → Campagnes mobiles
- Occasionnel → Promotions agressives
- Senior → Contact téléphonique

### 2. Allocation Budget
Concentrer les ressources sur les segments à fort ROI

### 3. Prédiction par Segment
Entraîner un modèle XGBoost par segment (voir `../02_Prediction/`)

### 4. Monitoring
Suivre l'évolution des segments dans le temps

---

## 📝 Naming des Segments

**⚠️ Important :** Une fois les clusters analysés, donnez-leur des **noms parlants** dans la cellule dédiée du notebook.

**Exemples :**
```python
cluster_names = {
    0: "VIP - Gros Dépensiers",
    1: "Digital Natives - Jeunes Connectés",
    2: "Occasionnels - Faible Engagement",
    3: "Seniors Fidèles - Magasin"
}
```

Ces noms facilitent la communication avec les équipes marketing.

---

## 📤 Exports

Le notebook génère automatiquement :

1. **cluster_profiles.csv**
   - Moyennes de toutes les features par cluster
   - Utilisable pour rapports/dashboards

2. **ML_DataSet_with_Clusters.csv** (dans `../01_Data/`)
   - Dataset complet avec colonne `Cluster_KMeans`
   - Utilisable pour analyses supplémentaires

---

## 🔧 Ajustements Possibles

### Changer K
Modifiez la variable `K_OPTIMAL` dans la cellule correspondante :
```python
K_OPTIMAL = 3  # ou 4, 5, etc.
```

### Ajouter/Retirer des Features
Modifiez la liste `features_clustering` :
```python
features_clustering = [
    'Revenu',
    'Total_Depense',
    # ... ajoutez vos features
]
```

### Tester d'autres Algorithmes
- **DBSCAN** : Déjà inclus, ajustez `eps` et `min_samples`
- **Gaussian Mixture Models** : À ajouter si besoin
- **Mean Shift** : Pour clustering sans K prédéfini

---

## 🎓 Concepts Clés

### Normalisation
**CRUCIAL pour le clustering !**
- Les algorithmes sont sensibles à l'échelle
- StandardScaler : (x - mean) / std
- Toutes les features ont alors mean=0, std=1

### PCA (Principal Component Analysis)
- Réduction de dimension pour visualisation
- Les 2 premières composantes capturent 30-50% de la variance
- Permet de visualiser des données multidimensionnelles en 2D

### Centroïdes (K-Means)
- Point moyen de chaque cluster
- Utilisé pour assigner les nouveaux points

---

## 🐛 Troubleshooting

### Erreur : "No module named 'sklearn.cluster'"
```bash
pip install scikit-learn
```

### Le clustering prend trop de temps
- Réduisez le nombre de features
- Utilisez un échantillon du dataset

### Les clusters ne font pas sens
- Vérifiez la normalisation
- Testez un autre K
- Retirez les features non pertinentes

### Silhouette Score très bas (< 0.3)
- Peut-être que les données n'ont pas de structure naturelle en clusters
- Essayez d'autres valeurs de K
- Vérifiez s'il y a des outliers à retirer

---

## 📚 Prochaines Étapes

### Analyse Approfondie
1. Créer des visualisations radar pour chaque segment
2. Analyser l'évolution temporelle des segments
3. Croiser avec les données de campagnes

### Modélisation par Segment
1. Entraîner un XGBoost par cluster
2. Comparer avec le modèle global
3. Mesurer l'amélioration du ROC-AUC

### Stratégie Marketing
1. Définir des actions concrètes par segment
2. Estimer le ROI par segment
3. Créer des personas

---

## ✅ Checklist

Avant de passer à l'analyse approfondie :

- [ ] Notebook exécuté avec succès
- [ ] K optimal identifié (probablement 3-4)
- [ ] Silhouette Score > 0.3 (acceptable)
- [ ] Segments nommés avec des noms parlants
- [ ] Profils analysés et compris
- [ ] cluster_profiles.csv exporté
- [ ] Dataset avec clusters sauvegardé

---

**Dernière mise à jour :** 2025-10-17
**Projet :** Rush 4 - Segmentation Clients
**Responsable :** Machine Learning & Clustering
