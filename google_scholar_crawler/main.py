from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])

# Guard against "soft failures": Google Scholar sometimes throttles without raising,
# returning an author with citedby=0 or no publications. Writing that would overwrite
# the good data on the google-scholar-stats branch. Exit non-zero instead so the
# workflow skips the push and the last successful data is retained.
if not author.get('citedby') or not author.get('publications'):
    raise SystemExit('Scholar returned incomplete data (likely rate-limited); '
                     'keeping the last successful data on the branch.')

name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
