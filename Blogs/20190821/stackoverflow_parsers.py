

def stackoverflow_feed_sorter(feed, master_keys=['id', 'title', 'summary',
                                                 'location', 'updated',
                                                 'published']):
    """
    Accepts feedparser.parse results from stackoverflow's job search RSS feed.
    Returns dictionary of last feed results.
    """
    out_all = []
    for entry in feed.entries:
        out = standardize_dict(entry, master_keys)
        out_all.append(out)
    return out_all


def standardize_dict(dictionary, master):
    """
    Check dictionary keys against master list. Return standardized output
    """
    out = dict()
    for entry in master:
        if entry in dictionary.keys():
            out[f'{entry}'] = dictionary[f'{entry}']
        else:
            out[f'{entry}'] = 'None'
    return out
