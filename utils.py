import pandas as pd
import numpy as np

def load_data(file_path):
    """
    Charge et prétraite les données du fichier CSV
    """
    data = pd.read_csv(file_path)

    # Conversion des timestamps
    data['UTC'] = pd.to_numeric(data['UTC'])
    data['datetime'] = pd.to_datetime(data['UTC'], unit='s')

    # Nettoyage des données
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    data[numeric_columns] = data[numeric_columns].ffill()

    return data

def calculate_statistics(data):
    """
    Calcule les statistiques descriptives pour les paramètres principaux
    """
    params = [
        "Temperature[C]", "Humidity[%]", "TVOC[ppb]", "eCO2[ppm]",
        "Raw H2", "Raw Ethanol", "Pressure[hPa]", "PM1.0", "PM2.5",
        "NC0.5", "NC1.0", "NC2.5"
    ]
    stats = data[params].describe().round(2)

    # Traduction des index
    stats.index = ['Nombre', 'Moyenne', 'Écart-type', 'Minimum', 
                   '25ème percentile', 'Médiane', '75ème percentile', 'Maximum']

    return stats

def create_correlation_matrix(data):
    """
    Crée une matrice de corrélation pour les paramètres principaux
    """
    params = [
        "Temperature[C]", "Humidity[%]", "TVOC[ppb]", "eCO2[ppm]",
        "Raw H2", "Raw Ethanol", "Pressure[hPa]", "PM1.0", "PM2.5",
        "NC0.5", "NC1.0", "NC2.5", "CNT"
    ]

    return data[params].corr().round(2)

def analyze_missing_values(data):
    """
    Analyse les valeurs manquantes dans le dataset
    """
    # Calcul du nombre et du pourcentage de valeurs manquantes
    missing = pd.DataFrame({
        'Missing Count': data.isnull().sum(),
        'Missing %': (data.isnull().sum() / len(data) * 100).round(2)
    })

    # Tri par pourcentage de valeurs manquantes décroissant
    missing = missing.sort_values('Missing %', ascending=False)

    return missing

def get_alarm_stats(data):
    """
    Calcule les statistiques liées aux alarmes
    """
    total_records = len(data)
    alarm_count = data['Fire Alarm'].sum()
    alarm_percentage = (alarm_count / total_records * 100).round(2)

    return {
        'total_records': total_records,
        'alarm_count': int(alarm_count),
        'alarm_percentage': alarm_percentage
    }
