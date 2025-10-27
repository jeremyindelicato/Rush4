# Rush4 - Projet Marketing Analytics

## Description
Projet d'analyse de données marketing avec tableaux de bord interactifs pour analyser le comportement des clients et l'efficacité des campagnes marketing.

## Installation

### Prérequis
- Python 3.9 ou supérieur

### Installation des dépendances

#### Option 1 : Avec environnement virtuel (Recommandé)

1. Créer un environnement virtuel :
```bash
cd 05_Dashboard_Analytics
python3 -m venv .venv
```

2. Activer l'environnement virtuel :
```bash
source .venv/bin/activate
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

#### Option 2 : Installation globale

```bash
pip3 install -r requirements.txt
```

Ou manuellement :
```bash
pip3 install streamlit==1.31.0 pandas==2.1.4 plotly==5.18.0
```

## Utilisation

### Lancer le Dashboard Panier Moyen

Le dashboard principal permet d'analyser la composition du panier moyen et l'influence des campagnes marketing.

#### Avec environnement virtuel

Depuis le répertoire 05_Dashboard_Analytics :
```bash
cd 05_Dashboard_Analytics
source .venv/bin/activate
streamlit run dashboard.py
```

#### Sans environnement virtuel

Option 1 - Depuis le répertoire racine du projet :
```bash
python3 -m streamlit run 05_Dashboard_Analytics/dashboard.py
```

Option 2 - Depuis le répertoire 05_Dashboard_Analytics :
```bash
cd 05_Dashboard_Analytics
python3 -m streamlit run dashboard.py
```

Le dashboard s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`

### Fonctionnalités du Dashboard

Le dashboard propose deux pages principales :

#### 1. Analyse du Panier Moyen
- Répartition des dépenses par catégorie de produits
- Indicateurs clés (revenu moyen, valeur du panier, etc.)
- Analyse des canaux d'achat (en ligne, catalogue, magasin)
- Analyse des visites web par segment de dépensier

#### 2. Influence des Campagnes
- Nombre de réponses par campagne marketing
- KPIs de participation et ROI
- Analyse de la récence par segment de dépensier
- Seuil de rentabilité

### Filtres disponibles
- Statut marital
- Catégorie d'âge
- Niveau d'éducation
- Nombre d'enfants/ados
- Segment de dépensier

## Structure du Projet

- `dashboard.py` : Dashboard principal Streamlit
- `data/Dataset_Dashboard_Analytics.csv` : Fichier de données
- `requirements.txt` : Librairies Python nécessaires
- `optimisation_roi.py` : Script d'optimisation du ROI
- `graph/` : Dossier des graphiques générés

## Données

Le fichier `data/Dataset_Dashboard_Analytics.csv` contient les données clients et leurs comportements d'achat.
