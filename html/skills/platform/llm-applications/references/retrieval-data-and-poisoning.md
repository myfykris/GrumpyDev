# LLM retrieval, data, and poisoning

Read this reference when the reviewed work directly or indirectly changes RAG, vector
indexes, embeddings, chunking,
ranking, citations, tenant filtering, training or fine-tuning data, feedback, memory,
ingestion, provenance, deletion propagation, or poisoning controls.

## Review requirements

- Enforce tenant and document authorization before retrieval and again before presenting or
  acting on retrieved content.

- Establish provenance, review, trust labels, ingestion validation, change control, deletion,
  and incident removal for training, fine-tuning, retrieval, feedback, memory, model, adapter,
  embedding, and prompt data. Detect poisoning and unexpected behavior rather than trusting a
  successful ingest.

- Scope vector indexes, caches, and retrieval filters by tenant and authorization. Cover hidden
  text, metadata, chunk overlap, embedding inversion or leakage, stale permissions, and deletion
  propagation.
