"""Interface interativa simples para baixar vídeos/áudio usando yt-dlp."""

import os
import sys

try:
    from yt_dlp import YoutubeDL
except ImportError as e:
    raise RuntimeError("yt-dlp não encontrado. Instale com: pip install yt-dlp") from e


def _normalize_query(raw: str) -> str:
    raw = raw.strip()
    if not raw:
        raise ValueError("Consulta vazia")
    if raw.startswith("http://") or raw.startswith("https://"):
        return raw
    if raw.startswith("ytsearch"):
        return raw
    return f"ytsearch1:{raw}"


def _prep_download_items(source_type: str, value: str) -> list[str]:
    if source_type == "1":
        return [_normalize_query(value)]

    if source_type == "2":
        if not os.path.isfile(value):
            raise FileNotFoundError(f"Arquivo não encontrado: {value}")

        lines = []
        with open(value, "r", encoding="utf-8") as f:
            for lin in f:
                lin = lin.strip()
                if not lin or lin.startswith("#"):
                    continue
                lines.append(_normalize_query(lin))

        if not lines:
            raise ValueError(f"Nenhuma URL/consulta válida encontrada no arquivo: {value}")
        return lines

    raise ValueError("Tipo de fonte inválido")


def _choose_output_path() -> str:
    outdir = input("Diretório de saída (em branco = diretório atual): ").strip()
    if not outdir:
        outdir = os.getcwd()
    if not os.path.isdir(outdir):
        os.makedirs(outdir, exist_ok=True)
    return outdir


def _choose_format() -> tuple[str, dict]:
    print("\nModo de download:")
    print("1) Vídeo + Áudio (arquivo de vídeo)")
    print("2) Somente áudio (MP3)")
    choice = input("Escolha 1 ou 2 [1]: ").strip() or "1"

    if choice == "2":
        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
        return "%(title)s.%(ext)s", ydl_opts

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
    }
    return "%(title)s.%(ext)s", ydl_opts


def download_items(items: list[str], outdir: str, out_template: str, ydl_opts: dict) -> None:
    ydl_opts = ydl_opts.copy()
    ydl_opts["outtmpl"] = os.path.join(outdir, out_template)

    with YoutubeDL(ydl_opts) as ydl:
        for src in items:
            print(f"\nBaixando: {src}")
            ydl.download([src])


def main() -> int:
    print("=== yt-dlb interativo (wrapper yt-dlp) ===")

    print("\nModo de entrada:")
    print("1) URL / termo de pesquisa")
    print("2) Ler lista de URL/termos de arquivo")
    source_type = input("Escolha 1 ou 2 [1]: ").strip() or "1"

    if source_type == "1":
        source_value = input("URL ou termo de busca: ").strip()
    else:
        source_value = input("Caminho do arquivo com URLs/termos (uma linha cada): ").strip()

    try:
        items = _prep_download_items(source_type, source_value)
    except Exception as e:
        print(f"Erro na entrada: {e}")
        return 1

    outdir = _choose_output_path()
    out_template, ydl_opts = _choose_format()

    try:
        download_items(items, outdir, out_template, ydl_opts)
    except Exception as e:
        print(f"Erro no download: {e}")
        return 2

    print("\nDownload concluído com sucesso.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
