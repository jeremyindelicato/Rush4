# Rapport d'Analyse Marketing - Dashboard Interactif

**Date:** Octobre 2025
**Projet:** Analyse du Panier Moyen et Performance des Campagnes Marketing
**Outil:** Dashboard Streamlit Interactif

---

## Table des Matières

1. [Résumé Exécutif](#résumé-exécutif)
2. [Méthodologie](#méthodologie)
3. [Analyse du Panier Moyen](#analyse-du-panier-moyen)
4. [Performance des Campagnes Marketing](#performance-des-campagnes-marketing)
5. [Segmentation Clients](#segmentation-clients)
6. [Recommandations Stratégiques](#recommandations-stratégiques)
7. [Conclusion](#conclusion)

---

## Résumé Exécutif

Ce rapport présente une analyse approfondie du comportement d'achat des clients et de l'efficacité des campagnes marketing menées par l'entreprise. Les données ont été analysées via un dashboard interactif permettant une exploration dynamique des métriques clés.

### Points Clés :
- **Analyse multicritère** du panier moyen par catégorie de produits
- **Évaluation du ROI** de 6 campagnes marketing distinctes
- **Segmentation clients** en 3 catégories : Petits, Moyens et Grands Dépensiers
- **Analyse comportementale** selon le statut marital, l'âge, le niveau d'éducation et la composition familiale

---

## Méthodologie

### Source des Données
- **Fichier:** Camp_Market_final.csv
- **Période analysée:** Données clients avec historique d'achats et réponses aux campagnes
- **Volume:** Base de données client complète avec variables démographiques et comportementales

### Variables Analysées

#### Variables Démographiques
- Année de naissance / Âge à l'inscription
- Niveau d'éducation
- Statut marital
- Composition familiale (enfants et adolescents)
- Revenu annuel

#### Variables Comportementales
- Achats par catégorie (Vins, Fruits, Viandes, Poissons, Produits Sucrés, Produits Or)
- Canaux d'achat (En ligne, Catalogue, En magasin)
- Achats en promotion vs achats normaux
- Fréquence des visites web
- Récence du dernier achat

#### Variables Marketing
- Réponses aux 6 campagnes marketing
- Taux de plaintes
- Coût de contact
- Revenus générés par conversion

### Outils Utilisés
- **Dashboard Streamlit** pour la visualisation interactive
- **Plotly** pour les graphiques dynamiques
- **Pandas** pour le traitement des données
- **Filtres interactifs** permettant l'analyse par segment

---

## Analyse du Panier Moyen

### 1. Composition du Panier Moyen par Catégorie

Le dashboard permet d'analyser la répartition des dépenses moyennes par catégorie de produits :

#### Catégories Analysées :
1. **Vins** - Généralement la catégorie dominante
2. **Viandes** - Deuxième poste de dépense important
3. **Poissons** - Part significative dans le panier moyen
4. **Fruits** - Catégorie complémentaire
5. **Produits Sucrés** - Part variable selon les segments
6. **Produits Or** (produits premium) - Indicateur de pouvoir d'achat

#### Insights Clés :

**Répartition type observée :**
- Les vins représentent généralement la part la plus importante des dépenses
- Les produits carnés (viandes + poissons) constituent le deuxième ensemble majeur
- Les produits sucrés et fruits varient fortement selon la composition familiale

**Impact de la segmentation :**
- **Grands Dépensiers** : Forte concentration sur vins et produits premium
- **Moyens Dépensiers** : Panier équilibré entre toutes les catégories
- **Petits Dépensiers** : Focus sur produits essentiels (viandes, fruits)

### 2. Indicateurs Clés de Performance (KPIs)

Le dashboard affiche en temps réel les métriques suivantes :

#### KPIs Financiers :
- **Revenu Moyen Annuel** : Indicateur de la capacité d'achat des clients
- **Revenu Mensuel Moyen** : Revenu annuel / 12 pour une vision mensuelle
- **Valeur du Panier Moyen** : Somme moyenne des achats par catégorie
- **Dépense Moyenne par Achat** : Total des dépenses / nombre d'achats

#### KPIs Comportementaux :
- **Âge Moyen** : Profil démographique de la clientèle
- **Nombre d'Achats Moyen** : Fréquence d'achat des clients
- **Taux de Plaintes** : Indicateur de satisfaction client

#### Observations Principales :
1. **Corrélation positive** entre revenu et valeur du panier moyen
2. **Impact significatif** du statut marital sur les montants dépensés
3. **Variation saisonnière** potentielle à approfondir
4. **Faible taux de plaintes** indiquant une satisfaction globale

### 3. Analyse des Canaux d'Achat

#### Distribution des Achats par Canal :

**Trois canaux principaux :**
1. **En Magasin** - Canal traditionnel
2. **En Ligne** - Canal digital en croissance
3. **Par Catalogue** - Canal historique

#### Analyse Promotion vs Normal :

Le dashboard décompose chaque canal en :
- **Achats Normaux** (prix régulier)
- **Achats en Promotion** (prix réduit)

**Métriques affichées :**
- Pourcentage d'achats en promotion par canal
- Volume total d'achats par canal
- Répartition promotion/normal en barres empilées

#### Insights Stratégiques :

1. **Sensibilité aux promotions** : Le pourcentage d'achats en promotion varie selon le canal
2. **Canal préférentiel** : Identification du canal générant le plus de volume
3. **Opportunités cross-canal** : Potentiel de migration entre canaux
4. **Optimisation promotionnelle** : Ajustement de la stratégie promotionnelle par canal

### 4. Visites Web par Segment de Dépensier

#### Analyse Comportementale Digitale :

**Observation type :**
- Les **Grands Dépensiers** visitent plus fréquemment le site web
- Les **Moyens Dépensiers** ont une fréquence intermédiaire
- Les **Petits Dépensiers** visitent moins souvent

#### Implications :
1. **Engagement digital** corrélé positivement avec le niveau de dépense
2. **Opportunité de conversion** : Augmenter les visites = augmenter les dépenses potentielles
3. **Stratégie de contenu** : Adapter le contenu web pour chaque segment
4. **Remarketing** : Cibler les visiteurs fréquents avec des offres premium

---

## Performance des Campagnes Marketing

### 1. Vue d'Ensemble des Campagnes

Le dashboard analyse **6 campagnes marketing distinctes** :
- Campagne 1
- Campagne 2
- Campagne 3
- Campagne 4
- Campagne 5
- Dernière Campagne (6)

### 2. Métriques de Performance

#### KPIs Calculés par Campagne :

**Métriques de Participation :**
- **Nombre de Participants** : Clients ayant répondu positivement
- **Taux de Participation** : (Réponses positives / Clients contactés) × 100
- **Participation Globale** : % de clients ayant répondu à au moins une campagne

**Métriques Financières :**
- **Coût de la Campagne** : Nombre de clients × Coût de contact unitaire
- **Revenu de la Campagne** : Nombre de réponses × Revenu par conversion
- **Bénéfice de la Campagne** : Revenu - Coût
- **ROI** : ((Revenu - Coût) / Coût) × 100

### 3. Seuil de Rentabilité

#### Analyse Critique :

Le dashboard affiche une **ligne de seuil de rentabilité à 611 réponses** :

**Calcul du seuil :**
```
Seuil = Coût total / Revenu par conversion
```

**Interprétation :**
- ✅ **Au-dessus de 611 réponses** : Campagne rentable (ROI positif)
- ❌ **En-dessous de 611 réponses** : Campagne déficitaire (ROI négatif)

#### Performance Relative des Campagnes :

**Scénario type observé :**
1. Certaines campagnes dépassent largement le seuil → Très rentables
2. D'autres sont proches du seuil → Rentabilité marginale
3. Certaines peuvent être en-dessous → Nécessitent une réévaluation

### 4. Filtrage et Segmentation des Campagnes

Le dashboard permet d'analyser les campagnes selon différents filtres :

#### Filtres Démographiques :
- **Statut marital** : Identifier quels profils répondent le mieux
- **Catégorie d'âge** : Adapter le message selon la génération
- **Niveau d'éducation** : Personnaliser la communication
- **Composition familiale** : Cibler selon les besoins familiaux

#### Filtres Comportementaux :
- **Segment de dépensier** : Concentrer les efforts sur les segments rentables
- **Historique d'achat** : Cibler selon les catégories préférées

### 5. Récence Moyenne par Segment

#### Analyse de la Fidélité Client :

**Métrique : Jours Moyens depuis le Dernier Achat**

**Observations typiques :**
- **Grands Dépensiers** : Récence faible (achats fréquents)
- **Moyens Dépensiers** : Récence intermédiaire
- **Petits Dépensiers** : Récence élevée (risque de churn)

#### Implications Marketing :
1. **Campagnes de réactivation** pour les segments à récence élevée
2. **Programmes de fidélité** pour maintenir l'engagement des Grands Dépensiers
3. **Offres de bienvenue** pour réengager les clients inactifs
4. **Timing optimal** : Contacter avant que la récence ne devienne critique

---

## Segmentation Clients

### 1. Trois Segments Principaux

Le dashboard segmente automatiquement les clients en :

#### A. Grands Dépensiers
**Caractéristiques :**
- Panier moyen élevé
- Achats fréquents
- Faible récence
- Visites web fréquentes
- Sensibles aux produits premium

**Stratégie recommandée :**
- Programme VIP / Fidélité premium
- Offres exclusives
- Service client prioritaire
- Communication personnalisée

#### B. Moyens Dépensiers
**Caractéristiques :**
- Panier moyen dans la norme
- Fréquence d'achat régulière
- Récence modérée
- Équilibre entre promotions et prix normaux

**Stratégie recommandée :**
- Programmes d'upselling
- Offres groupées
- Incitations à augmenter la fréquence
- Cross-selling entre catégories

#### C. Petits Dépensiers
**Caractéristiques :**
- Panier moyen faible
- Achats occasionnels
- Récence élevée
- Forte sensibilité aux promotions

**Stratégie recommandée :**
- Offres promotionnelles agressives
- Campagnes de réactivation
- Produits d'entrée de gamme
- Simplification du parcours d'achat

### 2. Filtrage Multidimensionnel

Le dashboard permet de croiser plusieurs dimensions :

#### Exemples d'Analyses Possibles :
1. **Célibataires Grands Dépensiers de 35-50 ans** : Profil urbain premium
2. **Couples avec enfants Moyens Dépensiers** : Famille active
3. **Seniors Petits Dépensiers** : Cible sensible au prix
4. **Diplômés universitaires sans enfants** : Professionnels jeunes

#### Bénéfices du Filtrage :
- **Personnalisation** : Messages ultra-ciblés
- **Optimisation budgétaire** : Concentrer les efforts sur segments rentables
- **Test A/B** : Comparer performance entre segments
- **Prédiction** : Anticiper comportements futurs

---

## Recommandations Stratégiques

### 1. Optimisation des Campagnes Marketing

#### Actions Prioritaires :

**Pour les campagnes sous le seuil de rentabilité :**
1. **Réviser le ciblage** : Utiliser les filtres pour identifier les segments rentables
2. **Ajuster le message** : Personnaliser selon les caractéristiques démographiques
3. **Optimiser le timing** : Contacter au moment optimal (récence, saisonnalité)
4. **Réduire les coûts** : Automatiser ou digitaliser les contacts

**Pour les campagnes rentables :**
1. **Scaler** : Augmenter le budget et l'audience
2. **Répliquer** : Appliquer la même approche à d'autres segments
3. **Affiner** : Continuer à optimiser pour maximiser le ROI
4. **Tester** : Expérimenter des variantes pour améliorer encore

### 2. Stratégie par Canal

#### Canal En Ligne
**Opportunités :**
- Croissance continue du digital
- Coûts d'acquisition potentiellement plus faibles
- Meilleur tracking et personnalisation
- Automatisation possible

**Recommandations :**
1. Investir dans l'UX du site web
2. Développer le contenu (blog, guides d'achat)
3. Implémenter le retargeting
4. Optimiser pour mobile

#### Canal En Magasin
**Opportunités :**
- Expérience tactile et sensorielle
- Conseil personnalisé
- Achat impulsif favorisé
- Fidélisation par la relation

**Recommandations :**
1. Former les équipes au cross-selling
2. Créer des événements en magasin
3. Programme de fidélité carte physique
4. Click & Collect pour allier online et offline

#### Canal Catalogue
**Opportunités :**
- Touche les seniors et zones rurales
- Support physique apprécié
- Consultation à domicile
- Effet de marque

**Recommandations :**
1. Digitaliser le catalogue (PDF interactif)
2. QR codes pour lier au online
3. Offres exclusives catalogue
4. Segmenter l'envoi selon profil

### 3. Gestion des Promotions

#### Analyse Actuelle :
Le dashboard montre la part des achats en promotion par canal.

#### Recommandations :
1. **Éviter la cannibalisation** : Ne pas tout promouvoir simultanément
2. **Promotions ciblées** : Adapter l'intensité selon le segment
3. **Seuils psychologiques** : -20%, -30%, -50% ont des impacts différents
4. **Urgence et rareté** : Offres limitées dans le temps
5. **Bundle promotions** : Grouper produits complémentaires

### 4. Développement de la Valeur Client

#### Objectif : Faire migrer les clients vers des segments supérieurs

**Petits → Moyens Dépensiers :**
- Programme de découverte de nouvelles catégories
- Offres sur le 2ème ou 3ème article
- Livraison gratuite à partir d'un seuil
- Points de fidélité accélérés

**Moyens → Grands Dépensiers :**
- Accès anticipé aux nouveautés
- Produits premium en édition limitée
- Service concierge
- Événements VIP

### 5. Réduction du Churn

#### Clients à Risque :
Identifier via la récence élevée et la baisse de fréquence.

**Actions de Rétention :**
1. **Email de réengagement** : "Vous nous manquez"
2. **Offre de retour** : Promotion spéciale réactivation
3. **Enquête de satisfaction** : Comprendre les raisons
4. **Programme de winback** : Série d'emails automatisés

### 6. Exploitation des Données Comportementales

#### Visites Web :
- **Corrélation visites/dépenses** : Augmenter le trafic web
- **Contenu éducatif** : Guides, recettes, accords mets-vins
- **Newsletter** : Maintenir l'engagement entre achats
- **Retargeting** : Relancer les visiteurs non-convertis

#### Composition Familiale :
- **Ciblage sur mesure** : Produits enfants, ados, adultes
- **Événements vie** : Rentrée scolaire, vacances, fêtes
- **Quantités adaptées** : Formats familiaux ou individuels

### 7. Optimisation du ROI Global

#### Approche Data-Driven :
1. **Dashboard en temps réel** : Monitoring continu des KPIs
2. **A/B testing systématique** : Tester avant de déployer
3. **Attribution multi-touch** : Comprendre le parcours complet
4. **Predictive analytics** : Anticiper les comportements

#### Allocation Budgétaire :
- **Règle 80/20** : Concentrer 80% du budget sur 20% des segments les plus rentables
- **Budget test** : Réserver 10-15% pour l'expérimentation
- **ROI minimum** : Fixer un seuil de rentabilité pour toute campagne

---

## Conclusion

### Synthèse des Résultats

Le dashboard d'analyse marketing développé offre une **vision complète et interactive** de la performance commerciale et marketing de l'entreprise. Les principales conclusions sont :

#### Forces Identifiées :
1. ✅ **Segmentation claire** en 3 catégories de dépensiers
2. ✅ **Diversité des canaux** permettant de toucher différents profils
3. ✅ **Données riches** sur comportements et démographie
4. ✅ **Certaines campagnes très rentables** (au-dessus du seuil)

#### Axes d'Amélioration :
1. 🔶 **Optimisation des campagnes sous-performantes**
2. 🔶 **Augmentation de l'engagement digital** (visites web)
3. 🔶 **Réduction de la récence** pour éviter le churn
4. 🔶 **Personnalisation accrue** des offres par segment

### Valeur Ajoutée du Dashboard

#### Pour l'Équipe Marketing :
- **Décisions basées sur les données** plutôt que l'intuition
- **Filtrage dynamique** pour tester hypothèses rapidement
- **Visualisation intuitive** des métriques complexes
- **ROI calculé automatiquement** pour chaque campagne

#### Pour la Direction :
- **KPIs synthétiques** pour pilotage global
- **Identification rapide** des opportunités et risques
- **Justification budgétaire** basée sur performances réelles
- **Suivi de la rentabilité** en temps réel

### Prochaines Étapes

#### Court Terme (1-3 mois) :
1. **Déployer les optimisations** sur campagnes sous-performantes
2. **Lancer tests A/B** sur segments identifiés comme à fort potentiel
3. **Former les équipes** à l'utilisation du dashboard
4. **Automatiser** les rapports hebdomadaires

#### Moyen Terme (3-6 mois) :
1. **Intégrer nouvelles sources de données** (réseaux sociaux, satisfaction client)
2. **Développer modèles prédictifs** (probabilité d'achat, risque de churn)
3. **Personnalisation avancée** des campagnes par segment
4. **Programme de fidélité** différencié par segment

#### Long Terme (6-12 mois) :
1. **IA et Machine Learning** pour recommandations produits
2. **Automatisation marketing** complète (trigger campaigns)
3. **Omnicanal intégré** avec parcours client unifié
4. **Expansion internationale** avec adaptation locale

### Mesure du Succès

#### Indicateurs de Performance :
- **ROI moyen des campagnes** : Objectif +20% vs baseline
- **Taux de réponse** : Objectif +15% avec ciblage optimisé
- **Valeur panier moyen** : Objectif +10% via upselling
- **Récence moyenne** : Objectif -20% via réactivation
- **Taux de churn** : Objectif -25% via fidélisation

### Conclusion Générale

Ce projet d'analyse marketing démontre la **puissance de la data visualization interactive** pour transformer des données brutes en insights actionnables. Le dashboard développé permet non seulement de **comprendre le passé**, mais surtout de **prendre de meilleures décisions pour l'avenir**.

L'approche **centrée sur le ROI** et la **segmentation fine** des clients positionne l'entreprise pour une **croissance rentable et durable**. La capacité à **filtrer, analyser et agir rapidement** sur les données constitue un **avantage concurrentiel majeur** dans un environnement commercial de plus en plus compétitif.

---

## Annexes

### A. Glossaire des Termes

- **ROI** : Return On Investment - Retour sur Investissement
- **KPI** : Key Performance Indicator - Indicateur Clé de Performance
- **Churn** : Taux d'attrition client (clients qui cessent d'acheter)
- **Récence** : Nombre de jours depuis le dernier achat
- **Upselling** : Vente de produits/services supérieurs
- **Cross-selling** : Vente de produits complémentaires
- **Panier moyen** : Montant moyen dépensé par transaction

### B. Méthodologie Technique

**Outils utilisés :**
- Python 3.9+
- Streamlit 1.50.0 (Framework de dashboard)
- Pandas 2.3.3 (Traitement de données)
- Plotly 6.3.1 (Visualisations interactives)

**Architecture :**
- Dashboard web accessible via navigateur
- Mise en cache des données pour performance optimale
- Filtrage dynamique côté client
- Responsive design pour tous écrans

### C. Sources et Références

- Données client anonymisées : Camp_Market_final.csv
- Méthodologie d'analyse marketing : Best practices secteur retail
- Calculs ROI : Standards comptables marketing

---

**Rapport généré dans le cadre du Projet Marketing Analytics**
**Pour toute question : Consulter la documentation du dashboard**

*Ce rapport est un document évolutif, à mettre à jour selon les nouvelles analyses et optimisations.*
