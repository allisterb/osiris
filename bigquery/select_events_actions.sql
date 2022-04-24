select distinct
    GLOBALEVENTID as ID,
    to_base64(sha1(concat(
        ifnull(Actor1Code,''), 
        ifnull(Actor1Name, ''), 
        ifnull(Actor1CountryCode, ''), 
        ifnull(Actor1KnownGroupCode, ''), 
        ifnull(Actor1EthnicCode, ''), 
        ifnull(Actor1Religion1Code, ''),
        ifnull(Actor1Religion2Code, ''), 
        ifnull(Actor1Type1Code, ''), 
        ifnull(Actor1Type2Code, ''), 
        ifnull(Actor1Type3Code, ''), 
        ifnull(Actor1Geo_Type, 0),
        ifnull(Actor1Geo_FullName, ''), 
        ifnull(Actor1Geo_CountryCode, ''), 
        ifnull(Actor1Geo_ADM1Code, ''), 
        ifnull(Actor1Geo_ADM2Code, ''), 
        ifnull(Actor1Geo_Lat, 0.0), 
        ifnull(Actor1Geo_Long, 0.0),
        ifnull(Actor1Geo_FeatureID, '')
    ))) as Actor1ID,
    to_base64(sha1(concat(
        ifnull(Actor2Code,''), 
        ifnull(Actor2Name, ''), 
        ifnull(Actor2CountryCode, ''), 
        ifnull(Actor2KnownGroupCode, ''), 
        ifnull(Actor2EthnicCode, ''), 
        ifnull(Actor2Religion1Code, ''),
        ifnull(Actor2Religion2Code, ''), 
        ifnull(Actor2Type1Code, ''), 
        ifnull(Actor2Type2Code, ''), 
        ifnull(Actor2Type3Code, ''), 
        ifnull(Actor2Geo_Type, 0),
        ifnull(Actor2Geo_FullName, ''), 
        ifnull(Actor2Geo_CountryCode, ''), 
        ifnull(Actor2Geo_ADM1Code, ''), 
        ifnull(Actor2Geo_ADM2Code, ''), 
        ifnull(Actor2Geo_Lat, 0.0), 
        ifnull(Actor2Geo_Long, 0.0),
        ifnull(Actor2Geo_FeatureID, '')
    ))) as Actor2ID,
    parse_date('%Y%m%d', cast(SQLDATE as string)) AS Date,
    cast(IsRootEvent as BOOL) as IsRoot,
    EventCode as CAMEOCode,
    EventBaseCode as BaseCAMEOCode,
    EventRootCode as RootCAMEOCode,
    QuadClass as CAMEOQuadClass,
    GoldsteinScale,
    NumMentions,
    NumSources,
    NumArticles,
    AvgTone,
    ActionGeo_Type as Geo_Type, 
    replace(ActionGeo_FullName, ',', ';') as Geo_FullName, 
    ActionGeo_CountryCode as Geo_CountryCode, 
    nullif(trim(concat(ifnull(ActionGeo_ADM1Code, ''), ' ', ifnull(ActionGeo_ADM2Code, ''))), '') as Geo_ADMCode,
    ActionGeo_Lat as Geo_Lat,
    ActionGeo_Long as Geo_Long,
    ActionGeo_FeatureID as Geo_FeatureID
    from `gdelt-bq.gdeltv2.events`
    where SQLDATE > 20220000 and SQLDATE < 20220421;