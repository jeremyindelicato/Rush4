# 🚀 Démarrage Rapide - Application de Prédiction

## ⚡ Lancement en 3 Étapes

### 1️⃣ Installer les dépendances (une seule fois)

```bash
pip install streamlit plotly
```

### 2️⃣ Lancer l'application

**Sur Mac/Linux** :
```bash
cd "02_Prediction"
./lancer_app.sh
```

**Sur Windows** :
Double-cliquez sur `lancer_app.bat`

**OU manuellement** :
```bash
cd "02_Prediction"
streamlit run app_prediction.py
```

### 3️⃣ Utiliser l'application

L'application s'ouvre automatiquement dans votre navigateur à : `http://localhost:8501`

---

## 📱 Modes Disponibles

### 🧑 Mode 1 : Prédiction Individuelle

**Pour tester UN client spécifique**

1. Cliquez sur "🧑 Prédiction Individuelle" dans la sidebar
2. Remplissez le formulaire avec les informations du client
3. Cliquez sur "🔮 PRÉDIRE LA RÉPONSE"
4. Obtenez instantanément :
   - ✅/❌ Si le client va répondre ou non
   - 📊 La probabilité (0-100%)
   - 💡 Une recommandation détaillée

**Exemple de profil à tester** :
```
Âge: 45 ans
Statut marital: Marié(e)
Éducation: Master
Revenu: 60000€
Nombre d'enfants: 1

Achats:
- Vins: 500€
- Viandes: 300€
- Poissons: 50€
- Fruits: 30€
- Produits sucrés: 20€
- Premium: 40€

Engagement:
- Visites web/mois: 7
- Jours depuis dernier achat: 30
- Achats catalogue: 3
- Achats magasin: 8
- Achats web: 5
- Campagnes acceptées: 2
```

→ **Résultat attendu** : Probabilité élevée (~70-80%) ✅

---

### 📋 Mode 2 : Prédiction en Batch

**Pour analyser PLUSIEURS clients à la fois**

1. Cliquez sur "📋 Prédiction en Batch"
2. Téléchargez votre fichier CSV
   - Vous pouvez utiliser `exemple_clients_test.csv` pour tester
3. Cliquez sur "🔮 LANCER LES PRÉDICTIONS"
4. Consultez les résultats :
   - Tableau complet avec prédictions
   - Graphiques de distribution
   - Statistiques globales
5. Téléchargez les résultats au format CSV

**Format du fichier CSV** :
- Utilisez la même structure que `ML_DataSet.csv`
- OU téléchargez le template `exemple_clients_test.csv`

---

### 📈 Mode 3 : Statistiques

**Pour consulter les performances du modèle**

- Accuracy : **87.72%**
- ROC-AUC : **0.8947**
- F1-Score : **0.6259**
- Top 5 variables importantes
- Détails des optimisations

---

## 💡 Cas d'Usage Pratiques

### Cas 1 : Préparer une Campagne Email

**Objectif** : Envoyer des emails uniquement aux clients susceptibles de répondre

1. Exportez votre base clients au format CSV
2. Uploadez-la dans le Mode Batch
3. Téléchargez les résultats
4. Filtrez pour ne garder que les clients avec "CONTACTER"
5. Envoyez vos emails à cette liste optimisée

**Résultat** : ROI maximisé, coûts réduits ✅

---

### Cas 2 : Identifier les Meilleurs Prospects

**Objectif** : Trouver les 100 meilleurs clients à appeler

1. Uploadez votre liste complète
2. Les résultats sont automatiquement triés par probabilité décroissante
3. Prenez les 100 premiers
4. Contactez-les en priorité

**Résultat** : Taux de conversion optimal ✅

---

### Cas 3 : Tester une Stratégie

**Objectif** : Comparer deux segments de clients

1. Créez deux profils types (Mode Individuel)
   - Profil A : Client jeune, actif, dépenses élevées
   - Profil B : Client âgé, peu actif, dépenses faibles
2. Comparez les probabilités
3. Adaptez votre stratégie marketing

**Résultat** : Segmentation data-driven ✅

---

## 🎯 Interprétation des Résultats

### Probabilités

| Probabilité | Signification | Action Recommandée |
|-------------|---------------|-------------------|
| **70-100%** | 🔥 Très élevée | ✅ Contacter en priorité |
| **50-70%** | ✅ Élevée | ✅ Inclure dans la campagne |
| **30-50%** | ⚠️ Moyenne | ⚠️ Cibler si budget disponible |
| **0-30%** | ❌ Faible | ❌ Ne pas contacter |

### Niveau de Confiance

- **Très Élevée** (≥70%) : Le modèle est très confiant
- **Élevée** (50-70%) : Bonne confiance
- **Moyenne** (30-50%) : Incertain
- **Faible** (<30%) : Peu probable

---

## 🔧 Dépannage Rapide

### ❌ "Modèle non trouvé"

**Solution** :
```bash
# Vérifier que le modèle existe
ls 02_Prediction/xgboost_champion_optimized.pkl
```

Si le fichier n'existe pas, vérifiez que vous avez bien exécuté le notebook `ML_XGBoost.ipynb` jusqu'à la fin.

---

### ❌ "Streamlit n'est pas installé"

**Solution** :
```bash
pip install streamlit plotly
```

---

### ❌ "Port 8501 déjà utilisé"

**Solution** :
```bash
# Utiliser un autre port
streamlit run app_prediction.py --server.port 8502
```

---

### ❌ "Erreur lors de la prédiction"

**Causes possibles** :
1. CSV mal formaté → Utilisez `exemple_clients_test.csv` comme template
2. Colonnes manquantes → Vérifiez que vous avez les 36 features requises
3. Valeurs aberrantes → Vérifiez que les valeurs sont cohérentes

---

## 📊 Fichiers Fournis

```
02_Prediction/
├── app_prediction.py              # Application Streamlit
├── xgboost_champion_optimized.pkl # Modèle entraîné
├── lancer_app.sh                  # Script de lancement (Mac/Linux)
├── lancer_app.bat                 # Script de lancement (Windows)
├── exemple_clients_test.csv       # Exemple de données pour test
├── README_APP.md                  # Documentation complète
└── DEMARRAGE_RAPIDE.md           # Ce fichier
```

---

## 🎓 Aller Plus Loin

### Personnaliser les Seuils

Par défaut, le seuil de décision est à **50%**. Vous pouvez le modifier dans le code :

```python
# Être plus sélectif (70%)
if probabilite >= 0.7:
    # À contacter

# Être plus inclusif (30%)
if probabilite >= 0.3:
    # À contacter
```

### Calculer le ROI

Ajoutez vos propres métriques business :

```python
COUT_CONTACT = 3  # 3€ par contact
GAIN_MOYEN = 50   # 50€ si conversion

# Calcul automatique du ROI dans les résultats
```

---

## 📞 Support

- **Documentation complète** : `README_APP.md`
- **Résultats du modèle** : `Results/vertopal.com_ML_XGBoost.pdf`
- **Notebook original** : `ML_XGBoost.ipynb`

---

## ✅ Checklist de Démarrage

- [ ] Python installé (3.8+)
- [ ] Dépendances installées (`pip install streamlit plotly`)
- [ ] Modèle présent (`xgboost_champion_optimized.pkl`)
- [ ] Application lancée (`./lancer_app.sh` ou `streamlit run app_prediction.py`)
- [ ] Navigateur ouvert sur `http://localhost:8501`

**Vous êtes prêt ! 🚀**

---

*Dernière mise à jour : Octobre 2025*
*Modèle : XGBoost Optimisé (ROC-AUC: 0.8947)*
