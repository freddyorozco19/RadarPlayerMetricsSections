# -*- coding: utf-8 -*-
"""

Created on Fri Jul 29 11:21:46 2022
Author: Freddy J. Orozco R.
Powered by: Win Stats

"""

import pandas as pd
import numpy as np
import streamlit as st
from radar_chart2 import Radar
import matplotlib.font_manager as font_manager
import matplotlib.patheffects as path_effects
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit.components.v1 as components
import io

##################################################################################################################################
## Import resources
font_path = 'keymer-bold.otf'  # Your font path goes here
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)

font_path = 'BasierCircle-Italic.ttf'  # Your font path goes here
font_manager.fontManager.addfont(font_path)
prop1 = font_manager.FontProperties(fname=font_path)

##################################################################################################################################
#Import data

# df1  = pd.read_excel('LigasConmebolApertura22_AllMetricsDataCleaning/ArgentinaApertura22_AllMetricsCalculated_DataCleaning.xlsx')
# df2  = pd.read_excel('LigasConmebolApertura22_AllMetricsDataCleaning/BoliviaApertura22_AllMetricsCalculated_DataCleaning.xlsx')
# df3  = pd.read_excel('LigasConmebolApertura22_AllMetricsDataCleaning/Brasil22_F16_130722_AllMetricsCalculated_DataCleaning.xlsx')
# df4  = pd.read_excel('LigasConmebolApertura22_AllMetricsDataCleaning/ChileApertura22_AllMetricsCalculated_DataCleaning.xlsx')
# df5  = pd.read_excel('LigasConmebolApertura22_AllMetricsDataCleaning/ColombiaApertura22_AllMetricsCalculated_DataCleaning.xlsx')
# df6  = pd.read_excel('LigasConmebolApertura22_AllMetricsDataCleaning/EcuadorApertura22_AllMetricsCalculated_DataCleaning.xlsx')
# df7  = pd.read_excel('LigasConmebolApertura22_AllMetricsDataCleaning/ParaguayApertura22_AllMetricsCalculated_DataCleaning.xlsx')
# df8  = pd.read_excel('LigasConmebolApertura22_AllMetricsDataCleaning/PeruApertura22_AllMetricsCalculated_DataCleaning.xlsx')
# df9  = pd.read_excel('LigasConmebolApertura22_AllMetricsDataCleaning/UruguayApertura22_160622_AllMetricsCalculated_DataCleaning.xlsx')
# df10 = pd.read_excel('LigasConmebolApertura22_AllMetricsDataCleaning/VenezuelaApertura22_160622_AllMetricsCalculated_DataCleaning.xlsx')

#df1 = pd.read_excel('LigasConmebolApertura22_AllMetricsDataCleaning/ColombiaApertura22_AllMetricsCalculated_DataCleaning.xlsx')
df1 = pd.read_excel('Storage/LigaColombia22_FullSeasonT_AllMetricsCalculated_DataCleaning.xlsx')
df2 = pd.read_excel('Storage/LigaArgentina22_FullSeason_AllMetricsCalculated_DataCleaning.xlsx')
df3 = pd.read_excel('Storage/LigaBolivia22_FullSeason_AllMetricsCalculated_DataCleaning.xlsx')
df4 = pd.read_excel('Storage/LigaChile22_FullSeason_AllMetricsCalculated_DataCleaning.xlsx')
df5 = pd.read_excel('Storage/LigaEcuador22_FullSeason_AllMetricsCalculated_DataCleaning.xlsx')
df6 = pd.read_excel('Storage/LigaParaguay22_FullSeason_AllMetricsCalculated_DataCleaning.xlsx')
df7 = pd.read_excel('Storage/LigaPerú22_FullSeason_AllMetricsCalculated_DataCleaning.xlsx')
df8 = pd.read_excel('Storage/LigaUruguay22_FullSeason_AllMetricsCalculated_DataCleaning.xlsx')
df9 = pd.read_excel('Storage/LigaVenezuela22_FullSeason_AllMetricsCalculated_DataCleaning.xlsx')
df10 = pd.read_excel('Storage/LigaBrasil22_FullSeason_AllMetricsCalculated_DataCleaning.xlsx')
df11 = pd.read_excel('Storage/LigaMéxico22_FullApertura_AllMetricsCalculated_DataCleaning.xlsx')
df12 = pd.read_excel('Storage/MLS22_FullSeason_AllMetricsCalculated_DataCleaning.xlsx')

######################################################################################################################################################################################################################################################################################################################################################################################################
#Streamlit configuration
st.set_page_config(layout="wide")
st.markdown("""---""")

with st.sidebar:
    
    st.image("https://i.ibb.co/qjvrH5y/win.png", width=250) 
    
    #COUNTRY CHOISE
    countries = ["Todos los países", "Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador", "Paraguay", "Perú", "Uruguay", "Venezuela", "ColombiaB", "Colombia2"]
    cousel = st.selectbox("Seleccionar país:", countries)
    if cousel == "Colombia":
        df = df1
    elif cousel == "Argentina":
        df = df2
    elif cousel == "Bolivia":
        df = df3
    elif cousel == "Chile":
        df = df4
    elif cousel == "Ecuador":
        df = df5
    elif cousel == "Paraguay":
        df = df6
    elif cousel == "Perú":
        df = df7
    elif cousel == "Uruguay":
        df = df8
    elif cousel == "Venezuela":
        df = df9
    elif cousel == "Brasil":
        df = df10
    elif cousel == "México":
        df = df11
    elif cousel == "Estados Unidos":
        df = df12     
    elif cousel == "Todos los países":
        df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11], axis = 0)
        
    #SELECT AGE
    agesel = st.slider('Filtro de edad:', 15, 50, (15, 50), 1)   
    df = df[df['Age'] <= agesel[1]]
    df = df[df['Age'] >= agesel[0]]
    
    #SELECT MINS
    minsel = st.slider('Filtro de minutos (%):', 0, 100)
    maxmin = df['Minutes played'].max() + 5
    minsel1 = (minsel*maxmin)/100
    df = df[df['Minutes played'] >= minsel1].reset_index()
    
    #SELECT POSITION OPTION
    positions = list(df['Pos1'].drop_duplicates())
    positions.append("ALL")
    positions.sort()
    seldf0 = st.selectbox("Filtrar por posición:", positions)
    
    dftres = df
    
    if seldf0 == 'ALL':
        df = dftres
    else:
        df = dftres[dftres['Pos1'] == seldf0].reset_index()
        dfax = df[['Player', 'Team', 'Pos1', 'Pos2', 'Age']]
    
    
    #st.write(df)
    dfccc = df
    dfcuatro = df
        
    #SELECT TEAM
    teams = list(df['Team'].drop_duplicates())
    teamsel1 = st.selectbox('Selecciona un equipo:', teams)
    df = df[df['Team'] == teamsel1]
    
    #SELECT PLAYER
    players = list(df['Player'].drop_duplicates())            
    playersel = st.selectbox('Selecciona un jugador:', players)
    df = df[df['Player'] == playersel]
    
    #GET AUX INFO
    dfaux = df[['Player', 'Team', 'Pos1', 'Age', '90s']]


##################################################################################################################################
# Data Cleaning - Exploratory Data Analysis 

#Filtrar métricas normalizadas por 90 minutos
dfp90 = df[['90s',
            'Successful attacking actions per 90', 'Offensive duels per 90', 'Offensive duels won per 90', 'Touches in box per 90', 'Goals per 90', 'Non-penalty goals per 90', 'Head goals per 90', 'xG per 90', 'NPxG per 90', 'Shots per 90', 'Shots on target per 90', 
            'Successful defensive actions per 90', 'Defensive duels per 90', 'Defensive duels won per 90', 'Sliding tackles per 90', 'Shots blocked per 90', 'Interceptions per 90', 
            'Duels per 90', 'Duels won per 90', 'Aerial duels per 90', 'Aerial duels won per 90', 'Fouls per 90', 'Dribbles per 90', 'Successful dribbles per 90', 'Progressive runs per 90', 'Received passes per 90', 'Received long passes per 90', 'Fouls suffered per 90', 
            'Assists per 90', 'xA per 90', 'Second assists per 90', 'Third assists per 90', 'Crosses per 90', 'Crosses completed per 90', 'Crosses to goalie box per 90', 'Crosses from left flank per 90', 'Crosses from right flank per 90', 'Shot assists per 90', 'Key passes per 90', 'Smart passes per 90', 'Smart passes completed per 90', 'Passes to penalty area per 90', 'Passes to penalty area completed per 90', 'Through passes per 90', 'Through passes completed per 90', 'Deep completions per 90', 'Deep completed crosses per 90',
            'Passes per 90', 'Passes completed per 90', 'Forward passes per 90', 'Forward passes completed per 90', 'Back passes per 90', 'Back passes completed per 90', 'Lateral passes per 90', 'Lateral passes completed per 90', 'Short / medium passes per 90', 'Short / medium passes completed per 90', 'Long passes per 90', 'Long passes completed per 90', 'Passes to final third per 90', 'Passes to final third completed per 90', 'Progressive passes per 90', 'Progressive passes completed per 90',
            'Free kicks per 90', 'Direct free kicks per 90',
            'Conceded goals per 90', 'Shots against per 90', 'xG against per 90', 'Prevented goals per 90', 'Back passes received as GK per 90', 'Exits per 90', 'Aerial duels per 90.1',
            'Yellow cards per 90', 'Red cards per 90']]

#Filtrar por acciones ofensivas
dfofe = df[['Successful attacking actions per 90', 'Offensive duels per 90', 'Offensive duels won per 90', 'Touches in box per 90', 'Goals per 90', 'Non-penalty goals per 90', 'Head goals per 90', 'xG per 90', 'NPxG per 90', 'Shots per 90', 'Shots on target per 90']]
dfofel = dfofe.columns
dfofeccc = dfccc[['Successful attacking actions per 90', 'Offensive duels per 90', 'Offensive duels won per 90', 'Touches in box per 90', 'Goals per 90', 'Non-penalty goals per 90', 'Head goals per 90', 'xG per 90', 'NPxG per 90', 'Shots per 90', 'Shots on target per 90', ]]
dfofelccc = dfofeccc.columns

#Filtrar por acciones defensivas
dfdef = df[['Successful defensive actions per 90', 'Defensive duels per 90', 'Defensive duels won per 90', 'Sliding tackles per 90', 'Shots blocked per 90', 'Interceptions per 90']]
dfdefl = dfdef.columns
dfdefccc = dfccc[['Successful defensive actions per 90', 'Defensive duels per 90', 'Defensive duels won per 90', 'Sliding tackles per 90', 'Shots blocked per 90', 'Interceptions per 90']]
dfdeflccc = dfdefccc.columns

#Filtrar por acciones de posesión
dfpos = df[['Duels per 90', 'Duels won per 90', 'Aerial duels per 90', 'Aerial duels won per 90', 'Fouls per 90', 'Dribbles per 90', 'Successful dribbles per 90', 'Progressive runs per 90', 'Received passes per 90', 'Received long passes per 90', 'Fouls suffered per 90']]
dfposl = dfpos.columns
dfposccc = dfccc[['Duels per 90', 'Duels won per 90', 'Aerial duels per 90', 'Aerial duels won per 90', 'Fouls per 90', 'Dribbles per 90', 'Successful dribbles per 90', 'Progressive runs per 90', 'Received passes per 90', 'Received long passes per 90', 'Fouls suffered per 90']]
dfposlccc = dfposccc.columns

#Filtrar por acciones de generación
dfcre = df[['Assists per 90', 'xA per 90', 'Second assists per 90', 'Third assists per 90', 'Crosses per 90', 'Crosses completed per 90', 'Crosses to goalie box per 90', 'Shot assists per 90', 'Key passes per 90', 'Smart passes per 90', 'Smart passes completed per 90', 'Passes to penalty area per 90', 'Passes to penalty area completed per 90', 'Through passes per 90', 'Through passes completed per 90', 'Deep completions per 90', 'Deep completed crosses per 90']]
dfcrel = dfcre.columns
dfcreccc = dfccc[['Assists per 90', 'xA per 90', 'Second assists per 90', 'Third assists per 90', 'Crosses per 90', 'Crosses completed per 90', 'Crosses to goalie box per 90', 'Shot assists per 90', 'Key passes per 90', 'Smart passes per 90', 'Smart passes completed per 90', 'Passes to penalty area per 90', 'Passes to penalty area completed per 90', 'Through passes per 90', 'Through passes completed per 90', 'Deep completions per 90', 'Deep completed crosses per 90']]
dfcrelccc = dfcreccc.columns

#Filtrar por acciones de distribución
dfdis = df[['Passes per 90', 'Passes completed per 90', 'Forward passes per 90', 'Forward passes completed per 90', 'Back passes per 90', 'Back passes completed per 90', 'Lateral passes per 90', 'Lateral passes completed per 90', 'Short / medium passes per 90', 'Short / medium passes completed per 90', 'Long passes per 90', 'Long passes completed per 90', 'Passes to final third per 90', 'Passes to final third completed per 90', 'Progressive passes per 90', 'Progressive passes completed per 90',]]
dfdisl = dfdis.columns
dfdisccc = dfccc[['Passes per 90', 'Passes completed per 90', 'Forward passes per 90', 'Forward passes completed per 90', 'Back passes per 90', 'Back passes completed per 90', 'Lateral passes per 90', 'Lateral passes completed per 90', 'Short / medium passes per 90', 'Short / medium passes completed per 90', 'Long passes per 90', 'Long passes completed per 90', 'Passes to final third per 90', 'Passes to final third completed per 90', 'Progressive passes per 90', 'Progressive passes completed per 90',]]
dfdislccc = dfdisccc.columns

#Filtrar por acciones complementarias
dfoth = df[['90s', 'Yellow cards per 90', 'Red cards per 90', 'Free kicks per 90', 'Direct free kicks per 90']]
dfothl = dfoth.columns
dfothccc = dfccc[['90s', 'Yellow cards per 90', 'Red cards per 90', 'Free kicks per 90', 'Direct free kicks per 90']]
dfothlccc = dfothccc.columns



df['Team'] = df['Team'].astype(str)
#df['Pos0'] = df['Pos0'].astype(str)
dfccc['Team'] = dfccc['Team'].astype(str)
#dfccc['Pos0'] = dfccc['Pos0'].astype(str)    

#GET AUX INFO PLAYER
#dfaux = df[['Player', 'Team', 'Pos1', 'Age', '90s']]
dfmins = dfaux['90s']
dfmins = dfmins*90

dfauxccc = dfccc[['Player', 'Team', 'Pos1', 'Age', '90s']]
dfminsccc = dfauxccc['90s']
dfminsccc = dfminsccc*90

#Valores por acciones ofensivas
valuessofe = dfofe.iloc[0,:]
valuessofe2 = round(dfofeccc.mean(), 2)

#Valores por acciones defensivas
valuessdef = dfdef.iloc[0,:]
valuessdef2 = round(dfdefccc.mean(), 2)

#Valores por acciones de posesión
valuesspos = dfpos.iloc[0,:]
valuesspos2 = round(dfposccc.mean(), 2)

#Valores por acciones de generación
valuesscre = dfcre.iloc[0,:]
valuesscre2 = round(dfcreccc.mean(), 2)

#Valores por acciones de distribución
valuessdis = dfdis.iloc[0,:]
valuessdis2 = round(dfdisccc.mean(), 2)

#Valores por acciones complementarias
valuessoth = dfoth.iloc[0,:]
valuessoth2 = round(dfothccc.mean(), 2)

#Valores

##################################################################################################################################

#dfmn = df5.mean()
#df5.loc[-1] = round(dfmn, 2)


#st.write(len(dfccc))
#st.dataframe(dfccc)
#st.write(len(df))
#st.dataframe(df)




##################################################################################################################################
##Radar process   

#Obtener valores minimos y máximos de métricas ofensivas        
lowwofe = []
highhofe = []
for an in range(len(dfofeccc.columns)):
    lowwofe.append(min(dfofeccc.iloc[:,an]))
    highhofe.append(max(dfofeccc.iloc[:,an]))    

#Obtener valores minimos y máximos de métricas defensivas        
lowwdef = []
highhdef = []
for an in range(len(dfdefccc.columns)):
    lowwdef.append(min(dfdefccc.iloc[:,an]))
    highhdef.append(max(dfdefccc.iloc[:,an]))    

#Obtener valores minimos y máximos de métricas de posesión        
lowwpos = []
highhpos = []
for an in range(len(dfposccc.columns)):
    lowwpos.append(min(dfposccc.iloc[:,an]))
    highhpos.append(max(dfposccc.iloc[:,an]))    
    
#Obtener valores minimos y máximos de métricas de generación        
lowwcre = []
highhcre = []
for an in range(len(dfcreccc.columns)):
    lowwcre.append(min(dfcreccc.iloc[:,an]))
    highhcre.append(max(dfcreccc.iloc[:,an]))    

#Obtener valores minimos y máximos de métricas de distribución
lowwdis = []
highhdis = []
for an in range(len(dfdisccc.columns)):
    lowwdis.append(min(dfdisccc.iloc[:,an]))
    highhdis.append(max(dfdisccc.iloc[:,an]))    

#Obtener valores minimos y máximos de métricas complementarias        
lowwoth = []
highhoth = []
for an in range(len(dfothccc.columns)):
    lowwoth.append(min(dfothccc.iloc[:,an]))
    highhoth.append(max(dfothccc.iloc[:,an]))        



rangparamofe = len(dfofelccc)
rangparamdef = len(dfdeflccc)
rangparampos = len(dfposlccc)
rangparamcre = len(dfcrelccc)
rangparamdis = len(dfdislccc)
rangparamoth = len(dfothlccc)

#Radar ofensivo
radarofe = Radar(dfofelccc, lowwofe, highhofe,
              # whether to round any of the labels to integers instead of decimal places
              round_int=[False]*rangparamofe,
              num_rings=4,  # the number of concentric circles (excluding center circle)
              # if the ring_width is more than the center_circle_radius then
              # the center circle radius will be wider than the width of the concentric circles
              ring_width=1, center_circle_radius=1)

#Radar defensivo
radardef = Radar(dfdeflccc, lowwdef, highhdef,
              # whether to round any of the labels to integers instead of decimal places
              round_int=[False]*rangparamdef,
              num_rings=4,  # the number of concentric circles (excluding center circle)
              # if the ring_width is more than the center_circle_radius then
              # the center circle radius will be wider than the width of the concentric circles
              ring_width=1, center_circle_radius=1)


#Radar de posesión
radarpos = Radar(dfposlccc, lowwpos, highhpos,
              # whether to round any of the labels to integers instead of decimal places
              round_int=[False]*rangparampos,
              num_rings=4,  # the number of concentric circles (excluding center circle)
              # if the ring_width is more than the center_circle_radius then
              # the center circle radius will be wider than the width of the concentric circles
              ring_width=1, center_circle_radius=1)

#Radar de generación
radarcre = Radar(dfcrelccc, lowwcre, highhcre,
              # whether to round any of the labels to integers instead of decimal places
              round_int=[False]*rangparamcre,
              num_rings=4,  # the number of concentric circles (excluding center circle)
              # if the ring_width is more than the center_circle_radius then
              # the center circle radius will be wider than the width of the concentric circles
              ring_width=1, center_circle_radius=1)

#Radar de distribución
radardis = Radar(dfdislccc, lowwdis, highhdis,
              # whether to round any of the labels to integers instead of decimal places
              round_int=[False]*rangparamdis,
              num_rings=4,  # the number of concentric circles (excluding center circle)
              # if the ring_width is more than the center_circle_radius then
              # the center circle radius will be wider than the width of the concentric circles
              ring_width=1, center_circle_radius=1)


#Radar complementario
radaroth = Radar(dfothlccc, lowwoth, highhoth,
              # whether to round any of the labels to integers instead of decimal places
              round_int=[False]*rangparamoth,
              num_rings=4,  # the number of concentric circles (excluding center circle)
              # if the ring_width is more than the center_circle_radius then
              # the center circle radius will be wider than the width of the concentric circles
              ring_width=1, center_circle_radius=1)

space0, space1, space2 = st.columns((0.6, 0.6, 0.6))


with space0:
    fig, ax = radarofe.setup_axis()  # format axis as a radar
    fig.set_facecolor('#050E1E')
    fig.set_dpi(600)

    rings_inner = radarofe.draw_circles(ax=ax, facecolor=(1,1,1,0), edgecolor='#222229')  # draw circles
    radar_output = radarofe.draw_radar_compare(valuessofe, valuessofe2, ax=ax,
                                            kwargs_radar={'facecolor': '#FF0046', 'alpha' : 0.5},
                                            kwargs_compare={'facecolor': '#182F56', 'alpha' : 0.5},
                                            )  # draw the radar
    radar_poly, radar_poly2, vertices, vertices2 = radar_output
    # range_labels = radar.draw_range_labels(ax=ax, fontsize=18,
    #                                        fontproperties=prop)  # draw the range labels
    param_labels = radarofe.draw_param_labels(ax=ax, fontsize=15, color=(1,1,1,0.8),
                                           fontproperties=prop)  # draw the param labels

    vert = vertices.tolist()
    dfver = pd.DataFrame(vert, columns=['X', 'Y'])
    uno = dfver['X'].tolist()
    dos = dfver['Y'].tolist()

    ax.scatter(vertices[:, 0], vertices[:, 1], c='#FF0046', edgecolors='#050E1E', s=120, alpha=0.5)
    ax.scatter(vertices2[:, 0], vertices2[:, 1], c='#182F56', edgecolors='#050E1E', s=120, alpha=0.5)

    #st.write(lowwofe)
    #st.write(highhofe)

    st.pyplot(fig, bbox_inches="tight", pad_inches=0.05, dpi=600, format="png")   
    
with space1:
    fig, ax = radardef.setup_axis()  # format axis as a radar
    fig.set_facecolor('#050E1E')
    fig.set_dpi(600)

    rings_inner = radardef.draw_circles(ax=ax, facecolor=(1,1,1,0), edgecolor='#222229')  # draw circles
    radar_output = radardef.draw_radar_compare(valuessdef, valuessdef2, ax=ax,
                                            kwargs_radar={'facecolor': '#FF0046', 'alpha' : 0.5},
                                            kwargs_compare={'facecolor': '#182F56', 'alpha' : 0.5},
                                            )  # draw the radar
    radar_poly, radar_poly2, vertices, vertices2 = radar_output
    # range_labels = radar.draw_range_labels(ax=ax, fontsize=18,
    #                                        fontproperties=prop)  # draw the range labels
    param_labels = radardef.draw_param_labels(ax=ax, fontsize=15, color=(1,1,1,0.8),
                                           fontproperties=prop)  # draw the param labels

    vert = vertices.tolist()
    dfver = pd.DataFrame(vert, columns=['X', 'Y'])
    uno = dfver['X'].tolist()
    dos = dfver['Y'].tolist()

    ax.scatter(vertices[:, 0], vertices[:, 1], c='#FF0046', edgecolors='#050E1E', s=120, alpha=0.5)
    ax.scatter(vertices2[:, 0], vertices2[:, 1], c='#182F56', edgecolors='#050E1E', s=120, alpha=0.5)

    #st.write(lowwdef)
    #st.write(highhdef)

    st.pyplot(fig, bbox_inches="tight", pad_inches=0.05, dpi=600, format="png")       
    
    
with space2:
    fig, ax = radarpos.setup_axis()  # format axis as a radar
    fig.set_facecolor('#050E1E')
    fig.set_dpi(600)

    rings_inner = radarpos.draw_circles(ax=ax, facecolor=(1,1,1,0), edgecolor='#222229')  # draw circles
    radar_output = radarpos.draw_radar_compare(valuesspos, valuesspos2, ax=ax,
                                            kwargs_radar={'facecolor': '#FF0046', 'alpha' : 0.5},
                                            kwargs_compare={'facecolor': '#182F56', 'alpha' : 0.5},
                                            )  # draw the radar
    radar_poly, radar_poly2, vertices, vertices2 = radar_output
    # range_labels = radar.draw_range_labels(ax=ax, fontsize=18,
    #                                        fontproperties=prop)  # draw the range labels
    param_labels = radarpos.draw_param_labels(ax=ax, fontsize=15, color=(1,1,1,0.8),
                                           fontproperties=prop)  # draw the param labels

    vert = vertices.tolist()
    dfver = pd.DataFrame(vert, columns=['X', 'Y'])
    uno = dfver['X'].tolist()
    dos = dfver['Y'].tolist()

    ax.scatter(vertices[:, 0], vertices[:, 1], c='#FF0046', edgecolors='#050E1E', s=120, alpha=0.5)
    ax.scatter(vertices2[:, 0], vertices2[:, 1], c='#182F56', edgecolors='#050E1E', s=120, alpha=0.5)


    st.pyplot(fig, bbox_inches="tight", pad_inches=0.05, dpi=600, format="png") 
    #st.write(lowwpos)
    #st.write(highhpos)


space3, space4, space5 = st.columns((0.6, 0.6, 0.6))
      
with space3:
    fig, ax = radarcre.setup_axis()  # format axis as a radar
    fig.set_facecolor('#050E1E')
    fig.set_dpi(600)

    rings_inner = radarcre.draw_circles(ax=ax, facecolor=(1,1,1,0), edgecolor='#222229')  # draw circles
    radar_output = radarcre.draw_radar_compare(valuesscre, valuesscre2, ax=ax,
                                            kwargs_radar={'facecolor': '#FF0046', 'alpha' : 0.5},
                                            kwargs_compare={'facecolor': '#182F56', 'alpha' : 0.5},
                                            )  # draw the radar
    radar_poly, radar_poly2, vertices, vertices2 = radar_output
    # range_labels = radar.draw_range_labels(ax=ax, fontsize=18,
    #                                        fontproperties=prop)  # draw the range labels
    param_labels = radarcre.draw_param_labels(ax=ax, fontsize=15, color=(1,1,1,0.8),
                                           fontproperties=prop)  # draw the param labels

    vert = vertices.tolist()
    dfver = pd.DataFrame(vert, columns=['X', 'Y'])
    uno = dfver['X'].tolist()
    dos = dfver['Y'].tolist()

    ax.scatter(vertices[:, 0], vertices[:, 1], c='#FF0046', edgecolors='#050E1E', s=120, alpha=0.5)
    ax.scatter(vertices2[:, 0], vertices2[:, 1], c='#182F56', edgecolors='#050E1E', s=120, alpha=0.5)

    #st.write(lowwcre)
    #st.write(highhcre)

    st.pyplot(fig, bbox_inches="tight", pad_inches=0.05, dpi=600, format="png")   
    
with space4:
    fig, ax = radardis.setup_axis()  # format axis as a radar
    fig.set_facecolor('#050E1E')
    fig.set_dpi(600)

    rings_inner = radardis.draw_circles(ax=ax, facecolor=(1,1,1,0), edgecolor='#222229')  # draw circles
    radar_output = radardis.draw_radar_compare(valuessdis, valuessdis2, ax=ax,
                                            kwargs_radar={'facecolor': '#FF0046', 'alpha' : 0.5},
                                            kwargs_compare={'facecolor': '#182F56', 'alpha' : 0.5},
                                            )  # draw the radar
    radar_poly, radar_poly2, vertices, vertices2 = radar_output
    # range_labels = radar.draw_range_labels(ax=ax, fontsize=18,
    #                                        fontproperties=prop)  # draw the range labels
    param_labels = radardis.draw_param_labels(ax=ax, fontsize=15, color=(1,1,1,0.8),
                                           fontproperties=prop)  # draw the param labels

    vert = vertices.tolist()
    dfver = pd.DataFrame(vert, columns=['X', 'Y'])
    uno = dfver['X'].tolist()
    dos = dfver['Y'].tolist()

    ax.scatter(vertices[:, 0], vertices[:, 1], c='#FF0046', edgecolors='#050E1E', s=120, alpha=0.5)
    ax.scatter(vertices2[:, 0], vertices2[:, 1], c='#182F56', edgecolors='#050E1E', s=120, alpha=0.5)

    #st.write(lowwdis)
    #st.write(highhdis)

    st.pyplot(fig, bbox_inches="tight", pad_inches=0.05, dpi=600, format="png")       
    
    
with space5:
    fig, ax = radaroth.setup_axis()  # format axis as a radar
    fig.set_facecolor('#050E1E')
    fig.set_dpi(600)

    rings_inner = radaroth.draw_circles(ax=ax, facecolor=(1,1,1,0), edgecolor='#222229')  # draw circles
    radar_output = radaroth.draw_radar_compare(valuessoth, valuessoth2, ax=ax,
                                            kwargs_radar={'facecolor': '#FF0046', 'alpha' : 0.5},
                                            kwargs_compare={'facecolor': '#182F56', 'alpha' : 0.5},
                                            )  # draw the radar
    radar_poly, radar_poly2, vertices, vertices2 = radar_output
    # range_labels = radar.draw_range_labels(ax=ax, fontsize=18,
    #                                        fontproperties=prop)  # draw the range labels
    param_labels = radaroth.draw_param_labels(ax=ax, fontsize=15, color=(1,1,1,0.8),
                                           fontproperties=prop)  # draw the param labels

    vert = vertices.tolist()
    dfver = pd.DataFrame(vert, columns=['X', 'Y'])
    uno = dfver['X'].tolist()
    dos = dfver['Y'].tolist()

    ax.scatter(vertices[:, 0], vertices[:, 1], c='#FF0046', edgecolors='#050E1E', s=120, alpha=0.5)
    ax.scatter(vertices2[:, 0], vertices2[:, 1], c='#182F56', edgecolors='#050E1E', s=120, alpha=0.5)

    #st.write(lowwoth)
    #st.write(highhoth)

    st.pyplot(fig, bbox_inches="tight", pad_inches=0.05, dpi=600, format="png") 
    
    
st.table(dfaux.style.set_precision(2)) 

   
s01, s02, s03 = st.columns((0.6, 0.6, 0.6))
with s01:
    coldfofe = list(dfofeccc.columns)
    coldfofe = pd.Series(coldfofe)
    lowwofe = pd.Series(lowwofe)
    highhofe = pd.Series(highhofe)
    valueofe = pd.Series(valuessofe.values)
    meanofe = pd.Series(valuessofe2.values)
    coldfofe = pd.concat([coldfofe, lowwofe, highhofe, valueofe, meanofe], axis=1)
    coldfofe.columns=['Métrica', 'Min', 'Max', 'Valor', 'Promedio']
    st.table(coldfofe.style.set_precision(2))
    
with s02:
    coldfdef = list(dfdefccc.columns)
    coldfdef = pd.Series(coldfdef)
    lowwdef = pd.Series(lowwdef)
    highhdef = pd.Series(highhdef)
    valuedef = pd.Series(valuessdef.values)
    meandef = pd.Series(valuessdef2.values)
    coldfdef = pd.concat([coldfdef, lowwdef, highhdef, valuedef, meandef], axis=1)
    coldfdef.columns=['Métrica', 'Min', 'Max', 'Valor', 'Promedio']
    st.table(coldfdef.style.set_precision(2))
    
with s03:
    coldfpos = list(dfposccc.columns)
    coldfpos = pd.Series(coldfpos)
    lowwpos = pd.Series(lowwpos)
    highhpos = pd.Series(highhpos)
    valuepos = pd.Series(valuesspos.values)
    meanpos = pd.Series(valuesspos2.values)
    coldfpos = pd.concat([coldfpos, lowwpos, highhpos, valuepos, meanpos], axis=1)
    coldfpos.columns=['Métrica', 'Min', 'Max', 'Valor', 'Promedio']
    st.table(coldfpos.style.set_precision(2))
    
    
s04, s05, s06 = st.columns((0.6, 0.6, 0.6))
    
with s04:
    coldfcre = list(dfcreccc.columns)
    coldfcre = pd.Series(coldfcre)
    lowwcre = pd.Series(lowwcre)
    highhcre = pd.Series(highhcre)
    valuecre = pd.Series(valuesscre.values)
    meancre = pd.Series(valuesscre2.values)
    coldfcre = pd.concat([coldfcre, lowwcre, highhcre, valuecre, meancre], axis=1)
    coldfcre.columns=['Métrica', 'Min', 'Max', 'Valor', 'Promedio']
    st.table(coldfcre.style.set_precision(2))
    
with s05:
    coldfdis = list(dfdisccc.columns)
    coldfdis = pd.Series(coldfdis)
    lowwdis = pd.Series(lowwdis)
    highhdis = pd.Series(highhdis)
    valuedis = pd.Series(valuessdis.values)
    meandis = pd.Series(valuessdis2.values)
    coldfdis = pd.concat([coldfdis, lowwdis, highhdis, valuedis, meandis], axis=1)
    coldfdis.columns=['Métrica', 'Min', 'Max', 'Valor', 'Promedio']
    st.table(coldfdis.style.set_precision(2))
    
with s06:
    coldfoth = list(dfothccc.columns)
    coldfoth = pd.Series(coldfoth)
    lowwoth = pd.Series(lowwoth)
    highhoth = pd.Series(highhoth)
    valueoth = pd.Series(valuessoth.values)
    meanoth = pd.Series(valuessoth2.values)
    coldfoth = pd.concat([coldfoth, lowwoth, highhoth, valueoth, meanoth], axis=1)
    coldfoth.columns=['Métrica', 'Min', 'Max', 'Valor', 'Promedio']
    st.table(coldfoth.style.set_precision(2))
    
