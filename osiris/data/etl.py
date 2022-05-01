from hashlib import sha1
import binascii

import pandas as pd

def calc_actor1_id(r:pd.DataFrame):
        return binascii.b2a_base64(sha1(''.join([
            r.Actor1Code if not pd.isnull(r.Actor1Code) else '', 
            r.Actor1Name if not pd.isnull(r.Actor1Name) else '',
            r.Actor1CountryCode if not pd.isnull(r.Actor1CountryCode) else '',
            r.Actor1KnownGroupCode if not pd.isnull(r.Actor1KnownGroupCode) else '',
            r.Actor1EthnicCode if not pd.isnull(r.Actor1EthnicCode) else '',
            r.Actor1Religion1Code if not pd.isnull(r.Actor1Religion1Code) else '',
            r.Actor1Religion2Code if not pd.isnull(r.Actor1Religion2Code) else '',
            r.Actor1Type1Code if not pd.isnull(r.Actor1Type1Code) else '',
            r.Actor1Type2Code if not pd.isnull(r.Actor1Type2Code) else '',
            r.Actor1Type3Code if not pd.isnull(r.Actor1Type3Code) else '',
            str(r.Actor1Geo_Type) if not pd.isnull(r.Actor1Geo_Type) else '',
            r.Actor1Geo_FullName if not pd.isnull(r.Actor1Geo_FullName) else '',
            r.Actor1Geo_CountryCode if not pd.isnull(r.Actor1Geo_CountryCode) else '',
            r.Actor1Geo_ADM1Code if not pd.isnull(r.Actor1Geo_ADM1Code) else '',
            r.Actor1Geo_ADM2Code if not pd.isnull(r.Actor1Geo_ADM2Code) else '',
            str(r.Actor1Geo_Lat)if not pd.isnull(r.Actor1Geo_Lat) else '',
            str(r.Actor1Geo_Long) if not pd.isnull(r.Actor1Geo_Long) else '',
            str(r.Actor1Geo_FeatureID) if not pd.isnull(r.Actor1Geo_FeatureID) else '',     
        ]).encode('utf-8')).digest()).strip().decode('utf-8')

def calc_actor2_id(r:pd.DataFrame):
        return binascii.b2a_base64(sha1(''.join([
            r.Actor2Code if not pd.isnull(r.Actor2Code) else '', 
            r.Actor2Name if not pd.isnull(r.Actor2Name) else '',
            r.Actor2CountryCode if not pd.isnull(r.Actor2CountryCode) else '',
            r.Actor2KnownGroupCode if not pd.isnull(r.Actor2KnownGroupCode) else '',
            r.Actor2EthnicCode if not pd.isnull(r.Actor2EthnicCode) else '',
            r.Actor2Religion1Code if not pd.isnull(r.Actor2Religion1Code) else '',
            r.Actor2Religion2Code if not pd.isnull(r.Actor2Religion2Code) else '',
            r.Actor2Type1Code if not pd.isnull(r.Actor2Type1Code) else '',
            r.Actor2Type2Code if not pd.isnull(r.Actor2Type2Code) else '',
            r.Actor2Type3Code if not pd.isnull(r.Actor2Type3Code) else '',
            str(r.Actor2Geo_Type) if not pd.isnull(r.Actor2Geo_Type) else '',
            r.Actor2Geo_FullName if not pd.isnull(r.Actor2Geo_FullName) else '',
            r.Actor2Geo_CountryCode if not pd.isnull(r.Actor2Geo_CountryCode) else '',
            r.Actor2Geo_ADM1Code if not pd.isnull(r.Actor2Geo_ADM1Code) else '',
            r.Actor2Geo_ADM2Code if not pd.isnull(r.Actor2Geo_ADM2Code) else '',
            str(r.Actor2Geo_Lat)if not pd.isnull(r.Actor2Geo_Lat) else '',
            str(r.Actor2Geo_Long) if not pd.isnull(r.Actor2Geo_Long) else '',
            str(r.Actor2Geo_FeatureID) if not pd.isnull(r.Actor2Geo_FeatureID) else '',     
        ]).encode('utf-8')).digest()).strip().decode('utf-8')

def shape_events_vertices(events:pd.DataFrame):
    from tqdm.auto import tqdm
    tqdm.pandas(total=len(events), unit='row', desc='Hashing Actor1 ID')
    events.insert(1, 'Actor1ID', events.progress_apply(calc_actor1_id, axis=1))
    tqdm.pandas(total=len(events), unit='row', desc='Hashing Actor2 ID')
    events.insert(2, 'Actor2ID', events.progress_apply(calc_actor2_id, axis=1))
    return events
