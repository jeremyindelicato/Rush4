# 🎯 Projet Rush 4 - Analyse Marketing & Segmentation Client

**Formation :** Bootcamp DATA Pro Max
**Durée :** 6 jours en groupe de 5
**Objectif :** Analyse approfondie des données marketing pour optimiser les campagnes et comprendre le comportement client

---

## 📋 Table des Matières

1. [Vue d'Ensemble du Projet](#-vue-densemble-du-projet)
2. [Structure du Projet](#-structure-du-projet)
3. [01 - Données](#01---données)
4. [02 - Prédiction (Machine Learning)](#02---prédiction-machine-learning)
5. [03 - Clustering (Segmentation Client)](#03---clustering-segmentation-client)
6. [04 - Recommandations Marketing](#04---recommandations-marketing)
7. [05 - Dashboard Analytique](#05---dashboard-analytique)
8. [Installation et Lancement](#-installation-et-lancement)
9. [Technologies Utilisées](#-technologies-utilisées)
10. [Résultats Clés](#-résultats-clés)

---

## 🎯 Vue d'Ensemble du Projet

Ce projet analyse les données marketing d'une entreprise pour :
- **Prédire** quels clients répondront aux campagnes futures
- **Segmenter** les clients en groupes homogènes
- **Optimiser** le ROI des campagnes marketing
- **Visualiser** les comportements d'achat via un dashboard interactif

### 🎓 Contexte Pédagogique

Ce projet fait partie du **Rush 4** du Bootcamp DATA Pro Max, un exercice intensif de 6 jours permettant de mettre en pratique :
- L'analyse exploratoire de données (EDA)
- Le Machine Learning (classification)
- Le clustering (segmentation non supervisée)
- La visualisation de données
- La communication de résultats business

---

## 📁 Structure du Projet

```
Projet 4 - Marketing/
├── 01_Data/                          # Données sources
│   ├── Camp_Market.csv              # Dataset original
│   ├── Camp_Market_final.csv        # Dataset avec feature engineering
│   └── ML_DataSet.csv               # Dataset prêt pour le ML
│
├── 02_Prediction/                    # Modèle de prédiction ML
│   ├── app_prediction.py            # Application Streamlit de prédiction
│   ├── xgboost_champion_optimized.pkl # Modèle XGBoost entraîné
│   ├── ML_suivi.ipynb               # Notebook d'entraînement
│   ├── requirements.txt             # Dépendances Python
│   ├── GUIDE_LANCEMENT.md           # Guide d'installation
│   └── README_ML.md                 # Documentation du modèle
│
├── 03_Clustering/                    # Segmentation client
│   ├── ML_Clustering.ipynb          # Notebook de clustering K-Means
│   ├── ML_Clustering_Optimisation.ipynb # Optimisation (K=4)
│   ├── Visualisation_K5.py          # Visualisations PCA
│   └── Data_Results/                # Résultats et graphiques
│
├── 04_Recommendations/               # Stratégies marketing
│   └── STRATEGIES_MARKETING.md      # Recommandations par segment
│
├── 05_Dashboard_Analytics/           # Dashboard interactif
│   ├── dashboard.py                 # Application Streamlit principale
│   ├── data/                        # Données pour le dashboard
│   ├── requirements.txt             # Dépendances Python
│   ├── README.md                    # Guide d'utilisation
│   └── RAPPORT_ANALYSE_MARKETING.md # Rapport d'analyse détaillé
│
└── README_Rush4_Global.md           # Ce fichier
```

---

## 01 - Données

### 📊 Dataset Principal : `Camp_Market.csv`

**Contenu :**
- **2237 clients** avec 49 variables
- Données démographiques (âge, revenu, éducation, statut marital)
- Historique d'achats par catégorie (vins, viandes, fruits, etc.)
- Comportement d'achat (en ligne, catalogue, magasin)
- Réponses aux campagnes marketing (6 campagnes)

### 🔧 Feature Engineering

**Variables créées :**
- `Total_Depense` : Somme des achats toutes catégories
- `Depense_Moy_Par_Achat` : Valeur moyenne du panier
- `Ratio_Vins`, `Ratio_Viandes` : Préférences produits
- `Taux_Reponse_Historique` : Réactivité aux campagnes passées
- `Engagement_Web` : Proportion d'achats en ligne
- Variables encodées (statut marital, éducation, âge)

---

## 02 - Prédiction (Machine Learning)

### 🎯 Objectif
Prédire si un client répondra positivement à la prochaine campagne marketing.

### 🤖 Modèle Champion : XGBoost Optimisé

**Performances :**
- **ROC-AUC : 0.8947** (excellente discrimination)
- **Accuracy : 87.72%**
- **F1-Score : 0.6259**
- **Precision : 0.57** (classe répondants)
- **Recall : 0.69** (classe répondants)

### 📈 Variables les Plus Importantes (Top 5)

1. **Jours Dernier Achat** (0.918) - La récence est cruciale
2. **Total Campagnes Acceptées** (0.806) - Historique de réponse
3. **Visites Web / Mois** (0.575) - Engagement digital
4. **Statut Marital** (0.463) - Influence démographique
5. **Ratio Vins** (0.445) - Préférence produit

### 🚀 Application Web de Prédiction

Une application Streamlit interactive permet de :
- **Prédire individuellement** : Entrer le profil d'un client et obtenir une prédiction
- **Prédiction en batch** : Télécharger un CSV et prédire pour plusieurs clients
- **Consulter les statistiques** : Voir les performances du modèle

**Lancer l'application :**
```bash
cd 02_Prediction
source .venv/bin/activate
streamlit run app_prediction.py
```

Voir [GUIDE_LANCEMENT.md](02_Prediction/GUIDE_LANCEMENT.md) pour l'installation complète.

---

## 03 - Clustering (Segmentation Client)

### 🎯 Objectif
Segmenter les clients en groupes homogènes pour personnaliser les stratégies marketing.

### 🔍 Méthode : K-Means avec PCA

**Approche :**
1. **Réduction de dimensionnalité** : PCA pour visualiser les clusters
2. **Clustering K-Means** : Testé avec K=3, 4, 5, 6
3. **Optimisation** : K=4 retenu (meilleur score silhouette)

### 📊 4 Segments Identifiés (K=4)

#### 🌟 Segment 1 : "VIP Ultra-Réactifs" (6% - 128 clients)
- **Revenu moyen** : 79,724€/an
- **Dépenses** : 1,616€ (16x la moyenne !)
- **Taux de réponse** : **63.3%** ⭐
- **Profil** : Sans enfants, 42 ans, gros acheteurs de vins premium
- **Stratégie** : Programme VIP exclusif, événements privés

#### 💎 Segment 2 : "Connaisseurs Aisés" (20% - 449 clients)
- **Revenu moyen** : 75,829€/an
- **Dépenses** : 1,341€
- **Taux de réponse** : 18.3%
- **Profil** : Acheteurs traditionnels, préfèrent le magasin physique
- **Stratégie** : Offres premium, fidélisation

#### 🌐 Segment 3 : "Familles Équilibrées" (27% - 601 clients)
- **Revenu moyen** : 57,294€/an
- **Dépenses** : 735€
- **Taux de réponse** : 12.5%
- **Profil** : Classe moyenne, fort engagement digital
- **Stratégie** : E-commerce, promotions ciblées

#### 💰 Segment 4 : "Familles Budget-Conscientes" (47% - 1059 clients)
- **Revenu moyen** : 34,858€/an
- **Dépenses** : 99€
- **Taux de réponse** : 9.1%
- **Profil** : Familles avec enfants, sensibles au prix
- **Stratégie** : Promotions, produits d'entrée de gamme

### 📈 Visualisation PCA

Le graphique PCA (voir image) montre :
- **Composante Principale 1 (42.6% variance)** : Pouvoir d'achat
- **Composante Principale 2 (10.7% variance)** : Comportement d'achat
- **Total : 53.3% de l'information** préservée dans la visualisation 2D

Les 4 clusters sont clairement séparés, validant la qualité de la segmentation.

---

## 04 - Recommandations Marketing

Basé sur l'analyse du clustering et des prédictions, des stratégies marketing détaillées ont été élaborées pour chaque segment.

**Consultez :**
- [STRATEGIES_MARKETING.md](04_Recommendations/STRATEGIES_MARKETING.md) : Stratégies complètes par segment

### 🎯 Recommandations Clés

1. **Cibler prioritairement les VIP** (63% de taux de réponse)
2. **Optimiser le budget** en évitant les segments à faible ROI
3. **Personnaliser les offres** selon les préférences produits
4. **Renforcer l'engagement digital** pour les Familles Équilibrées
5. **Proposer des promotions** pour les Familles Budget

---

## 05 - Dashboard Analytique

### 📊 Dashboard Streamlit Interactif

Un dashboard permet d'explorer les données de manière interactive avec :

#### Page 1 : Analyse du Client Type
- **Répartition du panier moyen** par catégorie de produits
- **Indicateurs clés** : Revenu moyen, valeur du panier, dépense moyenne
- **Analyse des canaux d'achat** : En ligne, catalogue, magasin (avec taux de promotion)
- **Visites web** par segment de dépensier

#### Page 2 : Influence des Campagnes
- **Performance des 6 campagnes** : Nombre de réponses par campagne
- **KPIs financiers** : ROI, coût, revenu, bénéfice par campagne
- **Seuil de rentabilité** : 611 réponses nécessaires
- **Analyse de récence** : Jours depuis le dernier achat par segment

### 🎨 Filtres Interactifs

Le dashboard permet de filtrer par :
- Statut marital
- Catégorie d'âge
- Niveau d'éducation
- Nombre d'enfants/ados
- Segment de dépensier (Petits/Moyens/Grands)

### 🚀 Lancer le Dashboard

```bash
cd 05_Dashboard_Analytics
source .venv/bin/activate
streamlit run dashboard.py
```

Voir [README.md](05_Dashboard_Analytics/README.md) pour l'installation complète.

---

## 🛠️ Installation et Lancement

### Prérequis

- **Python 3.9+**
- **Homebrew** (pour macOS, requis pour libomp)

### Installation Globale

```bash
# Cloner le projet
cd "Projet 4 - Marketing"

# Installer libomp (macOS uniquement, requis pour XGBoost)
/opt/homebrew/bin/brew install libomp
# Si nécessaire : brew link libomp --overwrite --force
```

### Lancer le Dashboard Analytics

```bash
cd 05_Dashboard_Analytics
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run dashboard.py
```

### Lancer l'Application de Prédiction

```bash
cd 02_Prediction
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app_prediction.py
```

**Note :** Voir les guides d'installation détaillés dans chaque dossier pour les instructions spécifiques.

---

## 🧰 Technologies Utilisées

### Langages & Frameworks
- **Python 3.9** : Langage principal
- **Streamlit** : Applications web interactives
- **Jupyter Notebook** : Analyse exploratoire et modélisation

### Machine Learning
- **XGBoost** : Modèle de prédiction (classification)
- **Scikit-learn** : Preprocessing, clustering K-Means, métriques
- **SHAP** : Interprétabilité du modèle

### Visualisation
- **Plotly** : Graphiques interactifs
- **Matplotlib / Seaborn** : Visualisations statiques
- **PCA** : Réduction de dimensionnalité pour visualisation

### Data Processing
- **Pandas** : Manipulation de données
- **NumPy** : Calculs numériques
- **Joblib** : Sérialisation du modèle

---

## 🏆 Résultats Clés

### 🎯 Prédiction
- **ROC-AUC de 0.8947** : Excellent modèle de classification
- **Top 3 des variables importantes** : Récence, historique de réponse, engagement web
- **Application déployée** : Interface web pour prédictions en temps réel

### 📊 Segmentation
- **4 segments distincts** identifiés avec K-Means
- **53.3% de variance** expliquée par les 2 premières composantes PCA
- **Segment VIP** avec 63% de taux de réponse identifié

### 💰 Optimisation Marketing
- **Seuil de rentabilité** : 611 réponses nécessaires par campagne
- **ROI calculé** par campagne et par segment
- **Stratégies personnalisées** élaborées pour chaque segment

### 📈 Dashboard
- **Interface interactive** avec filtres multiples
- **2 pages d'analyse** : Panier moyen + Campagnes
- **Visualisations dynamiques** avec Plotly

---

## 📝 Livrables

### Documents
- ✅ Notebooks Python commentés (ML, Clustering)
- ✅ Applications Streamlit (Dashboard, Prédiction)
- ✅ Documentation technique (README, guides)
- ✅ Rapport d'analyse marketing
- ✅ Stratégies marketing par segment

### Code
- ✅ Code versionné avec Git
- ✅ Structure modulaire et organisée
- ✅ Requirements.txt pour chaque module
- ✅ Scripts de lancement automatisés

### Présentations
- Soutenance orale : 15 min présentation + 10 min échanges
- Support visuel : Graphiques, métriques, recommandations

---

## 🎓 Compétences Développées

- **Analyse de données** : EDA approfondie, feature engineering
- **Machine Learning** : Classification, optimisation d'hyperparamètres, interprétabilité
- **Clustering** : Segmentation non supervisée, PCA, K-Means
- **Visualisation** : Dashboards interactifs, graphiques business
- **Communication** : Traduction des résultats techniques en insights business
- **Développement** : Applications web, gestion d'environnements, documentation

---

## 👥 Équipe & Contact

**Projet :** Rush 4 - Segmentation Clients
**Formation :** Bootcamp DATA Pro Max
**Durée :** 6 jours en groupe de 5
**Date :** Octobre 2025

---

## 📚 Pour Aller Plus Loin

### Améliorations Futures

1. **Modèle de prédiction**
   - Tester d'autres algorithmes (LightGBM, CatBoost)
   - Optimiser davantage les hyperparamètres
   - Ajouter plus de features (interactions)

2. **Clustering**
   - Tester d'autres méthodes (DBSCAN, Hierarchical)
   - Affiner la segmentation avec des sous-segments
   - Analyse temporelle de l'évolution des segments

3. **Dashboard**
   - Ajouter des prédictions en temps réel
   - Intégrer un système de recommandation produit
   - Tableau de bord de suivi ROI en temps réel

4. **Déploiement**
   - Containeriser avec Docker
   - Déployer sur cloud (Streamlit Cloud, Heroku)
   - API REST pour intégration avec CRM

---

**🎉 Projet terminé avec succès !**

Pour toute question, consultez les README spécifiques de chaque module ou les guides d'installation.
