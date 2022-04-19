declare start_date INT64 DEFAULT 20220000;
declare end_date INT64 DEFAULT 20220421;

select distinct
    sha1(concat(
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
    )) as ActorID,
    GLOBALEVENTID as EventID,
    Actor1Code as ActorCode, 
    replace(Actor1Name, ',', ';') as ActorName, 
    Actor1CountryCode as ActorCountryCode, 
    Actor1KnownGroupCode as ActorKnownGroupCode, 
    Actor1EthnicCode as ActorEthnicCode, 
    nullif(trim(concat(ifnull(Actor1Religion1Code, ''), ' ', ifnull(Actor1Religion2Code, ''))), '')  as ActorReligion,
    nullif(trim(concat(ifnull(Actor1Type1Code, ''), ' ', ifnull(Actor1Type2Code, ''), ' ', ifnull(Actor1Type3Code, ''))), '') as ActorType,
    Actor1Geo_Type as ActorGeo_Type, 
    replace(Actor1Geo_FullName, ',', ';') as ActorGeo_FullName, 
    Actor1Geo_CountryCode as ActorGeo_CountryCode, 
    nullif(trim(concat(ifnull(Actor1Geo_ADM1Code, ''), ' ', ifnull(Actor1Geo_ADM2Code, ''))), '') as ActorGeo_ADMCode, 
    Actor1Geo_Lat as ActorGeo_Lat, 
    Actor1Geo_Long as ActorGeo_Long, 
    Actor1Geo_FeatureID as ActorGeo_FeatureID,
    parse_date('%Y%m%d', cast(SQLDATE as string)) AS EventDate 
    from `gdelt-bq.gdeltv2.events`
    where SQLDATE > start_date and SQLDATE < end_date;