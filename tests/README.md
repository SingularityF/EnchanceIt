# Tests

### gcs.sh
Test Google Cloud Storage public access by listing files inside bucket. Should always work even without a service account.

### gcs_write.sh
Test write access to Google Cloud Storage. Service account should have write access through the `Storage Object Admin` role.
