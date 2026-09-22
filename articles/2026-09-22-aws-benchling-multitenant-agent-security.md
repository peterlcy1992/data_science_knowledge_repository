---
id: aws-benchling-multitenant-agent-security
title: "How Benchling Secured Multi-Tenant AI Agents with Amazon Bedrock AgentCore"
source: "AWS Machine Learning Blog"
url: "https://aws.amazon.com/blogs/machine-learning/how-benchling-secured-multi-tenant-ai-agents-with-amazon-bedrock-agentcore/"
published: "2026-09"
added: "2026-09-22"
category: llm-genai
tags: [ai-agents, security, multi-tenant, code-interpreter, sandboxing, bedrock-agentcore]
novelty: 3
sourced_via: "web search"
---

# How Benchling Secured Multi-Tenant AI Agents with Amazon Bedrock AgentCore

**Source:** [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/how-benchling-secured-multi-tenant-ai-agents-with-amazon-bedrock-agentcore/) · Published 2026-09 · Added 2026-09-22
**Category:** LLMs & Generative AI · **Tags:** `ai-agents`, `security`, `multi-tenant`, `code-interpreter`, `sandboxing`, `bedrock-agentcore`

## TL;DR

Benchling, a biotech R&D platform, needed to let AI agents write and execute scientific code on behalf of thousands of regulated customer organizations without any code being able to read another tenant's data or exfiltrate anything over the network — including via DNS, a channel most sandboxing setups don't bother to lock down. Their layered defense-in-depth design has run since April 2026 with 600+ code-execution sessions/day across 250+ weekly tenants and zero security incidents.

## 1. Business context

Benchling operates in life sciences, where customer data is both sensitive and regulated. Giving AI agents a code interpreter — letting them write and run arbitrary code to do real scientific analysis — is, in the authors' words, "non-negotiable for scientific accuracy," but it inverts the usual trust model: the code being executed is agent- or user-generated, so the system has to assume any of it could be hostile, whether through malice or an LLM going off the rails. On a single-tenant system that's a containment problem. On a platform serving thousands of separate customer organizations from shared infrastructure, it's also an isolation problem — one tenant's code must never be able to touch another tenant's data, and Benchling needed to own that isolation itself rather than depend entirely on a third party's guarantees, given the regulated nature of the workloads.

## 2. Technical details

Benchling built a defense-in-depth architecture with several independent layers, so that a failure in any single control doesn't compromise isolation:

- **Account-level isolation.** A dedicated "Untrusted Code Account," separate from production infrastructure, hosts Amazon Bedrock AgentCore's Code Interpreter (ACCI) — so a breakout from the sandbox still lands in an account with no access to production data.
- **Network hardening.** The VPC has no internet gateway or NAT gateway at all. A Route 53 Resolver DNS Firewall runs a three-priority policy — P10 explicit blocklist, P100 strict allowlist, P200 catch-all deny — specifically because standard network egress controls often check IP/port traffic but overlook **DNS resolution** as an exfiltration channel (data can be smuggled out encoded in subdomain lookups even when direct network egress is blocked). Prefix-list routing and NACLs additionally restrict all traffic to port 443, and S3 access goes through VPC endpoints with restrictive bucket policies rather than general internet routing.
- **Credential scoping.** Each execution job gets its own temporary, narrowly scoped credentials via AWS STS, rather than a shared or long-lived role — preventing the kind of role sprawl that becomes unmanageable once you're serving thousands of tenants.
- **Continuous validation.** Automated integration tests continuously simulate attack patterns — DNS tunneling attempts, unauthorized network connections, cross-bucket access attempts — against the live environment, rather than treating the security design as a one-time review.

The overall design assumes breach at every layer: no single control (sandboxing alone, or network policy alone, or credential scoping alone) is trusted to hold the whole isolation guarantee by itself.

## 3. Impact — potential & realized

**Realized:** since deployment in April 2026, the system has handled **600+ code execution sessions daily** across **250+ distinct tenants per week**, with **zero security incidents** and **zero cross-tenant data leakage** reported.

**Potential:** the DNS-exfiltration-as-blind-spot point generalizes well beyond Benchling — any multi-tenant system giving LLM agents code execution capability (which is rapidly becoming standard for "agentic" coding and data-analysis products) faces the same exfiltration surface, and the layered account-isolation-plus-DNS-firewall-plus-scoped-credentials pattern is a directly reusable template for that broader class of products, not just biotech-specific.

---

## Claude's Take

> Opinion, not the source's claims.

### Novelty: 3/5 — solid, well-executed defense-in-depth, not a new technique

None of the individual controls here are novel — account isolation, DNS firewalls, scoped STS credentials, and continuous red-team-style testing are all standard security practice. The value is in applying that standard playbook rigorously and specifically to the AI-agent-code-execution problem, and in calling out DNS as an exfiltration channel that's genuinely easy to miss when teams focus egress controls on IP/port rules. As more products give LLM agents a code interpreter by default, this kind of "assume the generated code is hostile" architecture is exactly what more teams will need to adopt — it's a useful reference design even though it doesn't introduce new security theory.

### Similar / related work

- [**Govern AI Agent Tool Access with Amazon Bedrock AgentCore Gateway**](2026-09-03-aws-bedrock-agentcore-gateway-governance.md) (in this bank) — a complementary AgentCore capability, governing what tools an agent can call rather than sandboxing the code it runs; the two problems (tool-access governance vs. code-execution isolation) sit side by side in a full agent-security architecture.
- [**Reduce RAG Costs on Amazon Bedrock with Query-Aware Compression**](2026-09-02-aws-bedrock-query-aware-rag-compression.md) (in this bank) — a different AgentCore/Bedrock production concern (cost, not security) on the same underlying platform.
- General cloud-security literature on sandboxing, DNS exfiltration, and least-privilege credentialing — the broad prior art this design draws on; left unlinked as established practice rather than one paper.

### Jargon buster

- **Defense-in-depth** — a security design philosophy of layering multiple independent controls so that the failure of any single layer doesn't compromise the whole system.
- **DNS exfiltration** — smuggling data out of a network by encoding it in DNS lookup requests (e.g., as subdomains), a channel that's easy to overlook because DNS traffic is often allowed even when other outbound network access is blocked.
- **AWS STS (Security Token Service)** — an AWS service that issues short-lived, narrowly scoped temporary credentials, used here to give each code-execution job its own limited-permission identity instead of a long-lived shared role.
- **VPC endpoint** — a private connection from a Virtual Private Cloud directly to an AWS service (like S3) that doesn't route through the public internet, reducing the network surface an attacker could exploit.
