import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page Streamlit
st.set_page_config(layout="wide", page_title="Analyse du Panier Moyen")

# CSS personnalisé pour améliorer le design
st.markdown("""
    <style>
    /* Sidebar styling avec couleur orange #ff9300 */
    [data-testid="stSidebar"] > div:first-child {
        background-color: #495057; /* Gris foncé */
    }

    [data-testid="stSidebar"] {
        background-color: #495057; /* Gris foncé */
    }

    /* Style des labels dans la sidebar */
    [data-testid="stSidebar"] label {
        color: white !important;
        font-weight: 600;
        font-size: 16px;
    }

    /* Style des selectbox et radio dans la sidebar */
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stRadio label {
        color: white !important;
    }

    /* Headers dans la sidebar */
    [data-testid="stSidebar"] h2 {
        color: white !important;
        font-weight: 700;
        padding-bottom: 10px;
        border-bottom: 2px solid white; 
        text-align: center;
    }

    /* Headers h3 dans la sidebar */
    [data-testid="stSidebar"] h3 {
        color: white !important;
        font-weight: 600;
        text-align: center;
    }

    /* Texte des paragraphes dans la sidebar */
    [data-testid="stSidebar"] p {
        color: white !important;
    }

    /* Options des selectbox et radio */
    [data-testid="stSidebar"] [data-baseweb="select"] {
        background-color: white;
    }

    /* Texte dans les inputs de la sidebar */
    [data-testid="stSidebar"] input {
        color: #1f2937 !important;
    }

    /* Dividers dans la sidebar */
    [data-testid="stSidebar"] hr {
        border-color: white !important;
    }

    /* Texte dans les options radio */
    [data-testid="stSidebar"] [role="radiogroup"] label {
        color: white !important;
    }

    /* Markdown dans la sidebar */
    [data-testid="stSidebar"] .stMarkdown {
        color: white !important;
    }

    /* Style principal du dashboard */
    .main {
        background-color: #111827; /* Fond principal très foncé */
    }

    /* Titres principaux */
    h1 {
        color: white;
        font-weight: 700;
        padding-bottom: 20px;
        border-bottom: 3px solid #495057;
        margin-bottom: 20px;
        text-align: center;
    }

    /* Sous-titres */
    h2, h3 {
        color: #d1d5db; /* Gris clair pour les sous-titres */
        font-weight: 600;
        margin-top: 20px;
        text-align: center;
    }

    /* Style des métriques */
    [data-testid="stMetricValue"] {
        font-size: 28px;
        font-weight: 700;
        color: white;
    }

    [data-testid="stMetricLabel"] {
        font-size: 14px;
        font-weight: 600;
        color: #9ca3af; /* Gris pour les labels */
    } 

    /* Cards pour les métriques */
    div[data-testid="metric-container"] {
        background-color: #1f2937; /* Fond des cartes plus clair */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #495057;
        text-align: center;
    }

    /* Style des descriptions */
    .stMarkdown p {
        font-size: 16px;
        color: #d1d5db; /* Gris clair pour le texte */
        line-height: 1.6;
    }

    /* Séparateurs */
    hr {
        margin: 30px 0;
        border: none;
        height: 2px;
        background: linear-gradient(to right, #495057, transparent);
    }

    /* Warnings et infos */
    .stWarning, .stInfo {
        border-radius: 10px;
        padding: 15px;
    }

    /* Amélioration des graphiques */
    .js-plotly-plot {
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data(file_path):
    """
    Charge les données depuis un fichier CSV.
    Utilise le cache de Streamlit pour améliorer les performances.
    """
    try:
        # Note: Pour une meilleure portabilité, il est conseillé de placer le CSV
        # dans le même dossier que le script et d'utiliser un chemin relatif.
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"Erreur : Le fichier '{file_path}' est introuvable. Veuillez vérifier le chemin.")
        return None

def main():
    """
    Fonction principale de l'application Streamlit.
    """
    file_path = r'data/Dataset_Dashboard_Analytics.csv'
    df = load_data(file_path)

    if df is None:
        return # Arrête l'exécution si les données ne sont pas chargées

    # --- NOUVEAU : Création de la colonne pour le filtre enfant/ados ---
    df['Enfants/Ados à la maison'] = df['Enfants_Maison'] + df['Ados_Maison']

    # --- 2. Configuration des filtres dans la barre latérale ---
    st.sidebar.markdown("## Navigation & Filtres")
    st.sidebar.markdown("---")

    # --- NOUVEAU : Navigation entre les pages ---
    page = st.sidebar.radio(
        "Choisissez une page",
        ["Analyse du client type", "Influence des Campagnes"],
        label_visibility="visible"
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("### Filtres de segmentation")
    
    # Filtre pour le statut marital (MODIFIÉ)
    marital_statuses = ['Tous'] + list(df['Statut_Marital'].unique())
    selected_marital = st.sidebar.selectbox(
        "Statut Marital",
        options=marital_statuses
    )
    # Filtre pour la catégorie d'âge
    age_categories = ['Tous'] + list(df['Categorie_Age'].unique())
    selected_age = st.sidebar.selectbox(
        "Catégorie d'Âge",
        options=age_categories
    )

    # Filtre pour le niveau d'éducation (MODIFIÉ)
    education_levels = ['Tous'] + list(df['Niveau_Education'].unique())
    selected_education = st.sidebar.selectbox(
        "Niveau d'Éducation",
        options=education_levels
    )

    # --- NOUVEAU : Filtre pour le nombre d'enfants/ados ---
    children_total = ['Tous'] + sorted(list(df['Enfants/Ados à la maison'].unique()))
    selected_children = st.sidebar.selectbox(
        "Nombre d'enfants/ados",
        options=children_total
    )

    # --- NOUVEAU : Filtre pour la segmentation des dépensiers ---
    selected_segmentation = 'Tous' # Valeur par défaut
    # Vérifie si la colonne existe avant de créer le filtre
    if 'Segmentation_Dépensier' in df.columns:
        # Ordre personnalisé pour un meilleur affichage dans le filtre
        segment_order = ['Grand Dépensier', 'Moyens Dépensier', 'Petits Dépensier']
        segmentation_options = ['Tous'] + segment_order
        selected_segmentation = st.sidebar.selectbox(
            "Segment de Dépensier",
            options=segmentation_options
        )

    # --- 3. Filtrage du DataFrame ---
    df_filtered = df.copy() # On part d'une copie complète des données

    # Applique le filtre sur le statut marital si une option autre que "Tous" est choisie
    if selected_marital != 'Tous':
        df_filtered = df_filtered[df_filtered['Statut_Marital'] == selected_marital]
    if selected_age != 'Tous':
        df_filtered = df_filtered[df_filtered['Categorie_Age'] == selected_age]
    if selected_education != 'Tous':
        df_filtered = df_filtered[df_filtered['Niveau_Education'] == selected_education]
    if selected_children != 'Tous':
        df_filtered = df_filtered[df_filtered['Enfants/Ados à la maison'] == selected_children]
    
    # Applique le filtre sur la segmentation si une option autre que "Tous" est choisie
    # La vérification de l'existence de la colonne est implicite car le filtre n'est affiché que si elle existe
    if selected_segmentation != 'Tous':
        df_filtered = df_filtered[df_filtered['Segmentation_Dépensier'] == selected_segmentation]

    # ==============================================================================
    # --- PAGE 1 : ANALYSE DU PANIER MOYEN ---
    # ==============================================================================
    if page == "Analyse du client type":
        st.title("Analyse du client type")
        st.markdown("Ce tableau de bord interactif permet d'analyser la répartition des dépenses moyennes par catégorie de produits.")

        if not df_filtered.empty:
            # --- Création des colonnes pour la disposition ---
            col_graph, col_kpi = st.columns([2, 1]) # Le graphique prend 2/3 de la place, les KPIs 1/3

            product_cols = ['Achat_Vins', 'Achat_Fruits', 'Achat_Viandes', 'Achat_Poissons', 'Achat_Produits_Sucres', 'Achat_Produits_Or']
            
            # Calcul du panier moyen pour chaque catégorie
            average_spending = df_filtered[product_cols].mean().reset_index()
            average_spending.columns = ['Catégorie', 'Dépense Moyenne']
            
            # --- Calculs pour les KPIs ---
            total_average_spending = average_spending['Dépense Moyenne'].sum()
            average_income = df_filtered['Revenu'].mean()
            average_monthly_income = average_income / 12
            avg_spending_per_purchase = df_filtered['Depense_Moy_Par_Achat'].mean()
            average_age = df_filtered['Age_Inscription'].mean()
            average_spending['Pourcentage'] = (average_spending['Dépense Moyenne'] / total_average_spending) * 100

            # --- 5. Affichage dans les colonnes ---
            with col_graph:
                st.subheader("Répartition du Panier Moyen par Catégorie")

                # Palette de couleurs personnalisée
                custom_colors = ['#99ccff', '#99ff99', '#ffcc99', '#ff9999', '#ffff99', '#cc99ff'] # Couleurs pastel

                fig = px.bar(
                    average_spending,
                    x='Catégorie',
                    y='Pourcentage',
                    color='Catégorie',
                    text=average_spending['Pourcentage'].apply(lambda x: f'{x:.2f}%'),
                    title="Pourcentage de chaque catégorie dans le total des dépenses moyennes",
                    color_discrete_sequence=custom_colors
                )
                fig.update_layout(
                    yaxis_title="Pourcentage du Panier Moyen (%)",
                    xaxis_title="Catégorie de Produit",
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(size=12, color='white'),
                    title_font=dict(size=18, color='white', family='Arial Black'),
                    showlegend=False,
                    hovermode='x unified'
                )
                fig.update_traces(
                    textposition='outside',
                    marker=dict(line=dict(width=0)),
                    hovertemplate='<b>%{x}</b><br>%{y:.2f}%<extra></extra>'
                )
                fig.update_xaxes(showgrid=False)
                fig.update_yaxes(showgrid=True, gridcolor='rgba(255, 255, 255, 0.1)')
                st.plotly_chart(fig, use_container_width=True)

            with col_kpi:
                st.subheader("Indicateurs Clés")
                st.metric(label="Revenu Moyen Annuel", value=f"{average_income:,.2f} €")
                st.metric(label="Revenu Mensuel Moyen", value=f"{average_monthly_income:,.2f} €")
                st.metric(label="Valeur du Panier Moyen", value=f"{total_average_spending:,.2f} €")
                st.metric(label="Dépense Moyenne par Achat", value=f"{avg_spending_per_purchase:,.2f} €")
                st.metric(label="Âge Moyen", value=f"{average_age:.1f} ans")

            # --- 6. NOUVEAU GRAPHIQUE : Analyse des lieux d'achat ---
            st.markdown("---") # Ajoute une ligne de séparation
            st.subheader("Analyse des Canaux d'Achat")

            # Estimer la part des promotions pour chaque canal sur les données filtrées
            promo_par_plateforme = {}
            normaux_par_plateforme = {}

            colonnes_plateformes = {
                'Achats_En_Ligne': 'En Ligne',
                'Achats_Catalogue': 'Catalogue',
                'Achats_En_Magasin': 'En Magasin'
            }

            for col, nom in colonnes_plateformes.items():
                # Proportion des achats de ce client sur cette plateforme
                proportion_plateforme_client = df_filtered[col] / df_filtered['Total_Achats'].replace(0, 1)
                
                # Estimer le nombre d'achats en promotion pour cette plateforme et pour chaque client
                promo_plateforme_client = df_filtered['Achats_Promotions'] * proportion_plateforme_client
                
                # Agréger les résultats
                total_promo_estime = promo_plateforme_client.sum()
                promo_par_plateforme[nom] = total_promo_estime
                normaux_par_plateforme[nom] = df_filtered[col].sum() - total_promo_estime

            # --- NOUVEAU : Création des colonnes pour le KPI et le graphique des canaux ---
            col_kpi_promo, col_chart_channels = st.columns([1, 3]) # Le KPI prend 1/4, le graphique 3/4

            # Préparer le DataFrame pour le graphique empilé
            df_promo = pd.DataFrame({'Canal': list(promo_par_plateforme.keys()), 'Type': 'Promotion', 'Achats': list(promo_par_plateforme.values())})
            df_normal = pd.DataFrame({'Canal': list(normaux_par_plateforme.keys()), 'Type': 'Normal', 'Achats': list(normaux_par_plateforme.values())})
            df_channels = pd.concat([df_promo, df_normal])

            # --- NOUVEAU : Calculer le pourcentage des promotions pour l'affichage texte ---
            # Calcule le total des achats pour chaque canal
            total_par_canal = df_channels.groupby('Canal')['Achats'].transform('sum')
            # Calcule le pourcentage de chaque type (Normal/Promotion) par rapport au total du canal
            df_channels['Pourcentage'] = (df_channels['Achats'] / total_par_canal.replace(0, 1)) * 100
            # Crée l'étiquette de texte : affiche le % pour les promotions, rien pour le reste
            df_channels['Texte'] = df_channels.apply(lambda row: f"{row['Pourcentage']:.1f}%" if row['Type'] == 'Promotion' else '', axis=1)
            # --- NOUVEAU : Calculer les totaux pour les afficher sur le graphique ---
            df_totals = df_channels.groupby('Canal')['Achats'].sum().reset_index()

            # --- NOUVEAU : Calcul du KPI de promotion total (maintenant que les données sont prêtes) ---
            total_promo_achats = sum(promo_par_plateforme.values())
            total_normal_achats = sum(normaux_par_plateforme.values())
            total_achats = total_promo_achats + total_normal_achats
            
            # Calcul du nombre moyen d'achats par client
            nb_clients_filtres = len(df_filtered)
            achats_moyens_par_client = total_achats / nb_clients_filtres if nb_clients_filtres > 0 else 0
            pourcentage_promo_total = (total_promo_achats / total_achats) * 100 if total_achats > 0 else 0
            if 'Plainte' in df_filtered.columns:
                total_plaintes = df_filtered['Plainte'].sum()
                pourcentage_plaintes = (total_plaintes / len(df_filtered)) * 100 if len(df_filtered) > 0 else 0


            with col_kpi_promo:
                st.metric(label="Achats Moyens par Client", value=f"{achats_moyens_par_client:.1f}")
                st.metric(label="Taux d'Achats en Promotion", value=f"{pourcentage_promo_total:.1f} %")
                if 'Plainte' in df_filtered.columns:
                    st.metric(label="Taux de Plaintes", value=f"{pourcentage_plaintes:.2f} %",
                              help="Pourcentage de clients s'étant plaints dans la sélection actuelle.")
                
            # Création du graphique à barres
            fig_channels = px.bar(
                df_channels,
                x='Canal',
                y='Achats',
                color='Type',
                text='Texte',
                title="Volume des Ventes par Canal (Normal vs. Promotion)",
                labels={'Achats': 'Nombre total d\'achats'},
                barmode='stack',
                color_discrete_map={'Normal': '#99ccff', 'Promotion': '#ffcc99'} # Pastel: Bleu, Orange
            )
            fig_channels.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(size=12, color='white'),
                title_font=dict(size=18, color='white', family='Arial Black'),
                legend=dict(
                    orientation="h",
                    yanchor="top",
                    y=-0.2,
                    xanchor="center",
                    x=0.5,
                    bgcolor='rgba(0,0,0,0)',
                    borderwidth=0
                ),
                hovermode='x unified'
            )
            fig_channels.update_traces(
                textposition='inside',
                marker=dict(line=dict(width=0)),
                hovertemplate='%{y:,.0f} achats<extra></extra>'
            )
            fig_channels.update_xaxes(showgrid=False)
            fig_channels.update_yaxes(showgrid=True, gridcolor='rgba(255, 255, 255, 0.1)')

            # Ajoute les totaux au-dessus des barres empilées
            for i, total in enumerate(df_totals['Achats']):
                fig_channels.add_annotation(
                    x=df_totals['Canal'][i],
                    y=total,
                    text=f"<b>{total:,.0f}</b>",
                    showarrow=False,
                    yshift=10,
                    font=dict(size=14, color='white', family='Arial Black')
                )

            with col_chart_channels:
                st.plotly_chart(fig_channels, use_container_width=True)

            # --- NOUVEAU GRAPHIQUE : VISITES WEB PAR SEGMENT ---
            st.markdown("---")
            st.subheader("Analyse des Visites Web par Segment de Dépensier")

            # Vérifier que les colonnes nécessaires existent dans les données filtrées
            if 'Segmentation_Dépensier' in df_filtered.columns and 'Visites_Web_Mois' in df_filtered.columns:
                
                # Calculer la moyenne des visites par segment sur les données filtrées
                visites_par_segment = df_filtered.groupby('Segmentation_Dépensier')['Visites_Web_Mois'].mean().reset_index()

                # Définir un ordre logique pour l'affichage
                ordre_segment = ['Petits Dépensier', 'Moyens Dépensier', 'Grand Dépensier']
                visites_par_segment['Segmentation_Dépensier'] = pd.Categorical(visites_par_segment['Segmentation_Dépensier'], categories=ordre_segment, ordered=True)
                visites_par_segment = visites_par_segment.sort_values('Segmentation_Dépensier')

                # Créer le graphique à barres
                segment_colors = {'Petits Dépensier': '#99ff99', 'Moyens Dépensier': '#ffcc99', 'Grand Dépensier': '#ff9999'} # Pastel: Vert, Orange, Rouge
                fig_visites = px.bar(
                    visites_par_segment,
                    x='Segmentation_Dépensier',
                    y='Visites_Web_Mois',
                    color='Segmentation_Dépensier',
                    text=visites_par_segment['Visites_Web_Mois'].apply(lambda x: f'{x:.1f}'),
                    title="Nombre Moyen de Visites Web par Mois par Segment",
                    color_discrete_map=segment_colors
                )
                fig_visites.update_layout(
                    xaxis_title="Segment de Dépensier",
                    yaxis_title="Visites Moyennes par Mois",
                    showlegend=False,
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(size=12, color='white'),
                    title_font=dict(size=18, color='white', family='Arial Black'),
                    hovermode='x'
                )
                fig_visites.update_traces(
                    textposition='outside',
                    marker=dict(line=dict(width=0)),
                    hovertemplate='<b>%{x}</b><br>%{y:.1f} visites/mois<extra></extra>'
                )
                fig_visites.update_xaxes(showgrid=False)
                fig_visites.update_yaxes(showgrid=True, gridcolor='rgba(255, 255, 255, 0.1)')
                st.plotly_chart(fig_visites, use_container_width=True)

        else:
            st.warning("Aucune donnée disponible pour les filtres sélectionnés.")

    # ==============================================================================
    # --- NOUVELLE PAGE 2 : INFLUENCE DES CAMPAGNES ---
    # ==============================================================================
    elif page == "Influence des Campagnes":
        st.title("Influence des Campagnes Marketing")
        st.markdown("Analyse du nombre de réponses positives pour chaque campagne marketing, selon les segments de clients sélectionnés.")

        # --- NOUVEAU : Filtre spécifique à la page Campagne ---
        campaign_filter_options = {
            'Toutes': 'Toutes les campagnes',
            'Reponse_Campagne_1': 'Campagne 1',
            'Reponse_Campagne_2': 'Campagne 2',
            'Reponse_Campagne_3': 'Campagne 3',
            'Reponse_Campagne_4': 'Campagne 4',
            'Reponse_Campagne_5': 'Campagne 5',
            'Reponse_Derniere_Campagne': 'Dernière Campagne (6)'
        }
        selected_campaign_key = st.selectbox(
            "Choisir une campagne spécifique pour les KPIs",
            options=list(campaign_filter_options.keys()),
            format_func=lambda x: campaign_filter_options[x]
        )

        if not df_filtered.empty:
            campaign_cols = {
                'Reponse_Campagne_1': 'Campagne 1',
                'Reponse_Campagne_2': 'Campagne 2',
                'Reponse_Campagne_3': 'Campagne 3',
                'Reponse_Campagne_4': 'Campagne 4',
                'Reponse_Campagne_5': 'Campagne 5',
                'Reponse_Derniere_Campagne': 'Dernière Campagne (6)'
            }

            # --- NOUVEAU : Calcul et affichage des KPIs ---
            st.markdown("---")
            # Ligne 1 pour les KPIs de participation
            col_kpi_part1, col_kpi_part2 = st.columns(2)
            # Ligne 2 pour les KPIs financiers
            col_kpi_fin1, col_kpi_fin2, col_kpi_fin3, col_kpi_fin4 = st.columns(4)

            # --- MODIFIÉ : Calcul et affichage des KPIs en fonction de la campagne sélectionnée ---
            if selected_campaign_key != 'Toutes':
                nb_clients_filtres = len(df_filtered)
                nb_reponses = df_filtered[selected_campaign_key].sum()
                
                # Taux de participation (ou conversion) pour la campagne sélectionnée
                taux_participation = (nb_reponses / nb_clients_filtres) * 100 if nb_clients_filtres > 0 else 0
                
                # ROI
                cout_contact = df_filtered['cout par campagne'].iloc[0]
                revenu_conversion = df_filtered['revenue par campagne'].iloc[0]
                cout_total = nb_clients_filtres * cout_contact
                revenu_total = nb_reponses * revenu_conversion
                roi = ((revenu_total - cout_total) / cout_total) * 100 if cout_total > 0 else 0
                benefice = revenu_total - cout_total

                with col_kpi_part1:
                    st.metric(label=f"Participants ({campaign_filter_options[selected_campaign_key]})", value=f"{nb_reponses} clients")
                with col_kpi_part2:
                    st.metric(label=f"Taux de Participation ({campaign_filter_options[selected_campaign_key]})", value=f"{taux_participation:.2f} %")
                
                with col_kpi_fin1:
                    st.metric(label="Coût de la Campagne", value=f"{cout_total:,.0f} €".replace(',', ' '))
                with col_kpi_fin2:
                    st.metric(label="Revenu de la Campagne", value=f"{revenu_total:,.0f} €".replace(',', ' '))
                with col_kpi_fin3:
                    st.metric(label="Bénéfice de la Campagne", value=f"{benefice:,.0f} €".replace(',', ' '))
                with col_kpi_fin4:
                    st.metric(label=f"ROI ({campaign_filter_options[selected_campaign_key]})", value=f"{roi:.2f} %")
            else:
                # Si "Toutes" est sélectionné, on affiche le taux de participation global
                df_filtered['A_Participe'] = (df_filtered[list(campaign_cols.keys())].sum(axis=1) > 0).astype(int)
                nb_participants_global = df_filtered['A_Participe'].sum()
                taux_participation_global = (df_filtered['A_Participe'].mean()) * 100 if not df_filtered.empty else 0
                with col_kpi_part1:
                    st.metric(label="Participants (au moins 1 campagne)", value=f"{nb_participants_global} clients")
                with col_kpi_part2:
                    st.metric(label="Taux de Participation Global", value=f"{taux_participation_global:.2f} %",
                              help="% de clients ayant répondu à au moins une campagne.")
                with col_kpi_fin1:
                    st.info("Sélectionnez une campagne pour voir son coût.")
                with col_kpi_fin2:
                    st.info("Sélectionnez une campagne pour voir son revenu.")
                with col_kpi_fin3:
                    st.info("Sélectionnez une campagne pour voir son bénéfice.")
                with col_kpi_fin4:
                    st.info("Sélectionnez une campagne pour voir son ROI.")
            st.markdown("---")

            # Calculer le nombre de réponses pour chaque campagne
            responses = [df_filtered[col].sum() for col in campaign_cols.keys()]
            
            # Créer un DataFrame pour le graphique
            df_campaigns = pd.DataFrame({
                'Campagne': list(campaign_cols.values()),
                'Nombre de Réponses': responses
            })

            # Créer le graphique à colonnes
            campaign_colors = ['#99ccff', '#99ff99', '#ffcc99', '#ff9999', '#ffff99', '#cc99ff'] # Couleurs pastel
            fig_campaigns = px.bar(
                df_campaigns,
                x='Campagne',
                y='Nombre de Réponses',
                color='Campagne',
                text='Nombre de Réponses',
                title="Nombre de Réponses Positives par Campagne",
                color_discrete_sequence=campaign_colors
            )
            fig_campaigns.update_layout(
                xaxis_title="Campagne Marketing",
                yaxis_title="Nombre de Réponses Positives",
                showlegend=False,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(size=12, color='white'),
                title_font=dict(size=18, color='white', family='Arial Black'),
                hovermode='x'
            )
            fig_campaigns.update_traces(
                textposition='outside',
                marker=dict(line=dict(width=0)),
                hovertemplate='<b>%{x}</b><br>%{y} réponses<extra></extra>'
            )
            fig_campaigns.update_xaxes(showgrid=False)
            fig_campaigns.update_yaxes(showgrid=True, gridcolor='rgba(255, 255, 255, 0.1)')

            # --- NOUVEAU : Ajout de la ligne de seuil de rentabilité ---
            fig_campaigns.add_hline(
                y=611,
                line_dash="dash",
                annotation_text="Seuil de rentabilité (611 réponses)",
                annotation_position="bottom right",
                line_color="#ef4444",
                line_width=3,
                annotation_font=dict(size=12, color='#ef4444', family='Arial')
            )

            st.plotly_chart(fig_campaigns, use_container_width=True)

            # --- MODIFIÉ : GRAPHIQUE DE LA RÉCENCE MOYENNE PAR SEGMENT ---
            st.markdown("---")
            st.subheader("Analyse de la Récence Moyenne par Segment de Dépensier")
            st.markdown("Ce graphique compare le nombre de jours moyen écoulé depuis le dernier achat pour chaque segment. Un nombre de jours plus bas indique des clients plus réguliers.")

            if 'Jours_Dernier_Achat' in df_filtered.columns and 'Segmentation_Dépensier' in df_filtered.columns:
                # Calculer la moyenne des jours depuis le dernier achat par segment
                recence_par_segment = df_filtered.groupby('Segmentation_Dépensier')['Jours_Dernier_Achat'].mean().reset_index()

                # Définir un ordre logique pour l'affichage
                ordre_segment = ['Petits Dépensier', 'Moyens Dépensier', 'Grand Dépensier']
                recence_par_segment['Segmentation_Dépensier'] = pd.Categorical(recence_par_segment['Segmentation_Dépensier'], categories=ordre_segment, ordered=True)
                recence_par_segment = recence_par_segment.sort_values('Segmentation_Dépensier')

                # Créer le graphique à barres
                segment_colors_recency = {'Petits Dépensier': '#99ff99', 'Moyens Dépensier': '#ffcc99', 'Grand Dépensier': '#ff9999'} # Pastel: Vert, Orange, Rouge
                fig_recency = px.bar(
                    recence_par_segment,
                    x='Segmentation_Dépensier',
                    y='Jours_Dernier_Achat',
                    color='Segmentation_Dépensier',
                    text=recence_par_segment['Jours_Dernier_Achat'].apply(lambda x: f'{x:.1f} jours'),
                    title="Nombre de Jours Moyen depuis le Dernier Achat par Segment",
                    color_discrete_map=segment_colors_recency
                )
                fig_recency.update_layout(
                    xaxis_title="Segment de Dépensier",
                    yaxis_title="Jours Moyens depuis le Dernier Achat",
                    showlegend=False,
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font=dict(size=12, color='white'),
                    title_font=dict(size=18, color='white', family='Arial Black'),
                    hovermode='x'
                )
                fig_recency.update_traces(
                    textposition='outside',
                    marker=dict(line=dict(width=0)),
                    hovertemplate='<b>%{x}</b><br>%{y:.1f} jours<extra></extra>'
                )
                fig_recency.update_xaxes(showgrid=False)
                fig_recency.update_yaxes(showgrid=True, gridcolor='rgba(255, 255, 255, 0.1)')
                st.plotly_chart(fig_recency, use_container_width=True)
            else:
                st.warning("Les colonnes 'Jours_Dernier_Achat' et 'Segmentation_Dépensier' sont nécessaires pour ce graphique.")


        else:
            st.warning("Aucune donnée disponible pour les filtres sélectionnés.")

if __name__ == '__main__':
    main()
