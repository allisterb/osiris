declare start_date INT64 DEFAULT 20220000;
declare end_date INT64 DEFAULT 20220421;

select distinct
    sha1(concat(
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
    )) as ActorID,
    GLOBALEVENTID as EventID,
    Actor2Code as ActorCode, 
    replace(Actor2Name, ',', ';') as ActorName, 
    Actor2CountryCode as ActorCountryCode, 
    Actor2KnownGroupCode as ActorKnownGroupCode, 
    Actor2EthnicCode as ActorEthnicCode, 
    nullif(trim(concat(ifnull(Actor2Religion1Code, ''), ' ', ifnull(Actor2Religion2Code, ''))), '')  as ActorReligion,
    nullif(trim(concat(ifnull(Actor2Type1Code, ''), ' ', ifnull(Actor2Type2Code, ''), ' ', ifnull(Actor2Type3Code, ''))), '') as ActorType,
    Actor2Geo_Type as ActorGeo_Type, 
    replace(Actor2Geo_FullName, ',', ';') as ActorGeo_FullName, 
    Actor2Geo_CountryCode as ActorGeo_CountryCode, 
    nullif(trim(concat(ifnull(Actor2Geo_ADM1Code, ''), ' ', ifnull(Actor2Geo_ADM2Code, ''))), '') as ActorGeo_ADMCode, 
    Actor2Geo_Lat as ActorGeo_Lat, 
    Actor2Geo_Long as ActorGeo_Long, 
    Actor2Geo_FeatureID as ActorGeo_FeatureID,
    parse_date('%Y%m%d', cast(SQLDATE as string)) AS EventDate 
    from `gdelt-bq.gdeltv2.events`
    where SQLDATE > start_date and SQLDATE < end_date;