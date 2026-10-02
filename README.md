# SEIRAMA Database MCP

MCP server terpisah untuk data alumni dari ClickHouse database `seirama`.

## Menjalankan

```powershell
pip install -e .
python database_server.py
```

Endpoint: `http://127.0.0.1:8002/mcp`

Tools: `get_alumni_angkatan_data`, `get_alumni_ringkas_data`.

## Menjalankan dengan Podman Compose

Jalankan ClickHouse:

```powershell
podman compose -f podman-compose.yml up -d
```

Restore backup ke volume Podman (jalankan saat container berhenti):

```powershell
podman compose -f podman-compose.yml down
podman run --rm `
	-v seirama_clickhouse_data:/target `
	-v "${PWD}/backups:/backup:ro" `
	docker.io/library/alpine:3.20 `
	sh -c "tar xzf /backup/database-mcp-clickhouse-20261001-084038.tar.gz -C /target"
podman compose -f podman-compose.yml up -d
```

Sesuaikan nama file backup jika menggunakan arsip yang berbeda.
