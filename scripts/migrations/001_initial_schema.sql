-- Migration: 001_initial_schema.sql
-- Description: Create iot_products and knowledge_base tables.

CREATE EXTENSION IF NOT EXISTS vector;

-- Table for IoT Hardware Catalog
CREATE TABLE IF NOT EXISTS iot_products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    brand VARCHAR(100),
    protocol VARCHAR(50), -- ex: Zigbee, Z-Wave, WiFi, Matter
    payload_yaml TEXT, -- YAML definition of the device's payloads/commands
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Table for RAG Knowledge Base
CREATE TABLE IF NOT EXISTS knowledge_base (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    embedding vector(1536), -- Vector size for OpenAI embeddings (Ada/v3)
    metadata JSONB DEFAULT '{}',
    source_uri VARCHAR(512), -- Source document path or URL
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create HNSW index for faster vector similarity search
CREATE INDEX ON knowledge_base USING hnsw (embedding vector_cosine_ops);
