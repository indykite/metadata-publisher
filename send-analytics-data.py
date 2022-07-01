import argparse
import json
import os

from datetime import datetime
from google.cloud import bigquery

# Define arguments
parser = argparse.ArgumentParser()
parser.add_argument("event_name")
parser.add_argument("repository")
parser.add_argument("commit_sha")
parser.add_argument("env")
parser.add_argument("version")
parser.add_argument("status")
parser.add_argument("bigquery_table")
args = parser.parse_args()

env_str = args.env
env = env_str.split(":", 1)[1] if ":" in env_str else env_str

new_rows = [{
"event":      args.event_name, \
"repo_name":  args.repository.split("/", 1)[1], \
"commit_sha": args.commit_sha, \
"version":    args.version,    \
"status":     args.status, \
"env":        env, \
"created_at": datetime.isoformat(datetime.utcnow()) \
}]

client = bigquery.Client()

errors = client.insert_rows_json(args.bigquery_table, new_rows)

if errors == []:
    print("New rows have been added.")
else:
    print("Encountered errors while inserting rows: {}".format(errors))
