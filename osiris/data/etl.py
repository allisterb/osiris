from hashlib import sha1
from datetime import datetime
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

def calc_action_adm_code(r:pd.DataFrame):
    return ' '.join([
        r.ActionGeo_ADM1Code if not pd.isnull(r.ActionGeo_ADM1Code) else '',
        r.ActionGeo_ADM2Code if not pd.isnull(r.ActionGeo_ADM2Code) else ''
    ]).strip()

def shape_events_vertices(events:pd.DataFrame):
    from tqdm.auto import tqdm
    tqdm.pandas(total=len(events), unit='row', desc='Hashing Actor1 ID')
    actor1_id = events.progress_apply(calc_actor1_id, axis=1)
    actor1 = events.filter(regex='Actor1')
    events = events[events.columns.drop(list(actor1))]
    tqdm.pandas(total=len(events), unit='row', desc='Hashing Actor2 ID')
    actor2_id = events.progress_apply(calc_actor2_id, axis=1)
    actor2 = events.filter(regex='Actor2')
    events = events[events.columns.drop(list(actor2))]
    tqdm.pandas(total=len(events), unit='row', desc='Creating Action ADM Code')
    events_action_geo_adm_code = events.progress_apply(calc_action_adm_code, axis=1)
    events = events[events.columns.drop(['ActionGeo_ADM1Code', 'ActionGeo_ADM2Code'])]
    event_date = events['SQLDATE'].map(lambda x: datetime.strptime(str(x), '%Y%m%d'), na_action='ignore')
    events = events[events.columns.drop('SQLDATE')]
    is_root = events['IsRootEvent'].astype(bool)
    events['ActionGeo_FullName'] = events['ActionGeo_FullName'].str.replace(',', ';')
    events = events[events.columns.drop('IsRootEvent')]
    actor1.insert(0, 'ActorID', actor1_id)
    actor2.insert(0, 'ActorID', actor2_id)
    events.insert(1, 'Actor1ID', actor1_id)
    events.insert(2, 'Actor2ID', actor2_id)
    events.insert(3, 'Date', event_date)
    events.insert(4, 'IsRoot', is_root)
    events.insert(17, 'Geo_ADMCode', events_action_geo_adm_code)
    events  = events.rename({'GLOBALEVENTID': 'ID',}, axis=1)
    
    return events, (actor1 + actor2)
