# SW Pack - 06 Data Consistency Privacy Decisions

Decision scope
Use this matrix for storage choices, data boundaries, transaction design, analytics/search/vector side stores, privacy, retention, and migration risk.

Relational SQL
Prefer when: transactional integrity, constraints, joins, reporting, mature migrations, and strong consistency are central.
Avoid when: schema volatility is extreme and migration discipline is absent.
Metrics: transaction latency, lock contention, migration duration, query plan health, restore test result, consistency violations.

Document database
Prefer when: aggregate-centric access, variable schema, and document-local reads/writes dominate.
Avoid when: cross-document transactions and relational reporting are primary needs unless officially supported and tested.
Metrics: document growth, query latency, index coverage, schema drift, migration complexity, consistency defects.

Key-value store / cache
Prefer when: very low-latency lookup, sessions, rate limits, caching, or ephemeral coordination matter.
Avoid when: it becomes the source of truth without durability, backup, eviction, and consistency design.
Metrics: hit rate, eviction rate, memory pressure, stale read rate, failover behavior.

Search index
Prefer when: relevance, full-text retrieval, faceting, or search UX matters.
Avoid when: it is treated as canonical data authority.
Metrics: indexing lag, query latency, relevance evaluation, drift from source of truth.

Columnar / OLAP
Prefer when: analytics, reporting, aggregates, and historical queries dominate.
Avoid when: transactional writes or low-latency per-record mutations dominate.
Metrics: ingestion lag, query cost, dashboard latency, freshness SLA.

Time-series
Prefer when: telemetry, IoT, financial ticks, or time-windowed metrics dominate.
Avoid when: arbitrary relational relationships or ad hoc entity queries dominate.
Metrics: write throughput, retention cost, downsampling accuracy, query latency.

Object storage
Prefer when: blobs, artifacts, backups, exports, media, and immutable objects dominate.
Avoid when: small mutable transactional records are the core access pattern.
Metrics: durability class, retrieval latency, lifecycle cost, checksum failures, restore test.

Vector database/index
Prefer when: semantic retrieval, RAG, similarity search, or embeddings are a proven requirement.
Avoid when: it becomes the source of truth or relevance quality is unmeasured.
Metrics: retrieval precision/recall, latency, index freshness, embedding drift, hallucination/evaluation failures.

Consistency patterns
Strong transaction: use when correctness needs atomic state changes and invariants.
Eventual consistency: use when temporary divergence is acceptable and reconciliation is defined.
Saga/outbox: use when distributed workflow needs reliable step progression and compensation.
CQRS: use when read/write models differ materially and consistency lag is acceptable.
CRDT/offline conflict handling: use when concurrent offline edits are expected and merge semantics are defined.

Privacy axes
Data minimization, purpose limitation, classification, retention, residency, lawful basis/consent, deletion/export, encryption, pseudonymization/anonymization, audit trail, breach response.

Primary source anchors
GDPR Article 5, GDPR Article 25, ISO/IEC 25010, NIST SSDF, Google SRE reliability practices.
Domain modeling considerations
Domain/persistence model addition: persistence design must support the domain model; it must not force core code into anemic records solely because the database row/document is primitive-shaped.
Map value objects, identities, timestamps, money, lifecycle state, approval state, privacy classification, and audit concepts explicitly. Store primitive columns/documents as needed, but reconstruct validated domain types on load and validate before save.
Consistency design must name the invariants protected by transactions, constraints, unique indexes, concurrency tokens, outbox/saga steps, or reconciliation. If an invariant is only protected by scattered validators, mark it as a risk.
