select 
    replace(MentionIdentifier, ',', '%2C') as ID, 
    GLOBALEVENTID as EventID, 
    cast(parse_datetime('%Y%m%d%H%M%S', cast(MentionTimeDate as string)) as Date) as MentionDate,
    MentionType, 
    replace(MentionSourceName, ',', ';') as Source, 
    Confidence, 
    MentionDocTone 
from `gdelt-bq.gdeltv2.eventmentions` 
where confidence > 75 and EventTimeDate > 20220000000000 and EventTimeDate < 20220421000000