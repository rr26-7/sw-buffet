# sw-buffet page 15: Algorithm and Data Structure Decisions

Purpose
Keep algorithm and data-structure choices proportional to evidence. Frontier models know the algorithms; they fail by not noticing that code sits on a hot path (naive scans inside loops) or by over-engineering (a custom or exotic structure where the standard library meets the target). This page is a decision procedure plus a closed list of detectable anti-patterns. It is deliberately not a catalogue of algorithms to pick from.

Use when
An algorithm or data-structure choice sits on a hot path: code whose cost grows with input size or request volume on a user-facing, batch-critical, or cost-bearing path. Off a hot path, use the simplest correct choice and do not optimize without evidence.

Owner
Engineering and Performance. Architect is consulted when the choice changes a storage engine, a data boundary, or a contract; Decision Steward validates evidence and status.

Decision procedure (required for every hot-path choice)
1. Scale: expected N and its growth, with an evidence level (E0-E4). An E0 guess is allowed only when labeled and must name what would confirm it.
2. Access pattern: operations and their mix (lookup by key, ordered iteration, range queries, insert/delete ratio, priority access, concurrency).
3. Target: time and space complexity derived from N and the latency or cost budget, not from habit.
4. Default: the standard library or platform structure that meets the target. Name it.
5. Alternative: a custom, specialized, or third-party structure is acceptable only with E3 evidence - a benchmark on representative data showing that the default misses the target - plus a named maintenance owner. Hand-rolled storage engines (B-trees, LSM trees, custom databases) are rejected unless the decision is Mode H with that evidence.
6. Record the choice as a decision object: options, evidence, rejection reasons, and the review trigger (typically N or latency changing by an order of magnitude).

Anti-patterns (closed list)
These are defects on a hot path whenever N is not provably small. The list is closed so detection can be automated as candidate hits (page 12 gates 24 and 25, each check tested against a seeded instance per gate 30), while the hot-path judgment stays with the reviewer. Anything not on the list is not a defect by default; it needs a measured cost (E3 or E4).
AP1 - Linear search (contains, indexOf, find, list scan) on one collection inside a loop over another collection.
AP2 - Sorting, re-building, or re-indexing a collection inside a loop.
AP3 - Allocating temporary collections or buffers per iteration of a hot loop.
AP4 - Building strings by repeated concatenation in a loop instead of a builder or join.
AP5 - N+1 access: one query, remote call, or file read per item instead of a batched or joined access.
AP6 - Quadratic deduplication or pairwise comparison where hashing or sorting gives the same result.
AP7 - Recursion whose depth is controlled by input without an explicit bound.
AP8 - Loading an unbounded collection fully into memory instead of streaming or paginating.
AP9 - Recomputing a derived value in full on every request when it can be maintained incrementally or cached with a defined invalidation rule.

Illustrative defaults (not exhaustive, not a menu)
Library names, versions, and licensing are current-state claims: verify them against official documentation at use time (page 14 Class 3).
- Lookup by key: hash map or dictionary. Consider an ordered map or B-tree index only when ordered iteration or range queries are required.
- Ordered keys with range queries: the platform's sorted map or tree. Mostly static data: a sorted array with binary search.
- Priority scheduling: the standard priority queue (binary or d-ary heap). Consider an indexed heap only for decrease-key-heavy graph algorithms with E3 evidence.
- Grouping and connectivity: union-find with path compression and union by rank or size.
- Sorting: the standard library sort; a stable sort when order of equal keys matters; external or parallel sorting only for data that does not fit in memory or with E3 evidence.
- Large-scale membership with tolerable false positives: a Bloom filter from a maintained library.
- Persistent, write-heavy, or indexed storage: a database engine, not a hand-rolled structure.

Output
Hot-path choices appear in the decision inventory with scale evidence, target, the default considered, and - for any non-default - the benchmark evidence and owner. Anti-pattern findings map to page 12 gate 24 (touched code) or gate 25 (periodic sweep).
