import clickhouse_connect
from ..config import settings

_client = None

def client():
    global _client
    if _client is None:
        _client = clickhouse_connect.get_client(host=settings.db_host, port=settings.db_port, username=settings.db_username, password=settings.db_password, database=settings.db_name)
    return _client

def rows(result):
    return [dict(zip(result.column_names, row)) for row in result.result_rows]

def _query(table, tahun, columns, order):
    filter_sql = "WHERE startsWith(selesai_diklat, {tahun:String})" if tahun else ""
    params = {"tahun": str(tahun)} if tahun else {}
    return rows(client().query(f"SELECT {columns} FROM {table} {filter_sql} ORDER BY {order}", parameters=params))

def get_alumni_angkatan(tahun=None):
    return _query("seirama.alumnidiklat_angkatan", tahun, "program, selesai_diklat, nama_lemdik, instansi_lemdik, jumlah_alumni, jumlah_diklat", "selesai_diklat, nama_lemdik, program")

def get_alumni_ringkas(tahun=None):
    return _query("seirama.alumnidiklat_ringkas", tahun, "asal_instansi, program, jenis_kelamin, selesai_diklat, nama_lemdik, instansi_lemdik, kabkot_instansi, provinsi_instansi, jumlah_alumni, jumlah_diklat", "selesai_diklat, instansi_lemdik, program, jenis_kelamin")
