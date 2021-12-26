import sys
import requests

from fixyourstreet_data.models.report import Report
from fixyourstreet_data.utils import (
    get_reports,
    save_reports
)


def main():

    base_url = 'http://fixyourstreet.ie/api?task=incidents&resp=json&by=maxid&id=%s'

    prev_max_id = -1
    max_id = sys.maxsize

    reports = get_reports()
    prev_report_ids = [r.incident.id for r in reports]

    if len(prev_report_ids):
        lowest_possible_id = max([i.incident.id for i in reports])
    else:
        lowest_possible_id = 0

    while max_id != prev_max_id:
        if int(max_id) < int(lowest_possible_id):
            break
        try:
            block = requests.get(
                base_url % max_id
            ).json()['payload']['incidents']
        except KeyError:
            break

        for report_data in block:
            report = Report(**report_data)
            if report.incident.id in prev_report_ids:
                continue
            reports.append(report)

        prev_max_id = max_id
        max_id = min([i['incident']['incidentid'] for i in block])

        print(len(reports))

    save_reports(reports)


if __name__ == '__main__':
    main()
