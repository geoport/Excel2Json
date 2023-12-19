from pandas import read_excel
import os
import json
from site_investigation import convert_site_investigation_data


def convert_project_tab(file_path):
    df = read_excel(file_path, sheet_name="project", header=None)
    investigation_category = (df.iloc[1, 1],)
    data = {
        "projectData": {
            "geologyEngineer": df.iloc[0, 1],
        }
    }

    return data, investigation_category


def convert_building_data(file_path):
    df = read_excel(file_path, sheet_name="Building", header=None)

    data = {
        "basementFloorNumber": df.iloc[0, 1],
        "totalFloorNumber": df.iloc[1, 1],
        "buildingType": df.iloc[2, 1],
        "buildingUsageClass": df.iloc[3, 1],
        "buildingImportanceFactor": df.iloc[4, 1],
        "buildingHeightClass": df.iloc[5, 1],
    }

    return data


def convert_seismic_data(file_path):
    df = read_excel(file_path, sheet_name="Seismicity", header=None)

    return {"earthquakeMagnitude": df.iloc[0, 1]}


def convert_site_tab(file_path):
    df = read_excel(file_path, sheet_name="ConstructionSite", header=None)

    data = {
        "landSlope": df.iloc[0, 1],
        "latitude": df.iloc[1, 1],
        "longitude": df.iloc[2, 1],
        "pafta": df.iloc[3, 1],
        "ada": df.iloc[4, 1],
        "parsel": df.iloc[5, 1],
        "city": df.iloc[6, 1],
        "county": df.iloc[7, 1],
        "neighborhood": df.iloc[8, 1],
    }

    return data


def convert_litology_tab(file_path):
    df = read_excel(file_path, sheet_name="Litology")

    borehole_numbers = df["Sondaj No"].unique()

    data = {}

    for no in borehole_numbers:
        litologies = []
        df_borehole = df[df["Sondaj No"] == no]
        for _, row in df_borehole.iterrows():
            litologies.append(
                {
                    "depth": row["Derinlik"],
                    "litology": row["Litoloji"],
                    "formation": row["Formasyon"],
                }
            )
        data[no] = litologies

    return data


# Xlsx uzantısı kullanmadan dosya adı girilmesi gerekiyor.
def convert_data(file_name):
    file_path = os.path.join("excels", file_name + ".xlsx")
    data, indevstigation_category = convert_project_tab(file_path)

    data["constructionFieldData"] = convert_site_tab(file_path)
    data["buildingData"] = convert_building_data(file_path)
    data["seismicData"] = convert_seismic_data(file_path)
    data["litologyData"] = convert_litology_tab(file_path)
    data["siteInvestigationData"] = convert_site_investigation_data(file_path)

    data["siteInvestigationData"]["indevstigationCategory"] = indevstigation_category

    with open(f"jsons/{file_name}.json", "w") as f:
        json.dump(data, f, indent=4)

    return data
