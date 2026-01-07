# LLM Gateway

A production-oriented LLM platform gateway that provides a unified, secure, and observable interface
for accessing large language models across multiple providers.

## Overview

LLM Gateway is a backend platform service designed to standardize how applications
access large language models (LLMs) inside an organization.

Instead of allowing each product or service to directly integrate with LLM providers
(e.g. OpenAI, Anthropic), LLM Gateway acts as a centralized entry point that handles:

- Provider abstraction
- Request routing and fallback
- Authentication and access control
- Cost and usage observability
- Platform-level policies and safeguards

This project focuses on **platform engineering**, not model experimentation.

## Why LLM Gateway

Directly integrating LLM providers into individual applications leads to:

- Tight coupling to vendor-specific APIs
- Duplicated prompt and retry logic
- Poor cost visibility and control
- Inconsistent authentication and security practices
- Difficult debugging and incident response

LLM Gateway solves these problems by introducing a **single, reusable platform layer**
between applications and LLM providers.

## Core Concepts

- **Gateway Pattern**  
  All LLM traffic flows through a single gateway service.

- **Provider Abstraction**  
  Applications interact with logical model aliases instead of vendor-specific model IDs.

- **Platform Ownership**  
  Authentication, rate limiting, retries, and observability are handled at the platform level.

- **Separation of Concerns**  
  Product teams focus on business logic; the platform manages LLM complexity.

## Getting Started

### Requirements

- Python 3.11+
- pip
- Git

### Installation

```bash
git clone git@github.com:yujieyangeve/llm-gateway.git
cd llm-gateway
pip install -e .
```

### Run locally
uvicorn llm_gateway.main:app --reload --port 8001

### Docs
http://127.0.0.1:8001/docs

## API Endpoints

### Health

- `GET /health/live`
- `GET /health/ready`

### Chat (planned)

- `POST /v1/chat`

All endpoints return a `X-Request-Id` header for request tracing.

## Roadmap
- [ ] Unified `/v1/chat` endpoint
- [ ] Better manage api_key
- [ ] Add AuthMiddleware for specific endpoint
- [ ] Multi-provider routing and fallback
- [ ] Usage and cost tracking
- [ ] Rate limiting and quotas
- [ ] Evaluation and observability hooks
- [ ] Agent orchestration support