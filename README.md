# yt-dlb

Uma ferramenta compatível com `yt-dlp` baseada em Python, projetada para reexportar toda a funcionalidade da biblioteca `yt-dlp`.

## Instalação

```bash
python -m pip install -e .
```

## Uso

```bash
yt-dlb https://www.youtube.com/watch?v=dQw4w9WgXcQ
yt-dlb -F https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

## Como funciona

O pacote chama o entrypoint `yt_dlp.main()` diretamente, então quase todas as opções e features do `yt-dlp` são suportadas.

## Uso interativo

O utilitário também oferece uma interface interativa para baixar por termo/URL e escolher diretório de saída:

```bash
yt-dlb --interactive
# ou
yt-dlb -i
# e também
yt-dlb-interactive
```

Na interface, você pode:
- informar uma URL de vídeo ou termo de pesquisa (ex: `Rick Astley`)
- apontar para um arquivo com uma lista de URLs/consultas (uma por linha)
- escolher diretório de saída
- escolher formato: vídeo+áudio ou somente áudio (MP3)

## Desenvolvimento

- Confira o repositório
- Instale com `pip install -e .`
- Execute `yt-dlb --help`
- Para testar internamente, rode `python -m yt_dlb --help`

