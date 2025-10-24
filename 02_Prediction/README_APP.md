# 📊 Application de Prédiction - Campagne Marketing

## 🚀 Installation

### 1. Installer les dépendances

```bash
pip install streamlit plotly
```

Si vous n'avez pas déjà les autres bibliothèques :

```bash
pip install pandas numpy joblib scikit-learn xgboost
```

## 🎯 Lancer l'Application

### Étape 1 : Assurez-vous que le modèle est dans le bon dossier

Le fichier `xgboost_champion_optimized.pkl` doit être dans le même dossier que `app_prediction.py`.

### Étape 2 : Lancer l'application

```bash
cd "02_Prediction"
streamlit run app_prediction.py
```

L'application s'ouvrira automatiquement dans votre navigateur par défaut à l'adresse : `http://localhost:8501`

## 📱 Fonctionnalités

### 🧑 Mode 1 : Prédiction Individuelle

**Utilisation** : Tester un profil de client spécifique

**Comment faire** :
1. Sélectionnez "🧑 Prédiction Individuelle" dans la sidebar
2. Remplissez les informations du client :
   - **Démographiques** : Âge, statut marital, éducation, revenu, enfants
   - **Achats** : Montants dépensés par catégorie (vins, viandes, etc.)
   - **Engagement** : Visites web, achats catalogue/magasin/web, campagnes acceptées
3. Cliquez sur "🔮 PRÉDIRE LA RÉPONSE"

**Résultats affichés** :
- ✅/❌ Prédiction (OUI ou NON)
- 📊 Probabilité de réponse (0-100%)
- 🎯 Niveau de confiance
- 💡 Recommandation détaillée
- 🔍 Facteurs clés du profil

### 📋 Mode 2 : Prédiction en Batch

**Utilisation** : Analyser plusieurs clients à la fois

**Comment faire** :
1. Sélectionnez "📋 Prédiction en Batch"
2. Téléchargez votre fichier CSV avec les profils clients
3. Cliquez sur "🔮 LANCER LES PRÉDICTIONS"
4. Téléchargez les résultats au format CSV

**Format du fichier CSV** :
- Même structure que `ML_DataSet.csv`
- Minimum requis : les 36 features utilisées par le modèle

**Résultats fournis** :
- Tableau complet avec prédictions et probabilités
- Graphiques de distribution
- Statistiques globales
- Export CSV pour utilisation dans vos campagnes

### 📈 Mode 3 : Statistiques

**Utilisation** : Consulter les performances du modèle

**Informations disponibles** :
- Métriques de performance (Accuracy, ROC-AUC, F1-Score)
- Top 5 des variables importantes
- Détails des optimisations appliquées
- Hyperparamètres utilisés

## 🎨 Captures d'écran (à quoi ça ressemble)

L'interface propose :
- **Design moderne** avec Streamlit
- **Graphiques interactifs** avec Plotly
- **Navigation intuitive** via sidebar
- **Résultats visuels** : jauges, graphiques en camembert, histogrammes

## 💡 Cas d'Usage Pratiques

### Exemple 1 : Tester un nouveau client

```
Âge: 45 ans
Statut: Marié(e)
Revenu: 60000€
Vins: 500€
Visites web: 8/mois
Campagnes acceptées: 2
```

→ Le modèle prédit si ce client acceptera votre prochaine offre

### Exemple 2 : Préparer une campagne email

1. Uploadez votre liste de 5000 clients
2. Le modèle identifie les 1500 plus susceptibles de répondre
3. Téléchargez la liste filtrée
4. Envoyez vos emails uniquement à ces 1500 clients
5. **Résultat** : ROI optimisé !

## 🔧 Personnalisation

### Modifier les seuils de décision

Dans `app_prediction.py`, ligne ~180 environ :

```python
# Par défaut : seuil à 50%
if probabilite >= 0.5:
    # À contacter

# Pour être plus sélectif (70%) :
if probabilite >= 0.7:
    # À contacter
```

### Ajouter de nouvelles features

Si vous entraînez un nouveau modèle avec plus de variables :
1. Mettez à jour le dictionnaire `client_data` (ligne ~120)
2. Ajoutez les champs de formulaire correspondants

## ⚠️ Dépannage

### Problème : "Modèle non trouvé"

**Solution** : Vérifiez que `xgboost_champion_optimized.pkl` est dans le dossier `02_Prediction`

```bash
# Depuis le dossier racine du projet
ls 02_Prediction/xgboost_champion_optimized.pkl
```

### Problème : "Erreur lors de la prédiction"

**Solution** : Assurez-vous que votre CSV a les bonnes colonnes. Téléchargez le template :

Les colonnes requises sont les 36 features du modèle (voir `ML_DataSet.csv` pour référence)

### Problème : Port 8501 déjà utilisé

**Solution** : Utilisez un autre port

```bash
streamlit run app_prediction.py --server.port 8502
```

## 📞 Support

Pour toute question ou amélioration, consultez la documentation du modèle dans :
- `02_Prediction/Results/vertopal.com_ML_XGBoost.pdf`

## 🎓 Notes Techniques

- **Framework** : Streamlit 1.x
- **Modèle** : XGBoost (scikit-learn API)
- **Performances** : ROC-AUC 0.8947, F1-Score 0.6259
- **Entraînement** : 2237 clients, 36 features
- **Optimisation** : GridSearchCV, scale_pos_weight

---

**Développé pour** : Projet Marketing - Prédiction de Réponse aux Campagnes
**Date** : Octobre 2025
**Modèle** : XGBoost Optimisé
