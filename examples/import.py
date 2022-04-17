if __name__ == '__main__': 
    from osiris_global import set_log_level
    set_log_level(debug = False)

    from rich import print

    from data.gdelt import DataSource
    gdelt = DataSource()

    events = gdelt.import_data('events', 'Nov-02-2021 02:00:00', 'Nov-02-2021 04:00:00')
    print(set(map(str, events['Actor1Name'].values)))
