# SW Pack - 10 Frontend Accessibility Commercial Decisions

Decision scope
Use this matrix for UI architecture, accessibility, internationalization, docs, billing, metering, entitlements, and product lifecycle.

Frontend app shape
Options: SPA, SSR/SSG, MPA, native mobile, desktop, PWA, embedded widget.
Prefer when: app shape matches SEO, interactivity, offline needs, deployment, team skill, and accessibility obligations.
Avoid when: framework preference replaces user workflow and delivery constraints.
Metrics: Core Web Vitals where web, task completion, error rate, crash rate, bundle size, support tickets.

State strategy
Options: server state, client state, optimistic UI, offline-first sync, URL state, local persisted state.
Prefer when: source of truth, conflict handling, and recovery are explicit.
Avoid when: client state hides failed writes or creates data loss.
Metrics: stale state defects, sync conflict rate, failed optimistic updates, offline success.

Accessibility
Options: WCAG 2.2 A/AA/AAA target, keyboard support, semantic HTML, focus management, contrast, screen-reader paths, reduced motion.
Prefer when: accessibility target is part of definition of done.
Avoid when: accessibility is postponed until after UI is locked.
Metrics: automated audit findings, manual keyboard/screen-reader test pass, contrast issues, task completion for assistive flows.
Sources: WCAG 2.2.

Internationalization
Options: locale, timezone, currency, date/number formatting, pluralization, RTL, translation workflow.
Prefer when: target markets/users require locale correctness.
Avoid when: strings, dates, or currencies are hard-coded.
Metrics: i18n test coverage, missing translations, locale formatting defects, support tickets.
Sources: W3C Internationalization.

Documentation
Options: README, ADRs, API docs, architecture diagrams, runbooks, changelog, user docs, support scripts.
Prefer when: documentation maps to operation, onboarding, and audit needs.
Avoid when: docs duplicate code without ownership or freshness checks.
Metrics: docs freshness, broken link count, onboarding time, runbook coverage, support deflection.
Sources: arc42, C4, OpenAPI where relevant.

Billing
Options: free, flat subscription, seat-based, usage-based, tiered, credits/prepaid, enterprise contract, hybrid.
Prefer when: billing model aligns with value metric, metering accuracy, support cost, and legal/tax/payment constraints.
Avoid when: billing is selected before entitlements, invoicing, refunds, taxes, trials, and dunning are defined.
Metrics: conversion, churn, failed payment recovery, revenue leakage, support tickets, reconciliation errors.
Sources: Stripe billing docs and provider-specific docs.

Metering and entitlements
Options: provider-side usage records, internal ledger, event stream, quota counter, feature entitlement service.
Prefer when: idempotency, audit trail, reconciliation, fraud/abuse detection, and backfill are designed.
Avoid when: usage events are not deduplicated or cannot be replayed/reconciled.
Metrics: duplicate event rate, dropped usage events, reconciliation diff, quota breach, fraud signals.
Sources: Stripe idempotency and usage-based billing docs, PCI/GDPR/CCPA where applicable.

Lifecycle
Options: beta, GA, maintenance, deprecation, migration, end-of-life.
Prefer when: user communication, data export, migration path, and support ownership exist.
Avoid when: deprecated features remain unowned or compliance evidence expires.
Metrics: deprecation adoption, migration completion, support load, unresolved known risks.
Domain modeling considerations
Frontend state-model addition: model meaningful UI workflows as explicit states instead of boolean/null bags such as isLoading + errorMessage? + data? when those combinations can become invalid or ambiguous.
Prefer discriminated state variants for loading, empty, loaded, failed, offline, optimistic, conflict, permission-denied, billing-blocked, and deprecated states where applicable.
DTOs from APIs should be adapted into view models that make impossible UI states hard to represent, while preserving accessibility, localization, recovery, and telemetry needs.
