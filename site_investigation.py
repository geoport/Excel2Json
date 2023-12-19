import pandas


def convert_borehole_data(file_path):
    df = pandas.read_excel(file_path, sheet_name="Boreholes")

    data = []

    for _, row in df.iterrows():
        litology = {
            "boreholeNumber": row["No"],
            "boreHoleDepth": row["Derinlik"],
        }
        data.append(litology)

    return data


def convert_lab_data(file_path):
    df = pandas.read_excel(file_path, sheet_name="LabExp")

    data = []

    for _, row in df.iterrows():
        exp = {
            "boreholeNumber": row["Sondaj No"],
            "depth": row["Derinlik"],
            "fineContent": row["Kil"],
            "liquidLimit": row["LL"],
            "plasticLimit": row["PL"],
            "waterContent": row["Wn"],
            "soilClass": row["Sınıflama"],
            "dryUnitWeight": row["GammaDry(g/cm3)"],
            "naturalUnitWeight": row["GammaNatural(g/cm3)"],
            "cohesion": row["Cohesion(kPa)"],
            "frictionAngle": row["Friction Angle"],
        }
        data.append(exp)

    return data


def convert_spt_data(file_path):
    df = pandas.read_excel(file_path, sheet_name="SPT")

    data = {}
    borehole_numbers = df["Sondaj No"].unique()
    for no in borehole_numbers:
        spts = []
        df_borehole = df[df["Sondaj No"] == no]
        for _, row in df_borehole.iterrows():
            spts.append(
                {
                    "depth": row["Derinlik"],
                    "N": row["N"],
                }
            )
        data[no] = spts

    return data


def convert_masw_data(file_path):
    df = pandas.read_excel(file_path, sheet_name="MASW")

    data = {}
    borehole_numbers = df["Profil No"].unique()
    for no in borehole_numbers:
        masws = []
        df_borehole = df[df["Profil No"] == no]
        for _, row in df_borehole.iterrows():
            masws.append(
                {
                    "thickness": row["Tabaka Kalınlığı"],
                    "compressionalWaveVelocity": row["Vp"],
                    "shearWaveVelocity": row["Vs"],
                }
            )
        data[no] = masws

    return data


def convert_ps_data(file_path):
    df = pandas.read_excel(file_path, sheet_name="PresioMeter")

    data = {}
    borehole_numbers = df["Sondaj No"].unique()
    for no in borehole_numbers:
        masws = []
        df_borehole = df[df["Sondaj No"] == no]
        for _, row in df_borehole.iterrows():
            masws.append(
                {
                    "depth": row["Derinlik"],
                    "limitPressure": row["PL"],
                    "netLimitPressure": row["Net PL"],
                }
            )
        data[no] = masws

    return data


def convert_site_investigation_data(file_path):
    data = {
        "boreHoleData": convert_borehole_data(file_path),
        "labExperiments": convert_lab_data(file_path),
        "sptData": convert_spt_data(file_path),
        "maswData": convert_masw_data(file_path),
        "pressuremeterData": convert_ps_data(file_path),
    }

    return data
