# Splunk Configuration Repository

This repository contains all Splunk infrastructure and application configurations following Splunk architectural best practices.

## Architecture Principles

**Separation of Concerns:**
- Infrastructure Level: Manages data flow, storage, and system settings
- Application Level: Manages data interpretation, parsing, and presentation  
- Deployment Level: Manages configuration distribution

## Repository Structure

### Infrastructure Components

**indexer-cluster/**
- master-node/indexes.conf (All index definitions)
- master-node/server.conf (Indexer cluster settings)
- peer-nodes/server.conf (Peer-specific settings)

**search-head-cluster/**
- deployer/apps/ (Apps deployed to all search heads)
- members/server.conf (Search head settings)
- members/distsearch.conf (Distributed search config)

**deployment-server/**
- serverclass.conf (Server class definitions)
- apps/_cluster/ (Cluster-wide configurations)
- apps/_indexer_base/default/indexes.conf (Base indexer config)
- apps/_forwarder_base/default/outputs.conf (Base forwarder config)

### Application Components

**apps/custom_logging/**
- default/app.conf (App metadata)
- default/props.conf (Data parsing rules)
- default/transforms.conf (Field extractions)
- local/ (Environment-specific overrides)
- metadata/local.meta (Permissions and sharing)

**universal-forwarders/**
- inputs.conf (Data input configurations)
- outputs.conf (Forwarding destinations)
- deploymentclient.conf (Deployment server connection)

## Configuration Guidelines

### Index Management
- Location: indexer-cluster/master-node/indexes.conf
- Principle: Indexes are infrastructure, not application-specific
- Naming: company_purpose_sensitivity

### Application Development  
- Location: apps/app_name/
- Contains: Parsing rules, dashboards, searches, alerts
- Does NOT contain: Index definitions, system settings

## File Ownership Rules

**indexer-cluster/**: Index definitions, cluster settings, replication factor

**search-head-cluster/**: Search-specific apps, knowledge objects shared across SH

**deployment-server/**: Base configurations, server class definitions

**apps/**: Data parsing, field extractions, dashboards, searches

**What NOT to Put in Apps:**
- Index definitions (indexes.conf)
- Server settings (server.conf) 
- Cluster configurations
- System-level authentication/authorization

## Development Workflow

1. Clone Repository
2. Create Feature Branch
3. Make Changes following directory structure guidelines
4. Test Locally using Docker environment
5. Submit PR with peer review required
6. Deploy via automated pipeline
