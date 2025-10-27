"""
Application Web pour Prédiction de Réponse aux Campagnes Marketing
Modèle: XGBoost optimisé
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

# Configuration de la page
st.set_page_config(
    page_title="Prédiction Campagne Marketing",
    page_icon="📊",
    layout="wide"
)

# Titre
st.title("📊 Prédiction de Réponse aux Campagnes Marketing")
st.markdown("---")

# Fonction pour charger le modèle
@st.cache_resource
def load_model():
    try:
        model = joblib.load('xgboost_champion_optimized.pkl')
        return model
    except FileNotFoundError:
        st.error("❌ Modèle non trouvé. Assurez-vous que 'xgboost_champion_optimized.pkl' est dans le même dossier.")
        return None

# Charger le modèle
model = load_model()

if model is not None:
    st.success("✅ Modèle chargé avec succès (ROC-AUC: 0.8947, F1-Score: 0.6259)")

# Sidebar pour la navigation
st.sidebar.title("🎯 Navigation")
mode = st.sidebar.radio(
    "Choisissez un mode:",
    ["🧑 Prédiction Individuelle", "📋 Prédiction en Batch", "📈 Statistiques"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📖 À propos")
st.sidebar.info(
    "Cette application prédit si un client va répondre positivement "
    "à une campagne marketing basée sur son profil et comportement d'achat."
)

# =====================================================================
# MODE 1 : PRÉDICTION INDIVIDUELLE
# =====================================================================
if mode == "🧑 Prédiction Individuelle":
    st.header("🧑 Entrez le Profil du Client")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("👤 Informations Démographiques")
        age = st.slider("Âge", 18, 100, 45)
        statut_marital = st.selectbox(
            "Statut marital",
            ["Marié(e)", "Célibataire", "Divorcé(e)", "Veuf(ve)", "En couple"]
        )
        niveau_education = st.selectbox(
            "Niveau d'éducation",
            ["Doctorat", "Master", "Licence", "Lycée", "Collège"]
        )
        revenu = st.number_input("Revenu annuel (€)", 0, 200000, 50000, 1000)
        total_enfants = st.number_input("Nombre d'enfants à la maison", 0, 5, 0)

    with col2:
        st.subheader("🛒 Comportement d'Achat")
        achat_vins = st.number_input("Montant Vins (€)", 0, 2000, 300)
        achat_viandes = st.number_input("Montant Viandes (€)", 0, 2000, 200)
        achat_poissons = st.number_input("Montant Poissons (€)", 0, 500, 50)
        achat_fruits = st.number_input("Montant Fruits (€)", 0, 500, 30)
        achat_sucres = st.number_input("Montant Produits Sucrés (€)", 0, 500, 20)
        achat_or = st.number_input("Montant Produits Premium (€)", 0, 500, 40)

    with col3:
        st.subheader("📊 Engagement")
        visites_web = st.number_input("Visites Web / Mois", 0, 20, 5)
        jours_dernier_achat = st.slider("Jours depuis dernier achat", 0, 365, 30)
        total_achats_catalogue = st.number_input("Achats via Catalogue", 0, 20, 3)
        total_achats_magasin = st.number_input("Achats en Magasin", 0, 20, 8)
        total_achats_web = st.number_input("Achats Web", 0, 20, 4)
        total_campagnes_acceptees = st.number_input("Campagnes Acceptées (historique)", 0, 6, 1)

    st.markdown("---")

    if st.button("🔮 PRÉDIRE LA RÉPONSE", type="primary", use_container_width=True):
        if model is not None:
            # Mapper les valeurs catégorielles
            statut_mapping = {
                "Marié(e)": 1, "Célibataire": 0, "Divorcé(e)": 2,
                "Veuf(ve)": 3, "En couple": 4
            }
            education_mapping = {
                "Doctorat": 4, "Master": 3, "Licence": 2, "Lycée": 1, "Collège": 0
            }

            # Calculer les features dérivées
            total_depense = achat_vins + achat_viandes + achat_poissons + achat_fruits + achat_sucres + achat_or
            ratio_vins = achat_vins / total_depense if total_depense > 0 else 0
            ratio_viandes = achat_viandes / total_depense if total_depense > 0 else 0
            total_achats = total_achats_catalogue + total_achats_magasin + total_achats_web
            engagement_web = visites_web * total_achats_web if total_achats_web > 0 else 0
            depense_moyenne_achat = total_depense / total_achats if total_achats > 0 else 0
            sensibilite_promo = 0.1  # Valeur par défaut
            taux_reponse_historique = total_campagnes_acceptees / 5 if total_campagnes_acceptees > 0 else 0

            # Créer le dataframe avec les 36 features (NOMS EXACTS du modèle ML_DataSet.csv)
            client_data = pd.DataFrame({
                'Revenu': [revenu],
                'Jours_Dernier_Achat': [jours_dernier_achat],
                'Achat_Vins': [achat_vins],
                'Achat_Fruits': [achat_fruits],
                'Achat_Viandes': [achat_viandes],
                'Achat_Poissons': [achat_poissons],
                'Achat_Produits_Sucres': [achat_sucres],
                'Achat_Produits_Or': [achat_or],
                'Achats_Promotions': [0],
                'Achats_En_Ligne': [total_achats_web],
                'Achats_Catalogue': [total_achats_catalogue],
                'Achats_En_Magasin': [total_achats_magasin],
                'Visites_Web_Mois': [visites_web],
                'Reponse_Campagne_3': [0],
                'Reponse_Campagne_4': [0],
                'Reponse_Campagne_5': [0],
                'Reponse_Campagne_1': [0],
                'Reponse_Campagne_2': [0],
                'Plainte': [0],
                'Total_Depense': [total_depense],
                'Total_Achats': [total_achats],
                'Depense_Moy_Par_Achat': [depense_moyenne_achat],
                'Total_Campagnes_Acceptees': [total_campagnes_acceptees],
                'Revenu_Moyen_Mois': [revenu / 12],
                'Age_Inscription': [age],
                'Niveau_Education_Encode': [education_mapping[niveau_education]],
                'Statut_Marital_Encode': [statut_mapping[statut_marital]],
                'Jour_Inscription_Encode': [1],
                'Categorie_Age_Encode': [1 if age < 35 else 2 if age < 50 else 3],
                'Total_Enfants': [total_enfants],
                'A_Des_Enfants': [1 if total_enfants > 0 else 0],
                'Ratio_Vins': [ratio_vins],
                'Ratio_Viandes': [ratio_viandes],
                'Taux_Reponse_Historique': [taux_reponse_historique],
                'Engagement_Web': [engagement_web],
                'Sensibilite_Promo': [sensibilite_promo]
            })

            # Faire la prédiction
            try:
                prediction = model.predict(client_data)[0]
                probabilite = model.predict_proba(client_data)[0, 1]

                # Afficher les résultats avec style
                st.markdown("---")
                st.header("🎯 Résultat de la Prédiction")

                col_res1, col_res2, col_res3 = st.columns(3)

                with col_res1:
                    if prediction == 1:
                        st.success("### ✅ RÉPONDRA")
                        st.metric("Décision", "OUI", "Contacter ce client")
                    else:
                        st.error("### ❌ NE RÉPONDRA PAS")
                        st.metric("Décision", "NON", "Ne pas contacter")

                with col_res2:
                    st.info(f"### 📊 {probabilite*100:.1f}%")
                    st.metric("Probabilité de Réponse", f"{probabilite*100:.1f}%")

                with col_res3:
                    if probabilite >= 0.7:
                        confiance = "🔥 Très Élevée"
                        color = "green"
                    elif probabilite >= 0.5:
                        confiance = "✅ Élevée"
                        color = "blue"
                    elif probabilite >= 0.3:
                        confiance = "⚠️ Moyenne"
                        color = "orange"
                    else:
                        confiance = "❌ Faible"
                        color = "red"

                    st.markdown(f"### {confiance}")
                    st.metric("Niveau de Confiance", confiance)

                # Gauge chart pour la probabilité
                fig = go.Figure(go.Indicator(
                    mode="gauge+number+delta",
                    value=probabilite * 100,
                    domain={'x': [0, 1], 'y': [0, 1]},
                    title={'text': "Probabilité de Réponse"},
                    delta={'reference': 50},
                    gauge={
                        'axis': {'range': [None, 100]},
                        'bar': {'color': "darkblue"},
                        'steps': [
                            {'range': [0, 30], 'color': "lightgray"},
                            {'range': [30, 50], 'color': "lightyellow"},
                            {'range': [50, 70], 'color': "lightgreen"},
                            {'range': [70, 100], 'color': "green"}
                        ],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': 50
                        }
                    }
                ))

                st.plotly_chart(fig, use_container_width=True)

                # Recommandation détaillée
                st.markdown("---")
                st.subheader("💡 Recommandation Détaillée")

                if probabilite >= 0.7:
                    st.success(
                        f"🎯 **Priorité Haute** : Ce client a {probabilite*100:.1f}% de chances de répondre. "
                        "**Action recommandée** : Contacter immédiatement avec une offre personnalisée."
                    )
                elif probabilite >= 0.5:
                    st.info(
                        f"✅ **Bon Prospect** : Ce client a {probabilite*100:.1f}% de chances de répondre. "
                        "**Action recommandée** : Inclure dans la campagne principale."
                    )
                elif probabilite >= 0.3:
                    st.warning(
                        f"⚠️ **Prospect Incertain** : Ce client a {probabilite*100:.1f}% de chances de répondre. "
                        "**Action recommandée** : Cibler uniquement si budget disponible."
                    )
                else:
                    st.error(
                        f"❌ **Faible Potentiel** : Ce client a seulement {probabilite*100:.1f}% de chances de répondre. "
                        "**Action recommandée** : Ne pas contacter pour optimiser le budget."
                    )

                # Facteurs clés
                st.markdown("---")
                st.subheader("🔍 Facteurs Clés du Profil")

                col_f1, col_f2 = st.columns(2)

                with col_f1:
                    st.markdown("**Points Positifs** 🟢")
                    if total_campagnes_acceptees > 0:
                        st.write(f"- ✅ A déjà accepté {total_campagnes_acceptees} campagne(s)")
                    if jours_dernier_achat < 60:
                        st.write(f"- ✅ Client actif (dernier achat: {jours_dernier_achat} jours)")
                    if total_depense > 500:
                        st.write(f"- ✅ Dépenses élevées ({total_depense:.0f}€)")
                    if visites_web > 5:
                        st.write(f"- ✅ Engagement web fort ({visites_web} visites/mois)")

                with col_f2:
                    st.markdown("**Points d'Attention** 🔴")
                    if total_campagnes_acceptees == 0:
                        st.write("- ⚠️ N'a jamais accepté de campagne")
                    if jours_dernier_achat > 180:
                        st.write(f"- ⚠️ Client inactif ({jours_dernier_achat} jours)")
                    if total_depense < 200:
                        st.write(f"- ⚠️ Dépenses faibles ({total_depense:.0f}€)")
                    if visites_web < 2:
                        st.write("- ⚠️ Faible engagement web")

            except Exception as e:
                st.error(f"❌ Erreur lors de la prédiction: {str(e)}")
                st.info("Vérifiez que toutes les features correspondent au modèle entraîné.")

# =====================================================================
# MODE 2 : PRÉDICTION EN BATCH
# =====================================================================
elif mode == "📋 Prédiction en Batch":
    st.header("📋 Prédiction en Batch (Fichier CSV)")

    st.info(
        "📁 **Format attendu** : Téléchargez un fichier CSV avec les mêmes colonnes "
        "que votre dataset d'entraînement (ML_DataSet.csv)"
    )

    uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success(f"✅ {len(df)} clients chargés")

            st.subheader("👀 Aperçu des données")
            st.dataframe(df.head(), use_container_width=True)

            if st.button("🔮 LANCER LES PRÉDICTIONS", type="primary"):
                if model is not None:
                    # Mapping des colonnes : CSV -> Modèle
                    column_mapping = {
                        # Campagnes
                        'Accepte_Campagne1': 'Reponse_Campagne_1',
                        'Accepte_Campagne2': 'Reponse_Campagne_2',
                        'Accepte_Campagne3': 'Reponse_Campagne_3',
                        'Accepte_Campagne4': 'Reponse_Campagne_4',
                        'Accepte_Campagne5': 'Reponse_Campagne_5',
                        # Achats (attention aux doublons !)
                        'Total_Achats_Web': 'Achats_En_Ligne',
                        'Total_Achats_Catalogue': 'Achats_Catalogue',
                        'Total_Achats_Magasin': 'Achats_En_Magasin',  # On garde celui-ci
                        'Total_Achats_Promo': 'Achats_Promotions',
                        # Autres
                        'Reclamation': 'Plainte',
                        'A_Enfants': 'A_Des_Enfants',
                        'Age': 'Age_Inscription',
                    }

                    st.info(f"📋 Colonnes dans le CSV: {list(df.columns)}")

                    # Renommer les colonnes si elles existent
                    df_renamed = df.rename(columns=column_mapping)

                    # Calculer les features manquantes si nécessaire
                    if 'Revenu_Moyen_Mois' not in df_renamed.columns and 'Revenu' in df_renamed.columns:
                        df_renamed['Revenu_Moyen_Mois'] = df_renamed['Revenu'] / 12

                    if 'Jour_Inscription_Encode' not in df_renamed.columns:
                        df_renamed['Jour_Inscription_Encode'] = 1  # Valeur par défaut

                    if 'Categorie_Age_Encode' not in df_renamed.columns and 'Age_Inscription' in df_renamed.columns:
                        df_renamed['Categorie_Age_Encode'] = df_renamed['Age_Inscription'].apply(
                            lambda x: 1 if x < 35 else 2 if x < 50 else 3
                        )

                    if 'Taux_Reponse_Historique' not in df_renamed.columns and 'Total_Campagnes_Acceptees' in df_renamed.columns:
                        df_renamed['Taux_Reponse_Historique'] = df_renamed['Total_Campagnes_Acceptees'] / 5

                    # Préparer les données
                    colonnes_a_exclure = [
                        'ID_Client', 'Annee_Naissance', 'Date_Inscription',
                        'Niveau_Education', 'Statut_Marital', 'Statut_Marital_Texte',
                        'Jour_Inscription', 'Categorie_Age', 'Cout_Contact_Z',
                        'Revenus_Z', 'Reponse_Derniere_Campagne',
                        'Enfants_Maison', 'Ados_Maison',
                        'Mois_Inscription', 'Anciennete_Jours', 'Achats_Hors_Promo',
                        'Achats_En_Magasin'  # Doublon avec Total_Achats_Magasin
                    ]

                    X = df_renamed.drop(columns=colonnes_a_exclure, errors='ignore')

                    # Debug: afficher le nombre de colonnes
                    st.info(f"🔍 Debug: {len(X.columns)} colonnes après exclusion")

                    # Définir les 36 features attendues par le modèle (dans l'ordre)
                    expected_features = [
                        'Revenu', 'Jours_Dernier_Achat', 'Achat_Vins', 'Achat_Fruits',
                        'Achat_Viandes', 'Achat_Poissons', 'Achat_Produits_Sucres', 'Achat_Produits_Or',
                        'Achats_Promotions', 'Achats_En_Ligne', 'Achats_Catalogue', 'Achats_En_Magasin',
                        'Visites_Web_Mois', 'Reponse_Campagne_3', 'Reponse_Campagne_4', 'Reponse_Campagne_5',
                        'Reponse_Campagne_1', 'Reponse_Campagne_2', 'Plainte', 'Total_Depense',
                        'Total_Achats', 'Depense_Moy_Par_Achat', 'Total_Campagnes_Acceptees', 'Revenu_Moyen_Mois',
                        'Age_Inscription', 'Niveau_Education_Encode', 'Statut_Marital_Encode', 'Jour_Inscription_Encode',
                        'Categorie_Age_Encode', 'Total_Enfants', 'A_Des_Enfants', 'Ratio_Vins',
                        'Ratio_Viandes', 'Taux_Reponse_Historique', 'Engagement_Web', 'Sensibilite_Promo'
                    ]

                    # Ajouter les colonnes manquantes avec des valeurs par défaut
                    for col in expected_features:
                        if col not in X.columns:
                            st.warning(f"⚠️ Colonne manquante '{col}' - Ajout avec valeur par défaut 0")
                            X[col] = 0

                    # Réordonner les colonnes pour correspondre exactement au modèle
                    X = X[expected_features]

                    # Debug: vérifier le nombre final de colonnes
                    st.success(f"✅ {len(X.columns)} features finales envoyées au modèle (attendu: 36)")

                    if len(X.columns) != 36:
                        st.error(f"❌ ERREUR: {len(X.columns)} colonnes au lieu de 36 !")
                        st.write("Colonnes présentes:", list(X.columns))
                        st.stop()

                    # Imputation
                    from sklearn.impute import SimpleImputer
                    imputer = SimpleImputer(strategy='median')
                    X_imputed = imputer.fit_transform(X)
                    X = pd.DataFrame(X_imputed, columns=X.columns)

                    # Prédictions
                    predictions = model.predict(X)
                    probabilites = model.predict_proba(X)[:, 1]

                    # Créer le rapport
                    resultats = pd.DataFrame({
                        'ID_Client': df['ID_Client'] if 'ID_Client' in df.columns else range(len(df)),
                        'Prediction': ['OUI ✅' if p == 1 else 'NON ❌' for p in predictions],
                        'Probabilite_Reponse_%': (probabilites * 100).round(2),
                        'Confiance': pd.cut(probabilites,
                                           bins=[0, 0.3, 0.5, 0.7, 1.0],
                                           labels=['Faible', 'Moyenne', 'Élevée', 'Très Élevée']),
                        'Recommandation': ['CONTACTER' if p >= 0.5 else 'Ne pas contacter'
                                          for p in probabilites]
                    })

                    resultats = resultats.sort_values('Probabilite_Reponse_%', ascending=False)

                    # Afficher les résultats
                    st.markdown("---")
                    st.header("📊 Résultats des Prédictions")

                    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)

                    with col_stat1:
                        st.metric("Total Clients", len(df))

                    with col_stat2:
                        nb_oui = sum(predictions == 1)
                        st.metric("À Contacter", nb_oui, f"{nb_oui/len(df)*100:.1f}%")

                    with col_stat3:
                        nb_haute_confiance = sum(probabilites >= 0.7)
                        st.metric("Haute Confiance", nb_haute_confiance)

                    with col_stat4:
                        prob_moyenne = probabilites.mean() * 100
                        st.metric("Prob. Moyenne", f"{prob_moyenne:.1f}%")

                    # Graphiques
                    col_g1, col_g2 = st.columns(2)

                    with col_g1:
                        fig_pie = px.pie(
                            values=[sum(predictions == 0), sum(predictions == 1)],
                            names=['Ne pas contacter', 'Contacter'],
                            title="Répartition des Recommandations",
                            color_discrete_sequence=['#ef4444', '#22c55e']
                        )
                        st.plotly_chart(fig_pie, use_container_width=True)

                    with col_g2:
                        fig_hist = px.histogram(
                            x=probabilites * 100,
                            nbins=20,
                            title="Distribution des Probabilités",
                            labels={'x': 'Probabilité (%)', 'y': 'Nombre de clients'}
                        )
                        st.plotly_chart(fig_hist, use_container_width=True)

                    # Tableau des résultats
                    st.subheader("📋 Tableau Détaillé")
                    st.dataframe(resultats, use_container_width=True, height=400)

                    # Téléchargement
                    csv = resultats.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 Télécharger les Résultats (CSV)",
                        data=csv,
                        file_name=f'predictions_{datetime.now().strftime("%Y%m%d_%H%M")}.csv',
                        mime='text/csv',
                        type="primary"
                    )

        except Exception as e:
            st.error(f"❌ Erreur lors du chargement du fichier: {str(e)}")

# =====================================================================
# MODE 3 : STATISTIQUES DU MODÈLE
# =====================================================================
else:
    st.header("📈 Statistiques du Modèle")

    col_perf1, col_perf2, col_perf3 = st.columns(3)

    with col_perf1:
        st.metric("Accuracy", "87.72%", "+11.65% vs baseline")

    with col_perf2:
        st.metric("ROC-AUC", "0.8947", "+1.24% vs baseline")

    with col_perf3:
        st.metric("F1-Score", "0.6259", "Excellent")

    st.markdown("---")

    st.subheader("🎯 Performances par Classe")

    perf_data = pd.DataFrame({
        'Classe': ['Non-Répondants (0)', 'Répondants (1)'],
        'Précision': [0.94, 0.57],
        'Rappel': [0.91, 0.69],
        'F1-Score': [0.93, 0.63],
        'Support': [381, 67]
    })

    st.dataframe(perf_data, use_container_width=True)

    st.markdown("---")

    st.subheader("🔍 Top 5 Variables Importantes (SHAP)")

    features_importance = pd.DataFrame({
        'Feature': [
            'Jours Dernier Achat',
            'Total Campagnes Acceptées',
            'Visites Web / Mois',
            'Statut Marital',
            'Ratio Vins'
        ],
        'Importance': [0.918, 0.806, 0.575, 0.463, 0.445]
    })

    fig_imp = px.bar(
        features_importance,
        x='Importance',
        y='Feature',
        orientation='h',
        title="Impact des Variables sur les Prédictions",
        color='Importance',
        color_continuous_scale='Blues'
    )

    st.plotly_chart(fig_imp, use_container_width=True)

    st.markdown("---")

    st.subheader("📊 Optimisations Appliquées")

    col_opt1, col_opt2 = st.columns(2)

    with col_opt1:
        st.markdown("""
        **✅ Techniques Utilisées**
        - GridSearchCV (32 combinaisons)
        - scale_pos_weight (gestion déséquilibre)
        - Comparaison avec SMOTE
        - SHAP values (interprétabilité)
        """)

    with col_opt2:
        st.markdown("""
        **⚙️ Hyperparamètres Optimaux**
        - n_estimators: 200
        - max_depth: 3
        - learning_rate: 0.1
        - gamma: 0.1
        - subsample: 0.8
        """)

    st.info(
        "💡 **Note** : Le modèle a été entraîné sur 2237 clients avec 36 features. "
        "Le ratio de déséquilibre initial était de 5.7:1 (non-répondants vs répondants)."
    )

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "🤖 Modèle XGBoost optimisé | "
    "📅 Dernière mise à jour: 2025-10-17 | "
    "📊 ROC-AUC: 0.8947"
    "</div>",
    unsafe_allow_html=True
)
