# Rush4 - Projet Marketing Analytics

## Description
Projet d'analyse de données marketing avec tableaux de bord interactifs pour analyser le comportement des clients et l'efficacité des campagnes marketing.

## Installation

### Prérequis
- Python 3.9 ou supérieur
- Un environnement virtuel (`.venv`)

### Installation des dépendances

1. Activez l'environnement virtuel et installez les packages nécessaires :
```bash
source .venv/bin/activate
pip install streamlit pandas plotly
```

## Utilisation

### Lancer le Dashboard Panier Moyen

Le dashboard principal permet d'analyser la composition du panier moyen et l'influence des campagnes marketing.

```bash
source .venv/bin/activate && streamlit run dashboard.py
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

- `dashboard_panier_moyen.py` : Dashboard principal Streamlit
- `Camp_Market_final.csv` : Fichier de données
- Scripts d'analyse Python (analyse_*.py)
- Dossiers de graphiques générés

## Données

Le fichier `Camp_Market_final.csv` contient les données clients et leurs comportements d'achat.
