import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from mcp.server.fastmcp import FastMCP
from seirama_mcp.integrations.warehouse import get_alumni_angkatan, get_alumni_ringkas

mcp = FastMCP("seirama-database", host="0.0.0.0", port=8002)

@mcp.tool()
def get_alumni_angkatan_data(tahun: int | None = None) -> dict:
    """Mengambil alumni berdasarkan periode dan lembaga diklat."""
    data = get_alumni_angkatan(tahun)
    return {"source": "seirama.alumnidiklat_angkatan", "tahun": tahun, "count": len(data), "data": data}

@mcp.tool()
def get_alumni_ringkas_data(tahun: int | None = None) -> dict:
    """Mengambil alumni berdasarkan instansi, gender, wilayah, dan periode."""
    data = get_alumni_ringkas(tahun)
    return {"source": "seirama.alumnidiklat_ringkas", "tahun": tahun, "count": len(data), "data": data}

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
