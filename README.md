# Splunk Configuration Repository

This repository contains all Splunk infrastructure and application configurations following Splunk architectural best practices.

## Architecture Principles

### Separation of Concerns
- **Infrastructure Level**: Manages data flow, storage, and system settings
- **Application Level**: Manages data interpretation, parsing, and presentation
- **Deployment Level**: Manages configuration distribution

### Configuration Hierarchy
1. **System/Cluster Level**: Index definitions, server settings, cluster configuration
2. **Deployment Server**: Configuration distribution to server classes
3. **Applications**: Data parsing, dashboards, searches, alerts

## Repository Structure
splunk-config/
├── indexer-cluster/           # Indexer cluster management
│   ├── master-node/
│   │   ├── indexes.conf      # All index definitions
│   │   ├── server.conf       # Indexer cluster settings
│   │   └── outputs.conf      # Inter-cluster communication
│   └── peer-nodes/
│       └── server.conf       # Peer-specific settings
│
├── search-head-cluster/       # Search head cluster management
│   ├── deployer/
│   │   └── apps/            # Apps deployed to all search heads
│   └── members/
│       ├── server.conf      # Search head settings
│       └── distsearch.conf  # Distributed search config
│
├── deployment-server/         # Forwarder and base configuration management
│   ├── serverclass.conf     # Server class definitions
│   └── apps/
│       ├── _cluster/        # Cluster-wide configurations
│       ├── _indexer_base/   # Base config for all indexers
│       │   └── default/
│       │       └── indexes.conf
│       └── _forwarder_base/ # Base config for all forwarders
│           └── default/
│               ├── outputs.conf
│               └── deploymentclient.conf
│
├── apps/                      # Splunk applications (parsing, dashboards, searches)
│   ├── custom_logging/
│   │   ├── default/
│   │   │   ├── app.conf     # App metadata
│   │   │   ├── props.conf   # Data parsing rules
│   │   │   ├── transforms.conf # Field extractions
│   │   │   └── savedsearches.conf # Saved searches and alerts
│   │   ├── local/           # Environment-specific overrides
│   │   └── metadata/
│   │       └── local.meta   # Permissions and sharing
│   └── ta_examples/         # Technology Add-ons

## File Ownership Rules

### What Goes Where
- indexer-cluster/: Index definitions, cluster settings
- search-head-cluster/: Search-specific apps, knowledge objects  
- deployment-server/: Base configurations, server class definitions
- apps/: Data parsing, field extractions, dashboards, searches

### What NOT to Put in Apps
- Index definitions (indexes.conf)
- Server settings (server.conf)
- Cluster configurations
- System-level authentication/authorization
