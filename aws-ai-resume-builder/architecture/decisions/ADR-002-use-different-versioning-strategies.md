# ADR-002: Use Different Versioning Strategies for S3 Buckets

## Status

Accepted

## Context

The resume upload bucket and generated website bucket store different types of data.

Uploaded resumes are temporary files. Each upload will use a unique object key, and the files will be automatically deleted after seven days.

Generated website files may be overwritten when:

* A user uploads an updated resume
* A portfolio website is regenerated
* A template is changed
* An incorrect file is deployed

## Decision

Configure versioning differently for the two buckets:

| Bucket                   | Versioning |
| ------------------------ | ---------- |
| Resume upload bucket     | Disabled   |
| Generated website bucket | Enabled    |

## Reasons

### Resume Upload Bucket

Versioning is disabled because:

* Uploaded resumes use unique object keys
* Resumes are temporary
* A lifecycle rule deletes them after seven days
* Retaining old versions may keep unnecessary personal information
* Previous versions would increase storage usage

### Generated Website Bucket

Versioning is enabled because:

* Website files may be overwritten
* Previous versions provide rollback capability
* Accidental deletion or replacement can be recovered
* Website regeneration may produce an incorrect result

## Alternatives Considered

### Enable Versioning on Both Buckets

This would provide recovery for uploaded resumes but would retain previous versions of sensitive documents and require additional lifecycle management.

### Disable Versioning on Both Buckets

This would reduce storage usage but would remove the ability to recover previously generated website files.

## Consequences

### Benefits

* Versioning is used only where it provides clear value
* Generated websites can be recovered
* Temporary resume storage remains simple
* Unnecessary retention of resume versions is avoided

### Trade-offs

* Website bucket storage usage may increase
* Noncurrent website versions may require a lifecycle rule later

## Outcome

Versioning will remain disabled on the temporary resume bucket and enabled on the generated website bucket.
