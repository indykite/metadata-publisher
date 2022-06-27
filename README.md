# Deployment Metadata Publisher 📜

❗**Note: Only for internal use**

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
        with:
          credentials_json: ${{ secrets.GCP_SERVICE_KEY }}
      - name: Checkout Analytics Repo
        uses: actions/checkout@v3
        with:
          token: ${{ secrets.<REPO_PAT> }}
          repository: indykite/analytics-prototype
          ref: v1.0.0
          path: deployment-analytics
      - name: Save Deployment Metadata
        if: ${{ always() }}
        uses: ./deployment-analytics
        with:
          env: <ENVIRONMENT>
          version: ${{ env.VERSION }}
          status: ${{ job.status }}
          bigquery_table: ${{ env.BIGQUERY_TABLE }}
```

To use it in your own repo, supply the repo's PAT and optionally specify
the appropriate environment(default is production).

As an example, the action is currently being used in the
[Indykite Console](https://github.com/indykite/indykite-console) repo.
