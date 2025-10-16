# 🤖 Projet Machine Learning - Prédiction de Réponse aux Campagnes Marketing

## 📊 Vue d'ensemble

**Objectif :** Construire un modèle prédictif pour prédire la probabilité qu'un client réponde à une campagne marketing future.

**Dataset :** ML_DataSet.csv
**Clients :** 2237
**Features :** 49 variables
**Target :** Reponse_Derniere_Campagne (0/1)
**Déséquilibre :** 85.1% classe 0 / 14.9% classe 1 (ratio 5.7:1)

---

## 🔧 Modifications Apportées au Dataset

### ✅ Nouvelles Variables Créées (10 features)

#### 1. **Variables Encodées**
| Variable Originale | Variable Encodée | Description |
|-------------------|------------------|-------------|
| Statut_Marital | Statut_Marital_Encode | single=0, couple=1 |
| Jour_Inscription | Jour_Inscription_Encode | Friday=0, Monday=1, ..., Wednesday=6 |
| Categorie_Age | Categorie_Age_Encode | Jeune(18-25)=0, Adulte(26-35)=1, Adulte confirmé(36-50)=2, Senior(51-65)=3, Vétéran(65+)=4 |

**Distribution Statut_Marital :**
- Single : 794 clients (35.5%)
- Couple : 1443 clients (64.5%)

**Distribution Catégorie_Age :**
- Jeune (18-25) : 116 clients (5.2%)
- Adulte (26-35) : 434 clients (19.4%)
- Adulte confirmé (36-50) : 989 clients (44.2%)
- Senior (51-65) : 638 clients (28.5%)
- Vétéran (65+) : 60 clients (2.7%)

#### 2. **Variables d'Engagement Client**

| Variable | Formule | Description |
|----------|---------|-------------|
| Total_Enfants | Enfants_Maison + Ados_Maison | Nombre total d'enfants au foyer |
| A_Des_Enfants | 1 si Total_Enfants > 0 else 0 | Indicateur binaire de présence d'enfants |

#### 3. **Ratios de Préférence Produit**

| Variable | Formule | Description |
|----------|---------|-------------|
| Ratio_Vins | Achat_Vins / Total_Depense | Part des dépenses en vins |
| Ratio_Viandes | Achat_Viandes / Total_Depense | Part des dépenses en viandes |

#### 4. **Métriques Comportementales**

| Variable | Formule | Description |
|----------|---------|-------------|
| Taux_Reponse_Historique | Total_Campagnes_Acceptees / 5 | Taux de réponse aux campagnes passées (0 à 1) |
| Engagement_Web | Achats_En_Ligne / Total_Achats | Proportion d'achats en ligne |
| Sensibilite_Promo | Achats_Promotions / Total_Achats | Sensibilité aux promotions |

---

## 📋 Variables pour le Modèle ML

### ✅ Variables Sélectionnées (36 features)

**Démographiques (7) :**
- Revenu, Revenu_Moyen_Mois
- Age_Inscription
- Niveau_Education_Encode
- Statut_Marital_Encode
- Categorie_Age_Encode
- Jour_Inscription_Encode

**Structure Familiale (2) :**
- Total_Enfants
- A_Des_Enfants

**Comportement d'Achat (9) :**
- Total_Depense
- Total_Achats
- Depense_Moy_Par_Achat
- Jours_Dernier_Achat (récence)
- Achats_En_Ligne
- Achats_Catalogue
- Achats_En_Magasin
- Achats_Promotions
- Visites_Web_Mois

**Préférences Produits (8) :**
- Achat_Vins
- Achat_Fruits
- Achat_Viandes
- Achat_Poissons
- Achat_Produits_Sucres
- Achat_Produits_Or
- Ratio_Vins
- Ratio_Viandes

**Historique Marketing (6) :**
- Reponse_Campagne_1
- Reponse_Campagne_2
- Reponse_Campagne_3
- Reponse_Campagne_4
- Reponse_Campagne_5
- Total_Campagnes_Acceptees

**Métriques Calculées (4) :**
- Taux_Reponse_Historique
- Engagement_Web
- Sensibilite_Promo
- Plainte

### ❌ Variables Exclues (13)

**Raisons d'exclusion :**
- **ID_Client** : Identifiant unique sans valeur prédictive
- **Annee_Naissance** : Redondant avec Age_Inscription
- **Date_Inscription** : Format date, redondant avec Jour_Inscription_Encode
- **Niveau_Education** : Version texte, remplacée par Niveau_Education_Encode
- **Statut_Marital** : Version texte, remplacée par Statut_Marital_Encode
- **Statut_Marital_Texte** : Doublon
- **Jour_Inscription** : Version texte, remplacée par Jour_Inscription_Encode
- **Categorie_Age** : Version texte, remplacée par Categorie_Age_Encode
- **Cout_Contact_Z** : Constante (toujours 3)
- **Revenus_Z** : Constante (toujours 11)
- **Enfants_Maison** : Remplacé par Total_Enfants
- **Ados_Maison** : Remplacé par Total_Enfants
- **Reponse_Derniere_Campagne** : Variable cible (TARGET)

---

## 🎯 Stack Technique Recommandée

### Bibliothèques Python
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost imbalanced-learn shap
```

### Modèles à Implémenter

#### 1. **Régression Logistique** (Baseline)
- Simple et interprétable
- `class_weight='balanced'` pour gérer le déséquilibre
- Nécessite normalisation (StandardScaler)

#### 2. **Random Forest** (Robuste)
- Robuste aux outliers
- `class_weight='balanced'`
- Feature importance automatique

#### 3. **XGBoost** ⭐ (Champion attendu)
- Meilleure performance attendue
- `scale_pos_weight=5.7` pour gérer le déséquilibre
- SHAP values pour interprétabilité

---

## 📊 Métriques d'Évaluation

### Priorités pour le Marketing

1. **ROC-AUC** : Capacité globale de discrimination
2. **Precision** : Éviter de cibler des clients non intéressés (coût)
3. **Recall** : Capturer un maximum de clients potentiels (opportunité)
4. **F1-Score** : Équilibre entre precision et recall

### Validation
- **Stratified K-Fold** (5-fold) : Maintient les proportions de classes
- **Train/Test Split** : 80/20 avec stratification

---

## 📂 Fichiers du Projet

### Fichiers de Données
- **Camp_Market.csv** : Dataset original (non modifié)
- **Camp_Market_final.csv** : Dataset avec features engineering de base
- **ML_DataSet.csv** : Dataset optimisé pour ML avec tous les encodages ✅

### Notebooks
- **ML_suivi.ipynb** : Notebook de suivi du projet avec structure complète ✅

### Documentation
- **README_ML.md** : Ce fichier (documentation complète)

---

## 🚀 Prochaines Étapes

### Phase 1 : Exploration ✅
- [x] Analyse de la variable cible
- [x] Vérification du déséquilibre
- [x] Sélection des features
- [x] Analyse de corrélation

### Phase 2 : Modélisation (À faire)
- [ ] Entraîner Régression Logistique
- [ ] Entraîner Random Forest
- [ ] Entraîner XGBoost
- [ ] Comparer les performances
- [ ] Analyser feature importance

### Phase 3 : Optimisation (À faire)
- [ ] Optimisation des hyperparamètres (GridSearchCV)
- [ ] Tester SMOTE pour le rééquilibrage
- [ ] Créer des features supplémentaires
- [ ] Analyser SHAP values pour XGBoost

### Phase 4 : Production (À faire)
- [ ] Sélectionner le meilleur modèle
- [ ] Calibrer les probabilités
- [ ] Créer un seuil de décision optimal
- [ ] Préparer la présentation des résultats

---

## 💡 Insights Attendus

### Questions Business à Répondre

1. **Quels sont les profils clients les plus réceptifs aux campagnes ?**
   - Analyse des features les plus importantes
   - Segmentation par catégorie d'âge, revenu, comportement

2. **Quel budget marketing optimal ?**
   - Calculer le ROI en ciblant uniquement les clients à forte probabilité
   - Comparer avec une campagne "broadcast"

3. **Quels canaux privilégier ?**
   - Analyser l'importance de Engagement_Web, Achats_Catalogue, etc.

4. **Quelle est la sensibilité aux promotions ?**
   - Rôle de Sensibilite_Promo dans les prédictions

---

## 📞 Contact et Support

**Projet :** Rush 4 - Segmentation Clients
**Formation :** Bootcamp DATA Pro Max
**Durée :** 6 jours en groupe de 5
**Outil :** Jupyter Notebook + Python

**Livrables attendus :**
- Notebook Python avec analyses + modèles + clustering
- Soutenance orale : 15 min présentation + 10 min échanges

---

## 📝 Notes Techniques

### Gestion du Déséquilibre (Ratio 5.7:1)

**Stratégie adoptée :**
1. Utiliser `class_weight='balanced'` pour Logistic Regression et Random Forest
2. Utiliser `scale_pos_weight=5.7` pour XGBoost
3. Validation avec `StratifiedKFold`
4. Métriques focus sur F1-Score et ROC-AUC (pas seulement accuracy)

**Alternative possible :**
- SMOTE (Synthetic Minority Over-sampling Technique)
- Undersampling de la classe majoritaire
- Ensemble methods avec différentes stratégies

### Feature Engineering Clés

**Ratios créés :**
- Permettent de capturer les **préférences relatives** plutôt qu'absolues
- Exemple : Un client dépensant 100€ dont 50€ en vin a un Ratio_Vins de 0.5
- Plus informatif que le montant absolu pour la prédiction

**Engagement métrics :**
- Captent le **comportement digital** vs traditionnel
- Important pour cibler les bonnes canaux de communication

**Historique de réponse :**
- Le **meilleur prédicteur** du comportement futur
- Taux_Reponse_Historique devrait être dans le top 3 des features importantes

---

**Date de création :** 2025-01-16
**Dernière mise à jour :** 2025-01-16
**Version :** 1.0
