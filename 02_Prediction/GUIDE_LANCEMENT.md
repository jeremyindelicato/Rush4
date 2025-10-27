# 🚀 Guide de Lancement - Application de Prédiction Marketing

## 📋 Prérequis

- Python 3.9 ou supérieur
- Les fichiers suivants doivent être présents :
  - `app_prediction.py`
  - `xgboost_champion_optimized.pkl` (modèle entraîné)
  - `requirements.txt`

---

## 🔧 Installation

### Option 1 : Avec environnement virtuel (Recommandé)

#### Étape 1 : Créer l'environnement virtuel

```bash
cd 02_Prediction
python3 -m venv .venv
```

#### Étape 2 : Activer l'environnement virtuel

```bash
source .venv/bin/activate
```

#### Étape 3 : Installer les dépendances

```bash
pip install -r requirements.txt
```

#### Étape 4 : Installer libomp (requis pour XGBoost sur macOS)

**IMPORTANT pour les utilisateurs macOS** : XGBoost nécessite la bibliothèque OpenMP.

Si vous avez Homebrew :
```bash
brew install libomp
```

Si vous n'avez pas Homebrew, installez-le d'abord :
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Option 2 : Installation globale

```bash
pip3 install -r requirements.txt
```

Puis installer libomp (macOS) :
```bash
brew install libomp
```

---

## 🚀 Lancement de l'Application

### 🎯 Méthode Recommandée : Script de Lancement Automatique

Si vous rencontrez l'erreur XGBoost libomp, utilisez le script de lancement qui résout automatiquement le problème :

```bash
cd 02_Prediction
./lancer_app_fix.sh
```

**Note** : Le script vous demandera votre mot de passe système une seule fois pour créer un lien symbolique vers libomp.

### Méthode Manuelle : Avec environnement virtuel

Depuis le répertoire `02_Prediction` :

```bash
source .venv/bin/activate
streamlit run app_prediction.py
```

### Méthode Alternative : Sans environnement virtuel

Option 1 - Depuis le répertoire racine du projet :
```bash
python3 -m streamlit run 02_Prediction/app_prediction.py
```

Option 2 - Depuis le répertoire `02_Prediction` :
```bash
cd 02_Prediction
python3 -m streamlit run app_prediction.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`

---

## 📊 Fonctionnalités de l'Application

L'application propose **3 modes** :

### 1. 🧑 Prédiction Individuelle
- Entrez manuellement le profil d'un client
- Obtenez une prédiction instantanée
- Visualisez la probabilité de réponse
- Recommandations personnalisées

### 2. 📋 Prédiction en Batch
- Téléchargez un fichier CSV avec plusieurs clients
- Obtenez des prédictions pour tous les clients en une fois
- Exportez les résultats en CSV
- Statistiques agrégées et visualisations

### 3. 📈 Statistiques du Modèle
- Performances du modèle (ROC-AUC: 0.8947)
- Variables les plus importantes
- Métriques détaillées

---

## 🛠️ Dépannage

### Problème : "streamlit: command not found"

**Solution** : Utilisez `python3 -m streamlit` au lieu de `streamlit` :
```bash
python3 -m streamlit run app_prediction.py
```

### Problème : "XGBoost Library could not be loaded" (macOS)

**Cause** : La bibliothèque OpenMP (libomp) n'est pas installée.

**Solution** :
```bash
brew install libomp
```

Si vous n'avez pas Homebrew :
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install libomp
```

### Problème : "Model not found"

**Cause** : Le fichier `xgboost_champion_optimized.pkl` n'est pas dans le bon répertoire.

**Solution** : Assurez-vous que le fichier `.pkl` est dans le même dossier que `app_prediction.py`

### Problème : Erreur lors du chargement du fichier CSV en batch

**Cause** : Le format du CSV ne correspond pas aux colonnes attendues.

**Solution** : Utilisez le fichier `exemple_clients_test.csv` comme référence pour le format.

---

## 📁 Structure des Fichiers

```
02_Prediction/
├── .venv/                              # Environnement virtuel (créé après installation)
├── .gitignore                          # Fichiers à ignorer par Git
├── app_prediction.py                   # Application Streamlit principale
├── xgboost_champion_optimized.pkl      # Modèle ML entraîné
├── requirements.txt                    # Dépendances Python
├── exemple_clients_test.csv            # Exemple de fichier pour batch
├── GUIDE_LANCEMENT.md                  # Ce fichier
├── GUIDE_EXECUTION.md                  # Guide original
└── README_ML.md                        # Documentation du modèle ML
```

---

## 📦 Librairies Utilisées

- **streamlit** : Framework web pour l'interface
- **pandas** : Manipulation des données
- **numpy** : Calculs numériques
- **plotly** : Visualisations interactives
- **joblib** : Chargement du modèle
- **scikit-learn** : Preprocessing et imputation
- **xgboost** : Modèle de prédiction

---

## 🎯 Performances du Modèle

- **Accuracy** : 87.72%
- **ROC-AUC** : 0.8947
- **F1-Score** : 0.6259
- **Precision** : 0.57 (classe répondants)
- **Recall** : 0.69 (classe répondants)

---

## 💡 Conseils d'Utilisation

### Pour une prédiction individuelle
1. Remplissez tous les champs du formulaire
2. Assurez-vous que les valeurs sont réalistes
3. Consultez les "Points Positifs" et "Points d'Attention" pour comprendre la prédiction

### Pour une prédiction en batch
1. Utilisez `exemple_clients_test.csv` comme modèle
2. Assurez-vous que toutes les colonnes nécessaires sont présentes
3. Téléchargez les résultats pour analyse ultérieure

### Interprétation des probabilités
- **≥ 70%** : Priorité haute - Contacter immédiatement
- **50-70%** : Bon prospect - Inclure dans la campagne
- **30-50%** : Prospect incertain - Cibler si budget disponible
- **< 30%** : Faible potentiel - Ne pas contacter

---

## 📞 Support

Pour plus d'informations sur le modèle ML, consultez :
- `README_ML.md` : Documentation complète du modèle
- `GUIDE_EXECUTION.md` : Guide d'exécution original

---

**Dernière mise à jour** : 2025-10-27
**Version** : 1.0
