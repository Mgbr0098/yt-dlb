"""Entry point yt-dlb, reencaminha para yt-dlp."""

import sys

try:
    from yt_dlp.__main__ import main as ytdlp_main
except ImportError:
    try:
        from yt_dlp import main as ytdlp_main
    except ImportError as e:
        raise RuntimeError(
            "yt-dlp não encontrado. Instale com: pip install yt-dlp"
        ) from e


def main() -> int:
    """Executa a CLI de yt-dlp com os argumentos fornecidos."""
    if len(sys.argv) > 1 and sys.argv[1] in ("--interactive", "-i"):
        try:
            from yt_dlb.interactive import main as interactive_main
        except ImportError as e:
            raise RuntimeError(
                "Modo interativo não disponível. Verifique se o módulo `yt_dlb.interactive` existe."
            ) from e

        return interactive_main()

    return ytdlp_main()


if __name__ == "__main__":
    raise SystemExit(main())
