# SW Pack - 05 API Integration Decisions

Decision scope
Use this matrix for public APIs, internal service contracts, browser/server communication, partner integrations, event contracts, and SDK strategy.

REST + OpenAPI
Prefer when: resource-oriented HTTP APIs, broad client tooling, public or partner contracts, cacheability, and documentation/discovery matter.
Avoid when: strongly typed low-latency internal RPC or bidirectional streaming is the primary need.
Evidence and metrics: OpenAPI lint/validation, contract tests, breaking-change count, cache hit rate, p95 latency, payload size, client support tickets.
Sources: RFC 9110 and OpenAPI specification.

gRPC + Protobuf
Prefer when: internal service-to-service contracts, typed schemas, efficient binary transport, streaming, and generated clients matter.
Avoid when: browser/public multi-client support requires simple HTTP semantics and no gateway strategy exists.
Evidence and metrics: proto compatibility checks, generated client usage, p95 latency, error rate, deadline/timeout behavior, streaming backpressure.
Sources: gRPC docs and protocol buffer ecosystem docs as applicable.

GraphQL
Prefer when: multiple frontends need flexible data selection, aggregation, schema-driven product evolution, and client query efficiency.
Avoid when: authorization, caching, N+1 prevention, query complexity limits, and schema governance are not designed.
Evidence and metrics: schema checks, resolver latency, query cost limits, cache behavior, authz tests, client adoption.
Sources: GraphQL official docs/spec.

Realtime / streaming / low-latency browser transport
Options: polling/long-polling, Server-Sent Events, WebSocket, WebRTC data channels, WebTransport over HTTP/3.
Prefer when: update direction, latency, ordering, reliability, browser support, infrastructure, and fallback requirements match the transport.
Avoid when: simpler HTTP request/response or event contracts solve the problem, browser/platform support is unverified, auth refresh/backpressure/reconnect behavior is undefined, or infrastructure/proxies/CDN do not support the path.
Evidence and metrics: browser support check, infrastructure/proxy/CDN test, connection count, reconnect behavior, backpressure, message latency, memory per connection, packet loss behavior, fallback plan.
Sources: WHATWG WebSockets, HTML Server-Sent Events, WebRTC/W3C, W3C WebTransport, MDN compatibility, and IETF HTTP/3/WebTransport-related specifications.

Event/message contracts
Prefer when: async workflows, decoupling, replay, auditability, and integration resilience matter.
Avoid when: request/response is simpler, ordering/idempotency is not defined, or schema governance is missing.
Evidence and metrics: schema registry compatibility, replay test, duplicate handling, consumer lag, dead-letter rate.

Typed same-language RPC
Prefer when: one full-stack language ecosystem owns both client and server and private speed of change matters.
Avoid when: public, cross-language, long-lived contracts are expected.
Evidence and metrics: type-check pass, generated/validated route contract, breaking-change count, SDK portability risk.

Cross-cutting gates
Every API decision must define versioning, authentication, authorization, input validation, idempotency/retry semantics, timeouts, error model, observability, and deprecation policy. Error-model consistency gate (not just presence): the service must expose ONE canonical error contract shared across every endpoint - a single Result-to-response (or exception-to-response) mapper - rather than each endpoint hand-rolling its own error shape. Name the wire format explicitly and prefer RFC 9457 Problem Details (application/problem+json) as the default HTTP error body unless a documented reason overrides it. Verifying "each endpoint has an error model" is insufficient - endpoints that each satisfy that locally still drift apart. Pin the contract with a cross-endpoint contract test (assert the same error envelope for validation, auth, not-found, conflict, and rate-limit cases across representative endpoints) so a new endpoint returning a divergent shape fails the build. This is the API-layer instance of the config-coherence rule: one source of truth for the error contract, enforced by a test, not by convention.
Domain modeling considerations
Cross-cutting gate addition: external API contracts and DTOs may be primitive-shaped for interoperability, but untrusted payloads must be parsed and validated at the boundary into commands, value objects, or domain types before core business logic runs.
Do not let OpenAPI/GraphQL/protobuf schemas become the only domain model. Explicitly document DTO-to-domain mapping, error model, idempotency keys, state transitions, and rejected invalid-state combinations.
Avoid API shapes that expose enum/status fields plus nullable companion data unless the state variants and required payloads are explicit and contract-tested.
