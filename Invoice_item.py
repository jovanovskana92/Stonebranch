import csv
import collections

with open('INVOICE_EXTRACTED.csv') as f:
    r = csv.reader(f)
    header1 = next(r)
    dict1 = {row[0]: row[1:] for row in r}
dict2 = collections.defaultdict(list)
with open('INVOICE_ITEM.csv', 'r') as f:
    r = csv.reader(f)
    header2 = next(r)
    for row in r:
        dict2[row[0]].append(row[1:])

with open('INVOICE_ITEM_EXTRACTED.csv', 'w', newline='') as f:
    w = csv.writer(f)
    _ = w.writerow(header1 + header2[1:])
    empty2 = [[] * (len(header2) - 1)]
    for k in sorted(dict1.keys()):
        for row2 in dict2.get(k, empty2):
            _ = w.writerow([k] + dict1[k] + row2)
