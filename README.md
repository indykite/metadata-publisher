# Deployment Metadata Publisher 📜

❗**Note: This project has been deprecated and has been replaced by
the Four Keys deployment.
See
<https://www.notion.so/indykite/Four-Keys-360f3454fb474a30b02a14ec2dd6f949>
for details.**

This repository contains a Github action which publishes data about a release
deployment to a table in BigQuery. This is achieved via a Docker container
action referencing a Dockerfile. The resulting Docker image executes a Python
script which sends selected deployment metadata to a BigQuery table.

Currently tracked deployment data include:

* event type
* repo name
* environment
* version
* commit sha
* status
* creation date

## Action in action

Here's how one can use the action in its own workflow:

```
env:
  BIGQUERY_TABLE: jarvis-dev-268314.deployment_analytics.deployment_events

jobs:
  deploy:
    name: Deploy
    runs-on: ubuntu-latest
    steps:
      - name: Authenticate to Google Cloud
        uses: google-github-actions/auth@v0
        if: ${{ always() }}
        with:
          credentials_json: ${{ secrets.GCP_SERVICE_KEY }}
      - name: Publish Deployment Metadata
        if: ${{ always() }}
        uses: indykite/metadata-publisher@v0
        with:
          env: <ENVIRONMENT>
          version: ${{ env.VERSION }}
          status: ${{ job.status }}
          bigquery_table: ${{ env.BIGQUERY_TABLE }}
```

To use it in your own repo, supply the repo's PAT and optionally specify
the appropriate environment (default is production).

As an example, the action is currently being used in the
[Indykite Console](https://github.com/indykite/indykite-console) repo.
